"""
X4G — Main Application (FastAPI)
══════════════════════════════════
Central entry-point that wires together:
  • Link / subscription CRUD
  • Auth (cookie-based sessions)
  • VLESS relay (relay_vless.py)
  • XHTTP transport (xhttp_siz10.py)
  • Telegram bot management (telegram_bot.py)
  • HTTP proxy endpoint
  • Public subscription pages (pages.py)

Exports used by other modules (relay_vless, xhttp_siz10, telegram_bot, etc.):
  LINKS, LINKS_LOCK, stats, hourly_traffic, connections,
  error_logs, logger, is_link_allowed, is_ip_allowed,
  save_state, log_activity, now_ir
"""

# ── stdlib ────────────────────────────────────────────────────────────────────
import asyncio
import base64
import hashlib
import json
import logging
import os
import secrets
import time
from collections import defaultdict, deque
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional
from urllib.parse import quote
from zoneinfo import ZoneInfo

# ── third-party ───────────────────────────────────────────────────────────────
import aiofiles
import httpx
import uvicorn
from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    Request,
    WebSocket,
    WebSocketDisconnect,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import (
    HTMLResponse,
    JSONResponse,
    RedirectResponse,
    Response,
)
from pydantic import BaseModel

# ── local ─────────────────────────────────────────────────────────────────────
from speed_limit import reset_bucket  # noqa: F401 — used in update_link

# ── Logging ───────────────────────────────────────────────────────────────────
# NOTE: All logs are in-memory only (error_logs, activity_logs).  If you need
# durable / searchable logs, enable the optional file-based rotation below.
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger: logging.Logger = logging.getLogger("X4G")

# Optional file-based log rotation (only if DATA_DIR is writable)
_log_data_dir = Path(os.environ.get("DATA_DIR", "/data"))
if _log_data_dir.is_dir() and os.access(_log_data_dir, os.W_OK):
    try:
        from logging.handlers import RotatingFileHandler

        _file_handler = RotatingFileHandler(
            _log_data_dir / "x4g.log",
            maxBytes=10 * 1024 * 1024,  # 10 MB
            backupCount=5,
        )
        _file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
        logger.addHandler(_file_handler)
    except Exception:
        pass  # silently fall back to stdout-only logging

# ── Timezone & constants ──────────────────────────────────────────────────────
IRAN_TZ: ZoneInfo = ZoneInfo("Asia/Tehran")

# ── Persistence ───────────────────────────────────────────────────────────────
DATA_DIR: Path = Path(os.environ.get("DATA_DIR", "/data"))
DATA_FILE: Path = DATA_DIR / "x4g_state.json"
SECRET_FILE: Path = DATA_DIR / "x4g_secret.key"
SAVE_LOCK: asyncio.Lock = asyncio.Lock()


def _load_or_create_secret() -> str:
    """Load a stable secret from disk / env. Persists across restarts so that
    password hashes remain valid even after Railway container restarts."""
    env_secret: str | None = os.environ.get("SECRET_KEY")
    if env_secret:
        return env_secret
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if SECRET_FILE.exists():
            existing: str = SECRET_FILE.read_text(encoding="utf-8").strip()
            if existing:
                return existing
        new_secret: str = secrets.token_urlsafe(32)
        SECRET_FILE.write_text(new_secret, encoding="utf-8")
        return new_secret
    except Exception as e:
        logger.warning(
            f"Could not persist SECRET_KEY, sessions/password may reset on restart: {e}"
        )
        return secrets.token_urlsafe(32)


CONFIG: dict[str, Any] = {
    "port": int(os.environ.get("PORT", 8000)),
    "secret": _load_or_create_secret(),
    "host": os.environ.get("RAILWAY_PUBLIC_DOMAIN", "localhost"),
}


# ── FastAPI app & CORS ───────────────────────────────────────────────────────
app: FastAPI = FastAPI(title="X4G", docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Request-ID middleware ─────────────────────────────────────────────────────
# Adds a unique ``X-Request-ID`` header to every response so that multi-hop
# requests can be traced end-to-end.
@app.middleware("http")
async def _request_id_middleware(request: Request, call_next):  # type: ignore[no-untyped-def]
    request_id: str = request.headers.get("x-request-id") or secrets.token_hex(16)
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response


# ── In-memory state ───────────────────────────────────────────────────────────
# NOTE: connections is modified by relay_vless.py and xhttp_siz10.py too.
# Because asyncio is single-threaded, bare dict mutations (assign / del) are
# already safe.  The _conn_lock is provided for compound operations that need
# atomicity across multiple steps (e.g. read-modify-write).
_conn_lock: asyncio.Lock = asyncio.Lock()

connections: dict[str, dict[str, Any]] = {}

stats: dict[str, Any] = {
    "total_bytes": 0,
    "total_requests": 0,
    "total_errors": 0,
    "start_time": time.time(),
}

# NOTE: All error / activity logs live in memory only and are lost on restart.
# See the RotatingFileHandler setup above if you need file-backed persistence.
error_logs: deque[dict[str, Any]] = deque(maxlen=50)
activity_logs: deque[dict[str, Any]] = deque(maxlen=200)
hourly_traffic: dict[str, int] = defaultdict(int)

http_client: httpx.AsyncClient | None = None

LINKS: dict[str, dict[str, Any]] = {}
LINKS_LOCK: asyncio.Lock = asyncio.Lock()
SUBS: dict[str, dict[str, Any]] = {}
SUBS_LOCK: asyncio.Lock = asyncio.Lock()

# ── Protocol / fingerprint defaults ───────────────────────────────────────────
PROTOCOLS: tuple[str, ...] = ("vless-ws", "xhttp")
DEFAULT_PROTOCOL: str = "vless-ws"

FINGERPRINTS: tuple[str, ...] = (
    "chrome", "firefox", "safari", "ios", "android",
    "edge", "360", "qq", "random", "randomized",
)
DEFAULT_FINGERPRINT: str = "chrome"

DEFAULT_ALPN_BY_PROTOCOL: dict[str, str] = {
    "vless-ws": "http/1.1",
    "xhttp": "h2,http/1.1",
}
DEFAULT_PORT: int = 443
MIN_PORT: int = 1
MAX_PORT: int = 65535

DEFAULT_SPEED_LIMIT: int = 0  # 0 = unlimited; stored as bytes/sec


# ── Debounced save ────────────────────────────────────────────────────────────
# Prevents multiple concurrent saves and batches rapid changes (create link,
# update link, …) into a single disk write per second.
_save_task: asyncio.Task[None] | None = None


async def _do_save() -> None:
    """Actual write-to-disk inside SAVE_LOCK."""
    async with SAVE_LOCK:
        try:
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            data: dict[str, Any] = {
                "links": dict(LINKS),
                "subs": dict(SUBS),
                "password_hash": AUTH["password_hash"],
                "saved_at": datetime.now().isoformat(),
            }
            tmp: Path = DATA_FILE.with_suffix(".tmp")
            async with aiofiles.open(tmp, "w", encoding="utf-8") as f:
                await f.write(json.dumps(data, ensure_ascii=False, indent=2))
            tmp.replace(DATA_FILE)
        except Exception as e:
            logger.warning(f"Could not save state: {e}")


def _schedule_save() -> None:
    """Schedule a debounced save.  Each call within 1 s cancels the previous
    pending save and resets the timer, ensuring at most one disk write per
    second even under bursty mutations."""
    global _save_task
    if _save_task is not None and not _save_task.done():
        _save_task.cancel()
    _save_task = asyncio.create_task(_debounced_save())


async def _debounced_save() -> None:
    try:
        await asyncio.sleep(1.0)
        await _do_save()
    except asyncio.CancelledError:
        pass


# Keep save_state() as a public name so other modules can call it directly.
async def save_state() -> None:
    """Force an immediate save (used on shutdown, password change, etc.)."""
    await _do_save()


# ── Hourly-traffic cleanup ───────────────────────────────────────────────────
async def _cleanup_hourly_traffic() -> None:
    """Remove hourly_traffic entries older than 24 hours to prevent unbounded
    memory growth.  Called by a startup background task every 5 minutes."""
    while True:
        try:
            await asyncio.sleep(300)  # 5 minutes
            cutoff: str = (now_ir() - timedelta(hours=24)).strftime("%H:00")
            # We compare HH:00 strings; entries whose key < cutoff within the
            # same day-window are stale.  Simpler: just keep only keys in the
            # last 24 windowed hours.
            now_h = now_ir()
            stale_keys: list[str] = []
            for hour_str in list(hourly_traffic.keys()):
                try:
                    h, m = hour_str.split(":")
                    entry_time = now_h.replace(
                        hour=int(h), minute=int(m), second=0, microsecond=0
                    )
                    if (now_h - entry_time).total_seconds() > 86400:
                        stale_keys.append(hour_str)
                except (ValueError, AttributeError):
                    stale_keys.append(hour_str)
            for k in stale_keys:
                hourly_traffic.pop(k, None)
        except asyncio.CancelledError:
            break
        except Exception:
            pass  # best-effort; don't crash the loop


# ── Activity logging ─────────────────────────────────────────────────────────
def log_activity(kind: str, message: str, level: str = "info") -> None:
    """Record an event in the in-memory activity log (create/delete/edit, login, etc.)."""
    activity_logs.append(
        {
            "kind": kind,
            "level": level,
            "message": message,
            "time": datetime.now().isoformat(),
        }
    )


# ── Auth ──────────────────────────────────────────────────────────────────────
SESSION_COOKIE: str = "x4g_session"

# 7 days — long enough for comfortable re-use on personal devices, short enough
# that a leaked cookie has a bounded window of abuse.
SESSION_TTL: int = 60 * 60 * 24 * 7  # 604 800 s


def hash_password(pw: str) -> str:
    """Hash a password with SHA-256 using the server secret as pepper.

    TODO: Migrate to bcrypt / argon2id for proper salting & memory-hardness.
    SHA-256 + pepper is *adequate* for this project's threat model but is not
    best practice for password hashing in general.
    """
    return hashlib.sha256(f"{CONFIG['secret']}{pw}{CONFIG['secret']}".encode()).hexdigest()


AUTH: dict[str, str] = {
    "password_hash": hash_password(os.environ.get("ADMIN_PASSWORD", "X4GKING"))
}
SESSIONS: dict[str, float] = {}
SESSIONS_LOCK: asyncio.Lock = asyncio.Lock()


async def create_session() -> str:
    token: str = secrets.token_urlsafe(32)
    async with SESSIONS_LOCK:
        SESSIONS[token] = time.time() + SESSION_TTL
    return token


async def is_valid_session(token: str | None) -> bool:
    if not token:
        return False
    async with SESSIONS_LOCK:
        exp: float | None = SESSIONS.get(token)
        if exp is None:
            return False
        if exp < time.time():
            SESSIONS.pop(token, None)
            return False
        return True


async def destroy_session(token: str | None) -> None:
    if not token:
        return
    async with SESSIONS_LOCK:
        SESSIONS.pop(token, None)


async def require_auth(request: Request) -> str:
    token: str | None = request.cookies.get(SESSION_COOKIE)
    if not await is_valid_session(token):
        raise HTTPException(status_code=401, detail="unauthorized")
    return token  # type: ignore[return-value]


# ── Lifespan (replaces deprecated on_event) ──────────────────────────────────
from contextlib import asynccontextmanager  # noqa: E402 — stdlib, needed here for lifespan
from typing import AsyncGenerator  # noqa: E402


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    """Startup / shutdown lifecycle managed via ASGI lifespan."""
    global http_client

    # ── Startup ───────────────────────────────────────────────────────────
    limits = httpx.Limits(max_connections=500, max_keepalive_connections=100)
    timeout = httpx.Timeout(30.0, connect=10.0)
    http_client = httpx.AsyncClient(
        limits=limits, timeout=timeout, follow_redirects=True,
    )
    await load_state()
    await _tg_start_bot()
    log_activity("system", "سرور راه‌اندازی شد", "ok")
    logger.info(f"X4G v9.8 started on port {CONFIG['port']}")

    # Start background hourly-traffic cleanup task
    _cleanup_task = asyncio.create_task(_cleanup_hourly_traffic())

    try:
        yield  # ← app is running
    finally:
        # ── Shutdown ──────────────────────────────────────────────────────
        _cleanup_task.cancel()
        try:
            await _cleanup_task
        except asyncio.CancelledError:
            pass
        await save_state()
        await _tg_stop_bot()
        if http_client:
            await http_client.aclose()


app.router.lifespan_context = lifespan  # type: ignore[attr-defined]

# ── Lazy imports deferred to after app definition ─────────────────────────────
# telegram_bot must be imported here because it references `app` and other names
# defined above.
from telegram_bot import start_bot as _tg_start_bot, stop_bot as _tg_stop_bot  # noqa: E402


# ── Helpers ───────────────────────────────────────────────────────────────────


def get_host(request: Request | None = None) -> str:
    """Resolve the public domain from the incoming request (Host / X-Forwarded-Host).
    Falls back to RAILWAY_PUBLIC_DOMAIN env var or CONFIG cache."""
    if request is not None:
        h: str | None = (
            request.headers.get("x-forwarded-host") or request.headers.get("host")
        )
        if h:
            h = h.split(":")[0]
            CONFIG["host"] = h
            return h
    return os.environ.get("RAILWAY_PUBLIC_DOMAIN", CONFIG["host"])


def generate_uuid() -> str:
    h: str = secrets.token_hex(16)
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"


def now_ir() -> datetime:
    return datetime.now(IRAN_TZ)


def generate_vless_link(
    uuid: str,
    host: str,
    remark: str = "X4G",
    protocol: str = DEFAULT_PROTOCOL,
    fingerprint: str | None = None,
    alpn: str | None = None,
    port: int | None = None,
) -> str:
    """Build a VLESS share-link for the chosen protocol (WS classic or XHTTP modes)."""
    fp: str = (fingerprint or DEFAULT_FINGERPRINT).strip() or DEFAULT_FINGERPRINT
    if fp not in FINGERPRINTS:
        fp = DEFAULT_FINGERPRINT
    alpn_val: str = (
        (alpn or "").strip() or DEFAULT_ALPN_BY_PROTOCOL.get(protocol, "http/1.1")
    )
    port_val: int = port or DEFAULT_PORT
    if not (MIN_PORT <= port_val <= MAX_PORT):
        port_val = DEFAULT_PORT

    if protocol == "vless-ws":
        path = f"/ws/{uuid}"
        params: dict[str, str] = {
            "encryption": "none",
            "security": "tls",
            "type": "ws",
            "host": host,
            "path": path,
            "sni": host,
            "fp": fp,
            "alpn": alpn_val,
        }
    else:
        path = f"/xhttp-siz10/{uuid}"
        params = {
            "encryption": "none",
            "security": "tls",
            "type": "xhttp",
            "mode": "auto",
            "host": host,
            "path": path,
            "sni": host,
            "fp": fp,
            "alpn": alpn_val,
        }
    query: str = "&".join(f"{k}={quote(str(v))}" for k, v in params.items())
    return f"vless://{uuid}@{host}:{port_val}?{query}#{quote(remark)}"


def vless_link_for_link(link: dict[str, Any], uid: str, host: str) -> str:
    """Call generate_vless_link with the link's stored fingerprint / alpn / port."""
    proto: str = link.get("protocol", DEFAULT_PROTOCOL)
    return generate_vless_link(
        uid,
        host,
        remark=f"X4G-{link.get('label', '')}",
        protocol=proto,
        fingerprint=link.get("fingerprint"),
        alpn=link.get("alpn"),
        port=link.get("port"),
    )


def uptime() -> str:
    secs: int = int(time.time() - stats["start_time"])
    h, m, s = secs // 3600, (secs % 3600) // 60, secs % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def parse_size_to_bytes(value: float, unit: str) -> int:
    unit = unit.upper()
    if unit == "GB":
        return int(value * 1024**3)
    if unit == "MB":
        return int(value * 1024**2)
    if unit == "KB":
        return int(value * 1024)
    return int(value)


def parse_speed_to_bytes(value: float, unit: str) -> int:
    """Convert a speed value+unit to bytes/sec.
    Supported units: MBIT (megabits/sec, most common), KB, MB."""
    if value <= 0:
        return 0
    unit = (unit or "MBIT").upper()
    if unit == "MBIT":
        return int(value * 1024 * 1024 / 8)
    if unit == "KB":
        return int(value * 1024)
    if unit == "MB":
        return int(value * 1024 * 1024)
    return int(value)


def is_link_expired(link: dict[str, Any]) -> bool:
    exp: str | None = link.get("expires_at")
    if not exp:
        return False
    try:
        return datetime.now() > datetime.fromisoformat(exp)
    except Exception:
        return False


def is_link_allowed(link: dict[str, Any] | None) -> bool:
    if link is None:
        return False
    if not link.get("active", True):
        return False
    if is_link_expired(link):
        return False
    lb: int = link.get("limit_bytes", 0)
    if lb > 0 and link.get("used_bytes", 0) >= lb:
        return False
    return True


def fmt_bytes(b: int) -> str:
    if b < 1024:
        return f"{b} B"
    if b < 1024**2:
        return f"{b / 1024:.1f} KB"
    if b < 1024**3:
        return f"{b / 1024**2:.2f} MB"
    return f"{b / 1024**3:.2f} GB"


def unique_ips_for_uuid(uuid: str) -> set[str]:
    """Return the set of unique IPs currently connected to a given UUID."""
    return {
        c.get("ip")
        for c in connections.values()
        if c.get("uuid") == uuid and c.get("ip")
    }


def is_ip_allowed(link: dict[str, Any] | None, uuid: str, ip: str) -> bool:
    """Enforce per-link concurrent IP limits.  ip_limit=0 means unlimited.
    An IP that already has an active session is always allowed (multi-tab
    on the same device won't break)."""
    if link is None:
        return False
    limit: int = int(link.get("ip_limit", 0) or 0)
    if limit <= 0:
        return True
    ips: set[str] = unique_ips_for_uuid(uuid)
    if ip in ips:
        return True
    return len(ips) < limit


# NOTE on client_ip(): this canonical implementation lives in main.py.
# relay_vless.py and xhttp_siz10.py each define their own copy.
# TODO: consolidate — those modules should import client_ip from main to
# avoid divergence.  (Cannot change those modules in this file.)
def client_ip(request: Request) -> str:
    """Extract the real client IP, accounting for proxy headers
    (X-Forwarded-For, X-Real-IP) used by Railway / Cloudflare."""
    fwd: str | None = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip: str | None = request.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "نامشخص"


# ── Basic endpoints ───────────────────────────────────────────────────────────


@app.get("/")
async def root() -> dict[str, str]:
    return {"service": "X4G", "version": "9.5", "status": "active", "channel": "https://t.me/X4GHUB"}


@app.get("/health")
async def health() -> dict[str, Any]:
    return {"status": "ok", "connections": len(connections), "uptime": uptime()}


# ── Subscription (single link) ───────────────────────────────────────────────


@app.get("/sub/{uuid}")
async def subscription_single(uuid: str, request: Request) -> Response:
    try:
        async with LINKS_LOCK:
            link: dict[str, Any] | None = LINKS.get(uuid)
        if not link or not is_link_allowed(link):
            raise HTTPException(status_code=404, detail="not found or inactive")
        host: str = get_host(request)
        vless: str = vless_link_for_link(link, uuid, host)
        content: str = base64.b64encode(vless.encode()).decode()
        return Response(
            content=content,
            media_type="text/plain",
            headers={
                "profile-title": quote(link["label"]),
                "support-url": "https://t.me/X4GHUB",
            },
        )
    except HTTPException:
        raise
    except Exception as exc:
        logger.error(f"subscription_single error: {exc}")
        raise HTTPException(status_code=500, detail="internal error")


@app.get("/sub-all")
async def subscription_all(request: Request, _: str = Depends(require_auth)) -> Response:
    try:
        host: str = get_host(request)
        async with LINKS_LOCK:
            lines: list[str] = [
                vless_link_for_link(d, uid, host)
                for uid, d in LINKS.items()
                if is_link_allowed(d)
            ]
        content: str = base64.b64encode("\n".join(lines).encode()).decode()
        return Response(content=content, media_type="text/plain")
    except HTTPException:
        raise
    except Exception as exc:
        logger.error(f"subscription_all error: {exc}")
        raise HTTPException(status_code=500, detail="internal error")


# ── Auth endpoints ────────────────────────────────────────────────────────────


@app.post("/api/login")
async def api_login(request: Request) -> JSONResponse:
    try:
        body: dict[str, Any] = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="invalid JSON body")
    ip: str = client_ip(request)
    if hash_password(str(body.get("password", ""))) != AUTH["password_hash"]:
        log_activity("auth", f"تلاش ورود ناموفق از {ip}", "err")
        raise HTTPException(status_code=401, detail="رمز عبور اشتباه است")
    token: str = await create_session()
    log_activity("auth", f"ورود موفق به پنل از {ip}", "ok")
    resp = JSONResponse({"ok": True})
    resp.set_cookie(
        SESSION_COOKIE,
        token,
        max_age=SESSION_TTL,
        httponly=True,
        samesite="lax",
        path="/",
    )
    return resp


@app.post("/api/logout")
async def api_logout(request: Request) -> JSONResponse:
    await destroy_session(request.cookies.get(SESSION_COOKIE))
    resp = JSONResponse({"ok": True})
    resp.delete_cookie(SESSION_COOKIE, path="/")
    return resp


@app.get("/api/me")
async def api_me(request: Request) -> dict[str, bool]:
    return {"authenticated": await is_valid_session(request.cookies.get(SESSION_COOKIE))}


@app.post("/api/change-password")
async def api_change_password(
    request: Request, token: str = Depends(require_auth)
) -> dict[str, bool]:
    try:
        body: dict[str, Any] = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="invalid JSON body")
    if hash_password(str(body.get("current_password", ""))) != AUTH["password_hash"]:
        raise HTTPException(status_code=400, detail="رمز فعلی اشتباه است")
    new_pw: str = str(body.get("new_password", ""))
    if len(new_pw) < 4:
        raise HTTPException(status_code=400, detail="رمز جدید باید حداقل ۴ کاراکتر باشد")
    AUTH["password_hash"] = hash_password(new_pw)
    async with SESSIONS_LOCK:
        SESSIONS.clear()
        SESSIONS[token] = time.time() + SESSION_TTL
    _schedule_save()
    log_activity("auth", "رمز عبور پنل تغییر کرد", "ok")
    return {"ok": True}


# ── Stats ─────────────────────────────────────────────────────────────────────


@app.get("/stats")
async def get_stats(_: str = Depends(require_auth)) -> dict[str, Any]:
    async with LINKS_LOCK:
        snap: dict[str, dict[str, Any]] = dict(LINKS)
    return {
        "active_connections": len(connections),
        "total_traffic_mb": round(stats["total_bytes"] / (1024**2), 2),
        "total_requests": stats["total_requests"],
        "total_errors": stats["total_errors"],
        "uptime": uptime(),
        "timestamp": datetime.now().isoformat(),
        "hourly": dict(hourly_traffic),
        "recent_errors": list(error_logs)[-10:],
        "links_count": len(snap),
        "active_links": sum(1 for l in snap.values() if is_link_allowed(l)),
        "expired_links": sum(1 for l in snap.values() if is_link_expired(l)),
    }


# ── Activity Logs ─────────────────────────────────────────────────────────────


@app.get("/api/activity")
async def get_activity(_: str = Depends(require_auth)) -> dict[str, list]:
    return {"logs": list(activity_logs)[-150:]}


# ── Live connections (grouped by config) ──────────────────────────────────────


@app.get("/api/connections")
async def get_connections(_: str = Depends(require_auth)) -> dict[str, Any]:
    """Return live connections grouped by UUID with per-IP breakdown."""
    async with LINKS_LOCK:
        snap: dict[str, dict[str, Any]] = dict(LINKS)

    # Pre-compute unique IPs per UUID in a single pass over connections.
    unique_ips_by_uuid: dict[str, set[str]] = defaultdict(set)
    for c in connections.values():
        uid = c.get("uuid", "")
        ip = c.get("ip")
        if uid and ip:
            unique_ips_by_uuid[uid].add(ip)

    by_uuid: dict[str, dict[str, Any]] = {}
    for conn_id, c in connections.items():
        uid: str = c.get("uuid", "نامشخص")
        ip: str = c.get("ip", "نامشخص")
        link: dict[str, Any] | None = snap.get(uid)
        label: str = link.get("label") if link else "کانفیگ حذف‌شده"
        proto: str = (link.get("protocol", DEFAULT_PROTOCOL) if link else "?")

        cfg: dict[str, Any] | None = by_uuid.get(uid)
        if cfg is None:
            cfg = {
                "uuid": uid,
                "label": label,
                "protocol": proto,
                "sessions": 0,
                "bytes": 0,
                "ips": {},
                "first_connected_at": c.get("connected_at"),
                "last_connected_at": c.get("connected_at"),
            }
            by_uuid[uid] = cfg
        cfg["sessions"] += 1
        cfg["bytes"] += c.get("bytes", 0)

        ip_entry: dict[str, Any] | None = cfg["ips"].get(ip)
        if ip_entry is None:
            ip_entry = {
                "ip": ip,
                "sessions": 0,
                "bytes": 0,
                "transports": set(),
                "first_connected_at": c.get("connected_at"),
                "last_connected_at": c.get("connected_at"),
            }
            cfg["ips"][ip] = ip_entry
        ip_entry["sessions"] += 1
        ip_entry["bytes"] += c.get("bytes", 0)
        ip_entry["transports"].add(c.get("transport", "vless-ws"))

        ca: str | None = c.get("connected_at")
        for entry in (cfg, ip_entry):
            if ca:
                if not entry["first_connected_at"] or ca < entry["first_connected_at"]:
                    entry["first_connected_at"] = ca
                if not entry["last_connected_at"] or ca > entry["last_connected_at"]:
                    entry["last_connected_at"] = ca

    configs: list[dict[str, Any]] = []
    for uid, cfg in by_uuid.items():
        ip_list: list[dict[str, Any]] = []
        for ip, e in cfg["ips"].items():
            ip_list.append(
                {
                    "ip": ip,
                    "sessions": e["sessions"],
                    "bytes": e["bytes"],
                    "bytes_fmt": fmt_bytes(e["bytes"]),
                    "transports": sorted(e["transports"]),
                    "connected_at": e["first_connected_at"],
                    "last_connected_at": e["last_connected_at"],
                }
            )
        ip_list.sort(key=lambda x: x.get("last_connected_at") or "", reverse=True)
        configs.append(
            {
                "uuid": uid,
                "label": cfg["label"],
                "protocol": cfg["protocol"],
                "ip_count": len(ip_list),
                "sessions": cfg["sessions"],
                "bytes": cfg["bytes"],
                "bytes_fmt": fmt_bytes(cfg["bytes"]),
                "connected_at": cfg["first_connected_at"],
                "last_connected_at": cfg["last_connected_at"],
                "connections": ip_list,
            }
        )
    configs.sort(key=lambda x: x.get("last_connected_at") or "", reverse=True)

    return {
        "configs": configs,
        "count": len(configs),
        "raw_count": len(connections),
    }


# ── Shared link CRUD helpers (used by API and Telegram bot) ───────────────────


async def make_link(
    label: str = "لینک جدید",
    limit_bytes: int = 0,
    expires_at: str | None = None,
    note: str = "",
    protocol: str = DEFAULT_PROTOCOL,
    fingerprint: str = DEFAULT_FINGERPRINT,
    alpn: str = "",
    port: int = DEFAULT_PORT,
    ip_limit: int = 0,
    speed_limit_bytes: int = 0,
    password: str | None = None,
) -> tuple[str, dict[str, Any]]:
    if protocol not in PROTOCOLS:
        protocol = DEFAULT_PROTOCOL
    fingerprint = (fingerprint or DEFAULT_FINGERPRINT).strip().lower()
    if fingerprint not in FINGERPRINTS:
        fingerprint = DEFAULT_FINGERPRINT
    if not (MIN_PORT <= port <= MAX_PORT):
        port = DEFAULT_PORT
    uid: str = generate_uuid()
    link_dict: dict[str, Any] = {
        "label": (label or "لینک جدید").strip()[:60] or "لینک جدید",
        "limit_bytes": max(0, limit_bytes),
        "used_bytes": 0,
        "created_at": datetime.now().isoformat(),
        "active": True,
        "expires_at": expires_at,
        "note": (note or "").strip()[:200],
        "is_default": False,
        "protocol": protocol,
        "fingerprint": fingerprint,
        "alpn": (alpn or "").strip()[:100],
        "port": port,
        "ip_limit": max(0, ip_limit),
        "speed_limit_bytes": max(0, speed_limit_bytes),
        "password": password or None,
    }
    async with LINKS_LOCK:
        LINKS[uid] = link_dict
    _schedule_save()
    log_activity("link", f"کانفیگ «{link_dict['label']}» ساخته شد", "ok")
    return uid, link_dict


async def remove_link(uid: str) -> str | None:
    async with LINKS_LOCK:
        if uid not in LINKS:
            return None
        label: str = LINKS[uid].get("label", uid)
        del LINKS[uid]
    _schedule_save()
    log_activity("link", f"کانفیگ «{label}» حذف شد", "err")
    return label


async def set_link_active(uid: str, active: bool) -> dict[str, Any] | None:
    async with LINKS_LOCK:
        if uid not in LINKS:
            return None
        LINKS[uid]["active"] = bool(active)
        label: str = LINKS[uid]["label"]
        result: dict[str, Any] = dict(LINKS[uid])
    log_activity(
        "link",
        f"کانفیگ «{label}» {'فعال' if active else 'غیرفعال'} شد",
        "ok" if active else "warn",
    )
    _schedule_save()
    return result


# ── Link Management ───────────────────────────────────────────────────────────


@app.post("/api/links")
async def create_link(request: Request, _: str = Depends(require_auth)) -> dict[str, Any]:
    try:
        body: dict[str, Any] = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="invalid JSON body")

    try:
        lv: float = float(body.get("limit_value") or 0)
    except (TypeError, ValueError):
        lv = 0.0
    lu: str = body.get("limit_unit") or "GB"
    limit_bytes: int = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)

    exp_days: int = int(body.get("expires_days") or 0)
    if exp_days < 0:
        raise HTTPException(status_code=400, detail="expires_days must be >= 0")
    expires_at: str | None = (
        (datetime.now() + timedelta(days=exp_days)).isoformat() if exp_days > 0 else None
    )

    try:
        port: int = int(body.get("port") or DEFAULT_PORT)
    except (TypeError, ValueError):
        port = DEFAULT_PORT
    try:
        ip_limit: int = int(body.get("ip_limit") or 0)
    except (TypeError, ValueError):
        ip_limit = 0

    try:
        sv: float = float(body.get("speed_limit_value") or 0)
    except (TypeError, ValueError):
        sv = 0.0
    su: str = body.get("speed_limit_unit") or "MBIT"
    speed_limit_bytes: int = 0 if sv <= 0 else parse_speed_to_bytes(sv, su)

    uid, link = await make_link(
        label=body.get("label") or "لینک جدید",
        limit_bytes=limit_bytes,
        expires_at=expires_at,
        note=body.get("note") or "",
        protocol=body.get("protocol") or DEFAULT_PROTOCOL,
        fingerprint=body.get("fingerprint") or DEFAULT_FINGERPRINT,
        alpn=body.get("alpn") or "",
        port=port,
        ip_limit=ip_limit,
        speed_limit_bytes=speed_limit_bytes,
        password=body.get("password"),
    )

    host: str = get_host(request)
    return {
        "uuid": uid,
        **link,
        "expired": False,
        "vless_link": vless_link_for_link(link, uid, host),
        "sub_url": f"https://{host}/p/{uid}",
        "raw_sub_url": f"https://{host}/sub/{uid}",
    }


@app.get("/api/links")
async def list_links(request: Request, _: str = Depends(require_auth)) -> dict[str, Any]:
    host: str = get_host(request)
    async with LINKS_LOCK:
        snap: dict[str, dict[str, Any]] = dict(LINKS)
    result: list[dict[str, Any]] = []
    for uid, d in snap.items():
        proto: str = d.get("protocol", DEFAULT_PROTOCOL)
        result.append(
            {
                "uuid": uid,
                **d,
                "protocol": proto,
                "expired": is_link_expired(d),
                "vless_link": vless_link_for_link(d, uid, host),
                "sub_url": f"https://{host}/p/{uid}",
                "raw_sub_url": f"https://{host}/sub/{uid}",
                "connected_ips": len(unique_ips_for_uuid(uid)),
            }
        )
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"links": result}


@app.patch("/api/links/{uid}")
async def update_link(
    uid: str, request: Request, _: str = Depends(require_auth)
) -> dict[str, bool]:
    try:
        body: dict[str, Any] = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="invalid JSON body")

    async with LINKS_LOCK:
        if uid not in LINKS:
            raise HTTPException(status_code=404, detail="link not found")
        link: dict[str, Any] = LINKS[uid]
        label: str = link.get("label", "")

        if "active" in body:
            link["active"] = bool(body["active"])
            log_activity(
                "link",
                f"کانفیگ «{label}» {'فعال' if link['active'] else 'غیرفعال'} شد",
                "ok" if link["active"] else "warn",
            )
        if "label" in body:
            link["label"] = str(body["label"])[:60]
        if "note" in body:
            link["note"] = str(body["note"])[:200]
        if "reset_usage" in body and body["reset_usage"]:
            link["used_bytes"] = 0
            log_activity("link", f"مصرف کانفیگ «{label}» ریست شد", "info")
        if "limit_value" in body:
            try:
                lv = float(body.get("limit_value") or 0)
            except (TypeError, ValueError):
                lv = 0.0
            lu = body.get("limit_unit") or "GB"
            link["limit_bytes"] = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
        if "expires_days" in body:
            ed = int(body["expires_days"] or 0)
            if ed < 0:
                raise HTTPException(status_code=400, detail="expires_days must be >= 0")
            link["expires_at"] = (
                (datetime.now() + timedelta(days=ed)).isoformat() if ed > 0 else None
            )
        if "fingerprint" in body:
            fp = str(body.get("fingerprint") or DEFAULT_FINGERPRINT).strip().lower()
            link["fingerprint"] = fp if fp in FINGERPRINTS else DEFAULT_FINGERPRINT
        if "alpn" in body:
            link["alpn"] = str(body.get("alpn") or "").strip()[:100]
        if "port" in body:
            try:
                p = int(body.get("port") or DEFAULT_PORT)
            except (TypeError, ValueError):
                p = DEFAULT_PORT
            link["port"] = p if (MIN_PORT <= p <= MAX_PORT) else DEFAULT_PORT
        if "ip_limit" in body:
            try:
                il = int(body.get("ip_limit") or 0)
            except (TypeError, ValueError):
                il = 0
            link["ip_limit"] = max(0, il)
        if "speed_limit_value" in body:
            try:
                sv = float(body.get("speed_limit_value") or 0)
            except (TypeError, ValueError):
                sv = 0.0
            su = body.get("speed_limit_unit") or "MBIT"
            link["speed_limit_bytes"] = 0 if sv <= 0 else parse_speed_to_bytes(sv, su)
            reset_bucket(uid)

    _schedule_save()
    return {"ok": True}


@app.delete("/api/links/{uid}")
async def delete_link(uid: str, _: str = Depends(require_auth)) -> dict[str, Any]:
    label = await remove_link(uid)
    if label is None:
        raise HTTPException(status_code=404, detail="link not found")
    return {"ok": True, "deleted": uid}


# ── HTTP Proxy ────────────────────────────────────────────────────────────────

_HOP_HEADERS: frozenset[str] = frozenset(
    {
        "connection",
        "keep-alive",
        "proxy-authenticate",
        "proxy-authorization",
        "te",
        "trailers",
        "transfer-encoding",
        "upgrade",
        "content-encoding",
        "content-length",
    }
)

# ── Rate limiter for the proxy endpoint ───────────────────────────────────────
# Simple in-memory sliding-window limiter: max 100 requests per minute per IP.
_PROXY_RATE_LIMIT: int = 100
_proxy_rate_windows: dict[str, deque[float]] = defaultdict(deque)


def _proxy_is_rate_limited(ip: str) -> bool:
    """Return True if the IP has exceeded the proxy rate limit."""
    now = time.time()
    window: deque[float] = _proxy_rate_windows[ip]
    # Evict entries older than 60 s
    while window and window[0] < now - 60:
        window.popleft()
    if len(window) >= _PROXY_RATE_LIMIT:
        return True
    window.append(now)
    return False


@app.api_route(
    "/proxy/{target_url:path}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
)
async def http_proxy(target_url: str, request: Request) -> Response:
    ip: str = client_ip(request)
    if _proxy_is_rate_limited(ip):
        raise HTTPException(status_code=429, detail="rate limit exceeded")
    if not target_url.startswith("http"):
        target_url = "https://" + target_url
    try:
        body: bytes = await request.body()
        headers: dict[str, str] = {
            k: v
            for k, v in request.headers.items()
            if k.lower() not in _HOP_HEADERS and k.lower() != "host"
        }
        resp = await http_client.request(
            method=request.method, url=target_url, headers=headers, content=body
        )
        stats["total_bytes"] += len(resp.content)
        stats["total_requests"] += 1
        hourly_traffic[now_ir().strftime("%H:00")] += len(resp.content)
        return Response(
            content=resp.content,
            status_code=resp.status_code,
            headers={
                k: v
                for k, v in resp.headers.items()
                if k.lower() not in _HOP_HEADERS
            },
        )
    except HTTPException:
        raise
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append(
            {"error": str(exc), "url": target_url, "time": datetime.now().isoformat()}
        )
        raise HTTPException(status_code=502, detail=f"Proxy error: {exc}")


# ── Public subscription page & data ──────────────────────────────────────────


@app.get("/p/{uuid_key}", response_class=HTMLResponse)
async def public_sub_page(uuid_key: str, request: Request) -> HTMLResponse:
    try:
        from pages import get_public_page_html

        async with LINKS_LOCK:
            exists: bool = uuid_key in LINKS
        if not exists:
            return HTMLResponse(
                "<h2 style='font-family:sans-serif;padding:40px'>کانفیگ پیدا نشد</h2>",
                status_code=404,
            )
        return HTMLResponse(content=get_public_page_html(uuid_key))
    except Exception as exc:
        logger.error(f"public_sub_page error: {exc}")
        return HTMLResponse(
            "<h2 style='font-family:sans-serif;padding:40px'>خطای داخلی</h2>",
            status_code=500,
        )


@app.get("/api/public/sub/{uuid_key}")
async def public_sub_data(uuid_key: str, request: Request) -> dict[str, Any]:
    async with LINKS_LOCK:
        link: dict[str, Any] | None = LINKS.get(uuid_key)
    if not link:
        raise HTTPException(status_code=404, detail="not found")

    # Optional password check: if the link has a password set, require it.
    link_password: str | None = link.get("password")
    if link_password:
        provided: str | None = request.query_params.get("password")
        if provided != link_password:
            raise HTTPException(status_code=403, detail="password required")

    host: str = get_host(request)
    allowed: bool = is_link_allowed(link)
    conn_count: int = sum(
        1 for c in connections.values() if c.get("uuid") == uuid_key
    )
    proto: str = link.get("protocol", DEFAULT_PROTOCOL)
    link_out: dict[str, Any] = {
        "uuid": uuid_key,
        "label": link["label"],
        "active": allowed,
        "protocol": proto,
        "used_bytes": link.get("used_bytes", 0),
        "used_fmt": fmt_bytes(link.get("used_bytes", 0)),
        "limit_bytes": link.get("limit_bytes", 0),
        "limit_fmt": (
            "∞" if link.get("limit_bytes", 0) == 0 else fmt_bytes(link["limit_bytes"])
        ),
        "expires_at": link.get("expires_at"),
        "vless_link": vless_link_for_link(link, uuid_key, host),
        "sub_url": f"https://{host}/sub/{uuid_key}",
        "connections": conn_count,
        "ip_limit": link.get("ip_limit", 0),
        "speed_limit_bytes": link.get("speed_limit_bytes", 0),
    }

    return {
        "locked": False,
        "name": link["label"],
        "desc": link.get("note", ""),
        "sub_url": f"https://{host}/p/{uuid_key}",
        "active_connections": conn_count,
        "total_used_fmt": fmt_bytes(link.get("used_bytes", 0)),
        "links": [link_out],
    }


# ── HTML Pages (login + dashboard) ───────────────────────────────────────────
from pages import LOGIN_HTML, DASHBOARD_HTML  # noqa: E402


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request) -> HTMLResponse | RedirectResponse:
    if await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        return RedirectResponse(url="/dashboard")
    return HTMLResponse(content=LOGIN_HTML)


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request) -> HTMLResponse | RedirectResponse:
    if not await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        return RedirectResponse(url="/login")
    return HTMLResponse(content=DASHBOARD_HTML)


@app.get("/test-ws", response_class=HTMLResponse)
async def test_ws_redirect() -> HTMLResponse:
    return HTMLResponse(content="<script>location.href='/dashboard'</script>")


# ── VLESS Relay ───────────────────────────────────────────────────────────────
from relay_vless import (  # noqa: E402
    RELAY_BUF,
    parse_vless_header,
    check_and_use,
    relay_ws_to_tcp,
    relay_tcp_to_ws,
    websocket_tunnel,
)

app.add_api_websocket_route("/ws/{uuid}", websocket_tunnel)

# ── XHTTP Transport ──────────────────────────────────────────────────────────
from xhttp_siz10 import router as xhttp_router  # noqa: E402

app.include_router(xhttp_router)


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=CONFIG["port"], log_level="info", workers=1)
