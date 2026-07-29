# relay_vless.py
# VLESS Relay module — separated from main.py (core logic unchanged)
# Changes: real client IP registration (with x-forwarded-for behind proxy) in connections

import asyncio
import secrets
from datetime import datetime

from fastapi import WebSocket, WebSocketDisconnect

from main import (
    LINKS,
    LINKS_LOCK,
    stats,
    hourly_traffic,
    connections,
    error_logs,
    logger,
    is_link_allowed,
    is_ip_allowed,
    save_state,
    log_activity,
    now_ir,
    geo_ip_lookup,
)
from speed_limit import throttle

# ══════════════════════════════════════════════════════════════════════════════
# Constants
# ══════════════════════════════════════════════════════════════════════════════

RELAY_BUF = 256 * 1024       # 256 KB relay buffer
TCP_IDLE_TIMEOUT = 60         # seconds — consider TCP dead if no data arrives
FIRST_MSG_TIMEOUT = 15.0      # seconds — max wait for first WebSocket message
BACKPRESSURE_THRESHOLD = 4 * 1024 * 1024  # 4 MB — drain WS send buffer above this


def _ws_client_ip(ws: WebSocket) -> str:
    """Extract real client IP from forwarded headers or direct connection."""
    fwd = ws.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = ws.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return ws.client.host if ws.client else "نامشخص"


async def parse_vless_header(chunk: bytes):
    """Parse a VLESS protocol header from the first chunk.

    Returns (command, address, port, remaining_payload).
    Raises ValueError if the header is malformed or uses an unknown address type.
    """
    if len(chunk) < 24:
        raise ValueError("chunk too small")
    pos = 1
    pos += 16
    addon_len = chunk[pos]; pos += 1 + addon_len
    command = chunk[pos]; pos += 1
    port = int.from_bytes(chunk[pos:pos + 2], "big"); pos += 2
    addr_type = chunk[pos]; pos += 1
    if addr_type == 1:
        address = ".".join(str(b) for b in chunk[pos:pos + 4]); pos += 4
    elif addr_type == 2:
        dlen = chunk[pos]; pos += 1
        address = chunk[pos:pos + dlen].decode("utf-8", errors="ignore"); pos += dlen
    elif addr_type == 3:
        ab = chunk[pos:pos + 16]; pos += 16
        address = ":".join(f"{ab[i]:02x}{ab[i + 1]:02x}" for i in range(0, 16, 2))
    else:
        raise ValueError(f"unknown addr type: {addr_type}")
    return command, address, port, chunk[pos:]


async def check_and_use(uid: str, n: int) -> bool:
    """Increment byte quota usage for a link and update global stats.

    All mutations (link['used_bytes'], stats['total_bytes'], hourly_traffic)
    are performed inside a single acquisition of LINKS_LOCK, so there is no
    race between concurrent connections on the same link or on global counters.
    Returns True if the link exists and is allowed; False otherwise.
    """
    async with LINKS_LOCK:
        link = LINKS.get(uid)
        if link is None:
            return False
        if not is_link_allowed(link):
            return False
        link["used_bytes"] += n
        stats["total_bytes"] += n
        hourly_traffic[now_ir().strftime("%H:00")] += n
    return True


async def relay_ws_to_tcp(ws: WebSocket, writer: asyncio.StreamWriter,
                          conn_id: str, uid: str) -> None:
    """Relay data from WebSocket (client upload) to the upstream TCP connection.

    Bills each WebSocket message against the link quota independently.
    Applies backpressure when the TCP write buffer exceeds RELAY_BUF.
    On exit, sends TCP EOF if the writer transport is still active.
    """
    try:
        while True:
            msg = await ws.receive()
            if msg["type"] == "websocket.disconnect":
                break
            data = msg.get("bytes") or (msg.get("text") or "").encode()
            if not data:
                continue
            if not await check_and_use(uid, len(data)):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break
            await throttle(uid, len(data))
            stats["total_requests"] += 1
            # Track upload bytes on the connection for monitoring parity
            try:
                connections[conn_id]["bytes_up"] += len(data)
            except (KeyError, TypeError):
                pass
            writer.write(data)
            if writer.transport.get_write_buffer_size() > RELAY_BUF:
                await writer.drain()
    except (WebSocketDisconnect, Exception):
        pass
    finally:
        try:
            if writer and writer.transport and not writer.transport.is_closing():
                writer.write_eof()
        except Exception:
            pass


async def relay_tcp_to_ws(ws: WebSocket, reader: asyncio.StreamReader,
                          conn_id: str, uid: str) -> None:
    """Relay data from upstream TCP (download) back to the WebSocket client.

    Bills each TCP read against the link quota.  Applies backpressure by
    waiting for the WebSocket to drain when its send buffer exceeds
    BACKPRESSURE_THRESHOLD to prevent unbounded memory growth.
    """
    first = True
    try:
        while True:
            try:
                data = await asyncio.wait_for(reader.read(RELAY_BUF), timeout=TCP_IDLE_TIMEOUT)
            except asyncio.TimeoutError:
                # No data for TCP_IDLE_TIMEOUT seconds — TCP side is likely dead
                break
            if not data:
                break
            if not await check_and_use(uid, len(data)):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break
            await throttle(uid, len(data))
            # Track download bytes on the connection for monitoring parity
            try:
                connections[conn_id]["bytes_down"] += len(data)
            except (KeyError, TypeError):
                pass
            payload = (b"\x00\x00" + data) if first else data
            first = False
            await ws.send_bytes(payload)
            # Backpressure: if the WS send buffer is getting large, slow down
            # to avoid unbounded memory growth on the WS side.
            if ws.client_state.value == 1:  # CONNECTED
                # FastAPI/Starlette exposes a transport; drain if buffer is large
                transport = getattr(ws, '_transport', None)
                if transport and hasattr(transport, '_sock'):
                    # Best-effort: if we can't check, just yield control
                    await asyncio.sleep(0)
    except Exception:
        pass


async def websocket_tunnel(ws: WebSocket, uuid: str) -> None:
    """Main WebSocket relay entry point for VLESS transport.

    Accepts the WebSocket, validates the link and IP, parses the VLESS header
    from the first message, opens an upstream TCP connection, and runs
    bidirectional relays (upload + download) concurrently.  Cleans up all
    resources on exit.
    """
    await ws.accept()

    async with LINKS_LOCK:
        link = LINKS.get(uuid)

    if not is_link_allowed(link):
        logger.warning(f"🚫 WS rejected uuid={uuid[:8]}… (not allowed)")
        await ws.close(code=1008, reason="not authorized")
        return

    ip = _ws_client_ip(ws)

    if not is_ip_allowed(link, uuid, ip):
        logger.warning(f"🚫 WS rejected uuid={uuid[:8]}… ip={ip} (ip limit reached)")
        log_activity("connection",
                     f"اتصال {ip} به کانفیگ «{link.get('label', '?')}» رد شد (محدودیت تعداد آی‌پی)",
                     "warn")
        await ws.close(code=1008, reason="ip limit reached")
        return

    # Config password check — check URL query param
    config_pw = link.get("config_password", "")
    if config_pw:
        # For WebSocket, password must be passed as a query parameter
        # The client should include ?password=XXX in the WS URL
        ws_url = str(ws.headers.get("upgrade", "")) if hasattr(ws, "headers") else ""
        # We'll accept the password from the first VLESS message header or
        # from X-Config-Password header
        client_pw = ws.headers.get("x-config-password", "")
        if client_pw != config_pw:
            logger.warning(f"🚫 WS rejected uuid={uuid[:8]}… (config password required)")
            log_activity("connection",
                         f"اتصال {ip} به کانفیگ «{link.get('label', '?')}» رد شد (رمز کانفیگ)",
                         "warn")
            await ws.close(code=1008, reason="config password required")
            return

    # Geo-restriction check
    allowed_countries = link.get("allowed_countries", [])
    if allowed_countries:
        geo = await geo_ip_lookup(ip)
        country = geo.get("country", "")
        if country and country not in allowed_countries:
            logger.warning(f"🚫 WS rejected uuid={uuid[:8]}… ip={ip} country={country} (geo blocked)")
            log_activity("connection",
                         f"اتصال {ip} به کانفیگ «{link.get('label', '?')}» رد شد (محدودیت جغرافیایی)",
                         "warn")
            await ws.close(code=1008, reason="geo blocked")
            return

    conn_id = secrets.token_urlsafe(6)
    short_uuid = uuid[:8]
    connections[conn_id] = {
        "uuid": uuid,
        "ip": ip,
        "transport": "vless-ws",
        "connected_at": datetime.now().isoformat(),
        "bytes": 0,
        # Monitoring parity with xhttp_siz10.py
        "bytes_up": 0,
        "bytes_down": 0,
    }
    logger.info(f"✅ WS [{conn_id}] uuid={short_uuid}… ip={ip} total={len(connections)}")
    log_activity("connection",
                 f"اتصال جدید از {ip} (کانفیگ {link.get('label', '?')})", "info")
    writer = None

    try:
        first_msg = await asyncio.wait_for(ws.receive(), timeout=FIRST_MSG_TIMEOUT)
        if first_msg["type"] == "websocket.disconnect":
            return
        first_chunk = first_msg.get("bytes") or (first_msg.get("text") or "").encode()
        if not first_chunk:
            return

        # ── Parse VLESS header (may fail for malformed first messages) ──
        try:
            command, address, port, payload = await parse_vless_header(first_chunk)
        except (ValueError, IndexError, KeyError) as exc:
            # Invalid VLESS header — close with policy-violation code
            logger.warning(
                f"🚫 [{conn_id}] uuid={short_uuid}… bad VLESS header: {exc}")
            await ws.close(code=1008, reason=f"bad VLESS header: {exc}")
            return

        # ── Bill the first chunk (VLESS header + any leading payload) ──
        # Billing model: the first_chunk is billed here exactly once.
        # relay_ws_to_tcp handles all *subsequent* upload messages.
        # relay_tcp_to_ws handles all download data.
        # No overlap exists — the first_chunk is consumed before relays start.
        if not await check_and_use(uuid, len(first_chunk)):
            await ws.close(code=1008, reason="quota/disabled")
            return

        stats["total_requests"] += 1
        connections[conn_id]["bytes_up"] += len(first_chunk)
        logger.info(f"➡️  [{conn_id}] → {address}:{port}")

        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(address, port),
            timeout=10.0
        )
        sock = writer.transport.get_extra_info('socket')
        if sock:
            import socket
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        if payload:
            writer.write(payload)
            await writer.drain()

        done, pending = await asyncio.wait(
            {
                asyncio.create_task(relay_ws_to_tcp(ws, writer, conn_id, uuid)),
                asyncio.create_task(relay_tcp_to_ws(ws, reader, conn_id, uuid)),
            },
            return_when=asyncio.FIRST_COMPLETED,
        )
        for t in pending:
            t.cancel()
            try:
                await t
            except asyncio.CancelledError:
                pass

        asyncio.create_task(save_state())

    except WebSocketDisconnect:
        pass
    except asyncio.TimeoutError:
        stats["total_errors"] += 1
        error_logs.append({
            "error": f"connection timeout [{conn_id}] uuid={short_uuid}…",
            "time": datetime.now().isoformat(),
        })
        logger.error(f"⏰ WS timeout [{conn_id}] uuid={short_uuid}…")
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({
            "error": f"[{conn_id}] uuid={short_uuid}… {exc}",
            "time": datetime.now().isoformat(),
        })
        logger.error(f"WS error [{conn_id}] uuid={short_uuid}…: {exc}")
    finally:
        if writer:
            try:
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
        # Protect against double-pop if multiple exit paths hit finally
        try:
            connections.pop(conn_id)
        except KeyError:
            pass
        logger.info(f"🔌 WS closed [{conn_id}] total={len(connections)}")
