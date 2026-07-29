# xhttp_siz10.py
# ══════════════════════════════════════════════════════════════════════════════
# Siz10a · XHTTP Ultra Transport — مود auto (packet-up / stream-up)
#  مسیر سرور دیگه به مود بستگی نداره (مطابق رفتار واقعی mode=auto در Xray):
#  کلاینت خودش بر اساس نوع اتصال (H2/REALITY یا نه) بین packet-up و
#  stream-up انتخاب می‌کنه، و مود واقعی فقط از روی شکل درخواست POST
#  (وجود یا عدم وجود seq در انتهای مسیر) روی سرور تشخیص داده می‌شه.
#  (stream-one حذف شد. منطق relay_vless دست‌نخورده.
#   stream-up بازنویسی شده با موتور تطبیقی: _AdaptiveFlow (AIMD روی high-water)
#   + _QuotaGate تطبیقی (batch بر اساس نرخ واقعی هر سشن) + سوکت تیون‌شده)
# ══════════════════════════════════════════════════════════════════════════════

import asyncio
import secrets
import socket
import time
from datetime import datetime

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse

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
    geo_ip_lookup,
)
from relay_vless import parse_vless_header, check_and_use
from speed_limit import throttle

router = APIRouter()

XHTTP_BUF = 512 * 1024
DOWNLINK_QUEUE_MAX = 512
SESSION_IDLE_TIMEOUT = 30
REAPER_INTERVAL = 10
TCP_CONNECT_TIMEOUT = 10.0
MAX_SEQ_BUF = 128
TCP_IDLE_TIMEOUT = 60  # seconds: tear down TCP if no data received for this long
LINK_REVALIDATE_INTERVAL = 5.0  # seconds: re-check link active status periodically

# ── تنظیمات موتور تطبیقی ──────────────────────────────────────────────────────
SOCK_BUF_SIZE = 2 * 1024 * 1024     # SO_SNDBUF / SO_RCVBUF

# _AdaptiveFlow: بازه‌ی مجاز برای high-water تطبیقی (AIMD)
FLOW_MIN_HW = 256 * 1024
FLOW_MAX_HW = 16 * 1024 * 1024
FLOW_START_HW = 2 * 1024 * 1024
FLOW_FAST_DRAIN_MS = 2.0    # زیر این یعنی downstream خیلی سریعه → بافر مجاز رو زیاد کن
FLOW_SLOW_DRAIN_MS = 25.0   # بالای این یعنی backpressure واقعی → فوری نصفش کن

# _QuotaGate: بازه‌ی مجاز برای batch تطبیقی چک کوتا
QUOTA_MIN_BATCH = 32 * 1024
QUOTA_MAX_BATCH = 1 * 1024 * 1024
QUOTA_START_BATCH = 64 * 1024
QUOTA_CHECK_INTERVAL = 0.2  # سقف زمانی؛ حتی اگر batch پر نشده، بعد این مدت چک کن

PACKET_UP_HIGH_WATER = 2 * 1024 * 1024  # packet-up همون منطق ساده‌ی قبلی رو داره (تمرکز این راند فقط stream-up بود)

xhttp_sessions: dict = {}
XHTTP_LOCK = asyncio.Lock()

FINGERPRINTS = {
    "chrome": {
        "content-type": "application/grpc",
        "cache-control": "no-cache, no-store",
        "x-accel-buffering": "no",
        "server": "cloudflare",
    },
    "plain": {
        "content-type": "application/octet-stream",
        "cache-control": "no-store",
        "x-accel-buffering": "no",
    },
}
DEFAULT_FINGERPRINT = "chrome"


def _resp_headers(fp: str) -> dict:
    return dict(FINGERPRINTS.get(fp, FINGERPRINTS[DEFAULT_FINGERPRINT]))


def _tune_socket(writer: asyncio.StreamWriter):
    """TCP_NODELAY + بافرهای بزرگ‌تر سوکت برای کاهش سربار سیستم‌عامل روی ترافیک بالا."""
    sock = writer.transport.get_extra_info("socket")
    if not sock:
        return
    try:
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SOCK_BUF_SIZE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, SOCK_BUF_SIZE)
    except OSError:
        pass


# ── helpers ────────────────────────────────────────────────────────────────────

def _bump_bytes(sess: dict, n: int) -> None:
    """Safely increment per-session byte counters and the global connection record.

    Increments sess['bytes_up'] (or 'bytes_down') and the shared connections
    dict entry atomically from asyncio's single-threaded perspective — no OS
    lock needed because there is no preemption between *await* points.
    """
    conn = connections.get(sess.get("conn_id"))
    if conn:
        conn["bytes"] += n


def _trim_seq_buf(sess: dict) -> None:
    """Drop oldest seq_buf entries if the buffer exceeds MAX_SEQ_BUF.

    Logs a warning so operators know out-of-order packets are piling up.
    """
    buf = sess.get("seq_buf", {})
    if len(buf) > MAX_SEQ_BUF:
        excess = len(buf) - MAX_SEQ_BUF
        oldest_keys = sorted(buf.keys())[:excess]
        for k in oldest_keys:
            buf.pop(k, None)
        logger.warning(
            f"⚠ XHTTP seq_buf overflow session=[{sess.get('conn_id', '?')[:8]}] "
            f"dropped {excess} oldest buffered packets (limit={MAX_SEQ_BUF})"
        )


# ── Quota Gate & Adaptive Flow (unchanged) ────────────────────────────────────

class _QuotaGate:
    """
    نسخه‌ی تطبیقی: به‌جای await check_and_use() به‌ازای هر چانک، و به‌جای یک آستانه‌ی
    ثابت، نرخ واقعی ترافیک هر سشن رو با EWMA اندازه می‌گیره و اندازه‌ی batch رو زنده
    عوض می‌کنه:
      - سشن پرسرعت (دانلود حجیم) → batch بزرگ می‌شه → await های سنگین کمتر.
      - سشن کم‌ترافیک/تعاملی → batch کوچیک می‌مونه → کوتا دقیق‌تر و قطع سریع‌تر
        اگه کاربر تموم کرده باشه.
    داده هیچ‌وقت نگه داشته نمی‌شه، فقط لحظه‌ی چک‌کردنِ کوتا adaptive هست.
    """
    __slots__ = ("uuid", "pending", "last_check", "ok", "batch_bytes", "rate_ewma")

    def __init__(self, uuid: str):
        self.uuid = uuid
        self.pending = 0
        self.last_check = time.monotonic()
        self.ok = True
        self.batch_bytes = QUOTA_START_BATCH
        self.rate_ewma = 0.0

    async def add(self, nbytes: int) -> bool:
        if not self.ok:
            return False
        self.pending += nbytes
        now = time.monotonic()
        elapsed = now - self.last_check
        if self.pending >= self.batch_bytes or elapsed >= QUOTA_CHECK_INTERVAL:
            flush, self.pending = self.pending, 0
            if elapsed > 0:
                inst_rate = flush / elapsed
                self.rate_ewma = inst_rate if self.rate_ewma == 0 else (0.7 * self.rate_ewma + 0.3 * inst_rate)
                target = int(self.rate_ewma * QUOTA_CHECK_INTERVAL)
                self.batch_bytes = max(QUOTA_MIN_BATCH, min(QUOTA_MAX_BATCH, target or QUOTA_MIN_BATCH))
            self.last_check = now
            self.ok = await check_and_use(self.uuid, flush)
            return self.ok
        return True

    async def flush(self) -> bool:
        if self.pending:
            flush, self.pending = self.pending, 0
            self.ok = self.ok and await check_and_use(self.uuid, flush)
        return self.ok


class _AdaptiveFlow:
    """
    high-water تطبیقی برای drain(), رفتار شبیه AIMD در TCP congestion control:
      - هر بار drain() صدا زده می‌شه، مدت زمانش اندازه‌گیری می‌شه.
      - اگه سریع تموم بشه (لینک پایین‌دستی داره جواب می‌ده) → سقف بافر مجاز رو
        additive increase می‌کنیم؛ یعنی دفعه‌ی بعد دیرتر drain صدا زده می‌شه،
        پس syscall/context-switch کمتر می‌شه و throughput واقعی بالا می‌ره.
      - اگه drain کند بشه (backpressure واقعیه، صف داره جمع می‌شه) → سقف رو فوری
        نصف می‌کنیم (multiplicative decrease) تا بافربلوت/لتنسی رشد نکنه.
    هر سشن یک نمونه‌ی جدا از این داره، پس مسیرهای کند و سریع تداخلی با هم ندارن.
    """
    __slots__ = ("high_water", "last_drain_ms")

    def __init__(self):
        self.high_water = FLOW_START_HW
        self.last_drain_ms = 0.0

    def should_drain(self, buf_size: int) -> bool:
        return buf_size > self.high_water

    async def drain(self, writer: asyncio.StreamWriter):
        t0 = time.monotonic()
        await writer.drain()
        elapsed_ms = (time.monotonic() - t0) * 1000
        self.last_drain_ms = elapsed_ms
        if elapsed_ms < FLOW_FAST_DRAIN_MS:
            self.high_water = min(FLOW_MAX_HW, int(self.high_water * 1.5) + 65536)
        elif elapsed_ms > FLOW_SLOW_DRAIN_MS:
            self.high_water = max(FLOW_MIN_HW, self.high_water // 2)


def _req_client_ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = request.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "نامشخص"


# ── TCP helpers ────────────────────────────────────────────────────────────────

async def _open_tcp_from_header(first_chunk: bytes):
    """Parse a VLESS header from *first_chunk* and open a raw TCP connection to the
    target address/port declared in it.  Returns (reader, writer, address, port)."""
    command, address, port, payload = await parse_vless_header(first_chunk)
    reader, writer = await asyncio.wait_for(
        asyncio.open_connection(address, port), timeout=TCP_CONNECT_TIMEOUT
    )
    _tune_socket(writer)
    if payload:
        writer.write(payload)
        await writer.drain()
    return reader, writer, address, port


async def _check_link(uuid: str):
    """Verify that the link identified by *uuid* is still active and authorised.

    Raises HTTPException(403) if the link is missing, disabled, or has exceeded
    its quota.
    """
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not is_link_allowed(link):
        raise HTTPException(status_code=403, detail="not authorized")


async def _validate_link_alive(uuid: str, session_id: str) -> bool:
    """Periodic lightweight re-check: returns False if the link was disabled since
    the session started.  Does NOT raise — the caller decides how to act."""
    try:
        async with LINKS_LOCK:
            link = LINKS.get(uuid)
        return is_link_allowed(link)
    except Exception:
        return False


async def _get_or_create_session(uuid: str, mode: str, session_id: str, ip: str = "نامشخص", config_password: str = "") -> dict:
    """Session بر اساس session_id که خودِ کلاینت در URL فرستاده، lazily ساخته می‌شه.

    If a session with the given *session_id* already exists its ``last_seen``
    timestamp is refreshed and it is returned.  Otherwise a brand-new session
    dict is created, registered in the global ``xhttp_sessions`` map, and a
    corresponding entry is added to the shared ``connections`` dict.
    """
    async with XHTTP_LOCK:
        sess = xhttp_sessions.get(session_id)
        if sess is not None:
            sess["last_seen"] = time.time()
            return sess

        async with LINKS_LOCK:
            link = LINKS.get(uuid)

        # Config password check
        link_pw = (link or {}).get("config_password", "")
        if link_pw and config_password != link_pw:
            logger.warning(f"XHTTP[{mode}] rejected uuid={uuid[:8]} ip={ip} (config password)")
            raise HTTPException(status_code=403, detail="config password required")

        # Geo-restriction check
        allowed_countries = (link or {}).get("allowed_countries", [])
        if allowed_countries:
            geo = await geo_ip_lookup(ip)
            country = geo.get("country", "")
            if country and country not in allowed_countries:
                logger.warning(f"XHTTP[{mode}] rejected uuid={uuid[:8]} ip={ip} country={country} (geo blocked)")
                raise HTTPException(status_code=403, detail="geo blocked")

        if not is_ip_allowed(link, uuid, ip):
            logger.warning(f"🚫 XHTTP[{mode}] rejected uuid={uuid[:8]} ip={ip} (ip limit reached)")
            raise HTTPException(status_code=403, detail="ip limit reached")

        conn_id = secrets.token_urlsafe(6)
        connections[conn_id] = {
            "uuid": uuid,
            "ip": ip,
            "connected_at": datetime.now().isoformat(),
            "bytes": 0,
            "transport": f"xhttp-{mode}",
        }
        sess = {
            "uuid": uuid, "mode": mode, "writer": None,
            "downlink_task": None, "uplink_task": None,
            "down_q": asyncio.Queue(maxsize=DOWNLINK_QUEUE_MAX),
            "last_seen": time.time(),
            "conn_id": conn_id, "tcp_open": False, "closed": False,
            "tearing_down": False,          # fix #11: guard against double-teardown
            "seq_buf": {}, "next_seq": 0,
            "gate": None,  # لازی ساخته می‌شه: _QuotaGate تطبیقی مخصوص stream-up
            "flow": None,  # لازی ساخته می‌شه: _AdaptiveFlow مخصوص stream-up
            "bytes_up": 0,  # fix #10: session-level upload byte counter
            "bytes_down": 0,  # fix #10: session-level download byte counter
            "last_tcp_data": time.time(),  # fix #8: timestamp of last TCP data received
            "_tcp_open_lock": asyncio.Lock(),  # fix #2: serialise TCP open for packet-up
        }
        xhttp_sessions[session_id] = sess
        logger.info(f"new XHTTP[{mode}] session [{session_id[:8]}] uuid={uuid[:8]} ip={ip}")
        return sess


async def _mark_real_mode(session_id: str, sess: dict, real_mode: str):
    """وقتی سشن با مود 'auto' ساخته شده، اولین درخواست POST واقعی مشخص می‌کنه
    که کلاینت در عمل packet-up انتخاب کرده یا stream-up؛ همون‌جا برچسب سشن و
    اتصال نمایشی رو به‌روز می‌کنیم تا در بخش «اتصالات» درست دیده بشه."""
    if sess.get("mode") == real_mode:
        return
    sess["mode"] = real_mode
    conn = connections.get(sess.get("conn_id"))
    if conn:
        conn["transport"] = f"xhttp-{real_mode}"


async def _teardown(session_id: str):
    """Gracefully tear down a session: cancel tasks, close TCP, drain queue, and
    remove from global maps.  Safe to call multiple times — a ``tearing_down``
    flag prevents double-teardown races."""
    async with XHTTP_LOCK:
        sess = xhttp_sessions.pop(session_id, None)
    if not sess:
        return
    if sess.get("tearing_down"):
        return  # fix #11: already being torn down — skip
    sess["tearing_down"] = True
    sess["closed"] = True
    for t in ("uplink_task", "downlink_task"):
        task = sess.get(t)
        if task:
            task.cancel()
            try:
                await task
            except (asyncio.CancelledError, Exception):
                pass
    writer = sess.get("writer")
    if writer:
        try:
            writer.close()
            await writer.wait_closed()
        except Exception:
            pass
    connections.pop(sess.get("conn_id"), None)
    dq = sess.get("down_q")
    if dq:
        try:
            dq.put_nowait(None)
        except Exception:
            pass
    logger.info(
        f"closed XHTTP[{sess.get('mode')}] [{session_id[:8]}] "
        f"bytes_up={sess.get('bytes_up', 0)} bytes_down={sess.get('bytes_down', 0)} "
        f"total={len(xhttp_sessions)}"
    )


async def _reaper():
    """Background task that periodically evicts idle sessions.

    Runs every ``REAPER_INTERVAL`` seconds and cleans up:
      - Sessions with no TCP connection that have been idle > SESSION_IDLE_TIMEOUT.
      - Sessions whose TCP connection has been idle > TCP_IDLE_TIMEOUT (no data
        received) — the remote end likely disconnected.
    Exceptions from individual teardowns are caught so one failure cannot kill
    the whole reaper loop.
    """
    while True:
        await asyncio.sleep(REAPER_INTERVAL)
        now = time.time()
        async with XHTTP_LOCK:
            stale_no_tcp = [
                sid for sid, s in xhttp_sessions.items()
                if now - s["last_seen"] > SESSION_IDLE_TIMEOUT and not s.get("tcp_open")
            ]
            stale_tcp_idle = [
                sid for sid, s in xhttp_sessions.items()
                if s.get("tcp_open") and now - s.get("last_tcp_data", 0) > TCP_IDLE_TIMEOUT
            ]
        all_stale = stale_no_tcp + stale_tcp_idle
        for sid in all_stale:
            try:
                await _teardown(sid)
            except Exception as exc:
                logger.error(f"⚠ reaper: _teardown failed for [{sid[:8]}]: {exc}")


_reaper_started = False


def ensure_reaper():
    global _reaper_started
    if not _reaper_started:
        asyncio.create_task(_reaper())
        _reaper_started = True


# ── downlink pump ──────────────────────────────────────────────────────────────

async def _pump_tcp_to_queue(session_id: str, uuid: str, reader: asyncio.StreamReader, down_q: asyncio.Queue):
    """Read data from the upstream TCP connection and enqueue it for the client's
    SSE / streaming-response downlink.

    Runs until the TCP connection closes or the session is torn down.  Applies
    the adaptive quota gate and speed throttling.  The link is re-validated
    every ``LINK_REVALIDATE_INTERVAL`` seconds so that a disabled link is
    noticed quickly.

    **Always** calls ``_teardown`` in its ``finally`` block so that the session
    is cleaned up even on unexpected errors (resource-leak prevention, fix #1).
    """
    first = True
    gate = _QuotaGate(uuid)  # دانلینک هم از همون گیت batched استفاده می‌کنه
    link_check_deadline = time.monotonic() + LINK_REVALIDATE_INTERVAL
    try:
        while True:
            data = await reader.read(XHTTP_BUF)
            if not data:
                break
            # fix #5: periodic link re-validation
            now_mono = time.monotonic()
            if now_mono >= link_check_deadline:
                link_check_deadline = now_mono + LINK_REVALIDATE_INTERVAL
                if not await _validate_link_alive(uuid, session_id):
                    logger.warning(f"⚠ XHTTP[{session_id[:8]}] link disabled during downlink, tearing down")
                    break
            if not await gate.add(len(data)):
                break
            await throttle(uuid, len(data))
            async with XHTTP_LOCK:
                sess = xhttp_sessions.get(session_id)
            if sess:
                # fix #6 & #10: atomic byte bump + session stats
                _bump_bytes(sess, len(data))
                sess["bytes_down"] = sess.get("bytes_down", 0) + len(data)
                # fix #8: record last TCP data timestamp
                sess["last_tcp_data"] = time.time()
            payload = (b"\x00\x00" + data) if first else data
            first = False
            await down_q.put(payload)
    except (asyncio.CancelledError, Exception):
        pass
    finally:
        await gate.flush()
        await _teardown(session_id)


async def _open_tcp_for_session(session_id: str, uuid: str, sess: dict, first_chunk: bytes):
    """تونل TCP رو از روی هدر VLESS باز می‌کنه و پمپ دانلینک رو راه می‌اندازه.

    Opens a raw TCP connection based on the VLESS header in *first_chunk*, stores
    the writer in the session, and spawns the ``_pump_tcp_to_queue`` background
    task for downstream data.
    """
    reader, writer, address, port = await _open_tcp_from_header(first_chunk)
    logger.info(f"connect XHTTP[{sess['mode']}] [{session_id[:8]}] -> {address}:{port}")
    sess["writer"] = writer
    sess["tcp_open"] = True
    sess["last_tcp_data"] = time.time()
    sess["downlink_task"] = asyncio.create_task(
        _pump_tcp_to_queue(session_id, uuid, reader, sess["down_q"])
    )
    asyncio.create_task(save_state())


def _downstream_gen(sess: dict):
    async def gen():
        try:
            while True:
                chunk = await sess["down_q"].get()
                if chunk is None:
                    break
                sess["last_seen"] = time.time()
                yield chunk
        finally:
            pass
    return gen()


# ══════════════════════════════ GET دانلینک (مشترک بین دو مد، بدون وابستگی به مود) ══════════════════════════════

@router.get("/xhttp-siz10/{uuid}/{session_id}")
async def xhttp_downlink(uuid: str, session_id: str, request: Request):
    """SSE-style downlink endpoint.  The client connects here to receive
    data relayed from the upstream TCP connection opened by a preceding
    packet-up or stream-up request.  Returns a ``StreamingResponse`` that
    blocks until the session is torn down or the upstream closes."""
    ensure_reaper()
    await _check_link(uuid)
    fp = request.query_params.get("fp", DEFAULT_FINGERPRINT)
    config_pw = request.query_params.get("password", "")
    sess = await _get_or_create_session(uuid, "auto", session_id, _req_client_ip(request), config_password=config_pw)
    if sess.get("closed"):
        raise HTTPException(status_code=404, detail="session closed")

    headers = _resp_headers(fp)
    return StreamingResponse(_downstream_gen(sess), headers=headers, media_type=headers["content-type"])


# ══════════════════════════════ PACKET-UP (آپلینک با seq) ══════════════════════════════

@router.post("/xhttp-siz10/{uuid}/{session_id}/{seq}")
async def packet_up_upload(uuid: str, session_id: str, seq: int, request: Request):
    """Packet-up upload endpoint.  Each POST carries one ordered packet
    identified by *seq*.  The first packet (seq=0) contains the VLESS header
    and triggers the TCP connection to the target.

    Packets arriving out of order are buffered in ``seq_buf`` (capped at
    ``MAX_SEQ_BUF``) and replayed in order once the missing packets arrive.
    The TCP open is serialised with an ``asyncio.Lock`` inside the session to
    prevent a race when two packets arrive simultaneously (fix #2).

    On any write failure the session is torn down and a 502 is returned.
    """
    ensure_reaper()
    config_pw = request.query_params.get("password", "")
    sess = await _get_or_create_session(uuid, "packet-up", session_id, _req_client_ip(request), config_password=config_pw)
    await _mark_real_mode(session_id, sess, "packet-up")
    if sess.get("closed"):
        raise HTTPException(status_code=404, detail="session closed")

    sess["last_seen"] = time.time()
    body = await request.body()
    if not body:
        return {"ok": True}

    if not await check_and_use(uuid, len(body)):
        await _teardown(session_id)
        raise HTTPException(status_code=403, detail="quota/disabled/unknown")
    await throttle(uuid, len(body))

    stats["total_requests"] += 1
    _bump_bytes(sess, len(body))
    sess["bytes_up"] = sess.get("bytes_up", 0) + len(body)

    try:
        if sess["writer"] is None:
            # fix #2: serialise TCP open with per-session lock
            async with sess["_tcp_open_lock"]:
                # Double-check after acquiring the lock (another packet may have opened TCP)
                if sess["writer"] is None:
                    # اولین پکتی که حاوی هدر VLESS است، می‌تونه seq=0 نباشه اگر پکت‌ها
                    # خارج از ترتیب برسن؛ بافر کوچیک برای سورت کردن seqهای زودرس.
                    if seq != 0:
                        sess["seq_buf"][seq] = body
                        _trim_seq_buf(sess)  # fix #3: memory limit
                        return {"ok": True, "buffered": True}
                    await _open_tcp_for_session(session_id, uuid, sess, body)
                    # هر پکت بافرشده‌ای که حالا نوبتش رسیده رو هم بفرست
                    nxt = 1
                    while nxt in sess["seq_buf"]:
                        pending = sess["seq_buf"].pop(nxt)
                        sess["writer"].write(pending)
                        nxt += 1
                    sess["next_seq"] = nxt
                    return {"ok": True, "connected": True}

        if seq == sess["next_seq"]:
            sess["writer"].write(body)
            sess["next_seq"] += 1
            while sess["next_seq"] in sess["seq_buf"]:
                pending = sess["seq_buf"].pop(sess["next_seq"])
                sess["writer"].write(pending)
                sess["next_seq"] += 1
        else:
            sess["seq_buf"][seq] = body
            _trim_seq_buf(sess)  # fix #3: memory limit

        if sess["writer"].transport.get_write_buffer_size() > PACKET_UP_HIGH_WATER:
            await sess["writer"].drain()
    except Exception as exc:
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        # fix #7: descriptive error with session_id prefix
        logger.error(f"⚠ packet-up [{session_id[:8]}] write failed: {exc}")
        await _teardown(session_id)
        raise HTTPException(status_code=502, detail=f"packet-up write failed [{session_id[:8]}]: {exc}")

    return {"ok": True}


# ══════════════════════════════ STREAM-UP (یک POST پیوسته) ══════════════════════════════
# موتور تطبیقی: _QuotaGate (batch کوتا بر اساس نرخ واقعی) + _AdaptiveFlow (AIMD روی
# high-water درین) + کش رفرنس‌ها داخل لوپ. هیچ داده‌ای بافر/coalesce نمی‌شه —
# هر بایت فوری write() می‌شه، فقط «کِی صبر کنیم برای drain» تطبیقیه.

@router.post("/xhttp-siz10/{uuid}/{session_id}")
async def stream_up_upload(uuid: str, session_id: str, request: Request):
    """Stream-up upload endpoint.  The client POSTs a single long-lived request
    body containing raw upstream data.  Data is forwarded to the target TCP
    connection chunk-by-chunk with adaptive flow control and quota gating.

    The link is periodically re-validated (every ``LINK_REVALIDATE_INTERVAL``
    seconds) so that a disabled link is noticed mid-stream.

    On quota exhaustion or any write error the session is torn down (resource-leak
    prevention, fix #1) and an appropriate HTTP error is returned.
    """
    ensure_reaper()
    config_pw = request.query_params.get("password", "")
    sess = await _get_or_create_session(uuid, "stream-up", session_id, _req_client_ip(request), config_password=config_pw)
    await _mark_real_mode(session_id, sess, "stream-up")
    if sess.get("closed"):
        raise HTTPException(status_code=404, detail="session closed")

    gate = sess.get("gate")
    if gate is None:
        gate = _QuotaGate(uuid)
        sess["gate"] = gate

    flow = sess.get("flow")
    if flow is None:
        flow = _AdaptiveFlow()
        sess["flow"] = flow

    conn = connections[sess["conn_id"]]   # یک بار لوک‌آپ، نه هر چانک
    writer = sess["writer"]               # ممکنه هنوز None باشه

    link_check_deadline = time.monotonic() + LINK_REVALIDATE_INTERVAL
    try:
        async for chunk in request.stream():
            if not chunk:
                continue
            sess["last_seen"] = time.time()

            # fix #5: periodic link re-validation
            now_mono = time.monotonic()
            if now_mono >= link_check_deadline:
                link_check_deadline = now_mono + LINK_REVALIDATE_INTERVAL
                if not await _validate_link_alive(uuid, session_id):
                    logger.warning(f"⚠ XHTTP[{session_id[:8]}] link disabled during stream-up, aborting")
                    raise HTTPException(status_code=403, detail="link disabled")

            if not await gate.add(len(chunk)):
                raise HTTPException(status_code=403, detail="quota/disabled/unknown")
            await throttle(uuid, len(chunk))

            stats["total_requests"] += 1
            _bump_bytes(sess, len(chunk))
            sess["bytes_up"] = sess.get("bytes_up", 0) + len(chunk)

            if writer is None:
                await _open_tcp_for_session(session_id, uuid, sess, chunk)
                writer = sess["writer"]
                continue

            writer.write(chunk)
            if flow.should_drain(writer.transport.get_write_buffer_size()):
                await flow.drain(writer)
    except HTTPException:
        # fix #1: always teardown on exception path (resource-leak prevention)
        await gate.flush()
        await _teardown(session_id)
        raise
    except Exception as exc:
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        # fix #7: descriptive error with session_id prefix
        logger.error(f"⚠ stream-up [{session_id[:8]}] error: {exc}")
        await gate.flush()
        await _teardown(session_id)
        raise HTTPException(status_code=502, detail=f"stream-up error [{session_id[:8]}]: {exc}")

    await gate.flush()
    return {"ok": True}
