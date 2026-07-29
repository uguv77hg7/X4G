import asyncio
import json
import os
import hashlib
import secrets
import time
import aiofiles
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from urllib.parse import quote
from collections import deque, defaultdict
from pathlib import Path

import pyotp
from fastapi import FastAPI, Request, HTTPException, WebSocket, WebSocketDisconnect, Depends
from fastapi.responses import Response, HTMLResponse, JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import httpx
import logging
import subprocess
import struct

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("X4G")

IRAN_TZ = ZoneInfo("Asia/Tehran")

app = FastAPI(title="X4G", docs_url=None, redoc_url=None)

# ── Persistence ───────────────────────────────────────────────────────────────
DATA_DIR = Path(os.environ.get("DATA_DIR", "/data"))
DATA_FILE = DATA_DIR / "x4g_state.json"
SECRET_FILE = DATA_DIR / "x4g_secret.key"
BACKUPS_DIR = DATA_DIR / "backups"
SAVE_LOCK = asyncio.Lock()

def _load_or_create_secret() -> str:
    """SECRET_KEY را روی دیسک ذخیره و ثابت نگه می‌دارد.
    قبلاً وقتی متغیر محیطی SECRET_KEY تنظیم نشده بود، با هر ری‌استارت سرویس
    (که روی Railway هر چند ساعت یک‌بار اتفاق می‌افتد) یک مقدار تصادفی جدید
    ساخته می‌شد. چون هش پسورد بر پایه‌ی همین secret ساخته می‌شود، تغییر آن
    باعث می‌شد پسورد درست هم دیگر قبول نشود. حالا secret یک‌بار ساخته و در
    فایل ذخیره می‌شود و در ری‌استارت‌های بعدی همان مقدار خوانده می‌شود."""
    env_secret = os.environ.get("SECRET_KEY")
    if env_secret:
        return env_secret
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if SECRET_FILE.exists():
            existing = SECRET_FILE.read_text(encoding="utf-8").strip()
            if existing:
                return existing
        new_secret = secrets.token_urlsafe(32)
        SECRET_FILE.write_text(new_secret, encoding="utf-8")
        return new_secret
    except Exception as e:
        logger.warning(f"Could not persist SECRET_KEY, sessions/password may reset on restart: {e}")
        return secrets.token_urlsafe(32)

CONFIG = {
    "port": int(os.environ.get("PORT", 8000)),
    "secret": _load_or_create_secret(),
    "host": os.environ.get("RAILWAY_PUBLIC_DOMAIN", "localhost"),
    "xray_binary": os.environ.get("XRAY_BINARY", "/usr/local/bin/xray"),
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def load_state():
    global LINKS, AUTH, SUBS, restart_count, uptime_history
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if DATA_FILE.exists():
            async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
                raw = await f.read()
            data = json.loads(raw)
            LINKS.update(data.get("links", {}))
            SUBS.update(data.get("subs", {}))
            if "password_hash" in data:
                AUTH["password_hash"] = data["password_hash"]
            if "totp_secret" in data:
                AUTH["totp_secret"] = data["totp_secret"]
            if "totp_enabled" in data:
                AUTH["totp_enabled"] = data["totp_enabled"]
            restart_count = data.get("restart_count", 0)
            uptime_history_data = data.get("uptime_history", [])
            uptime_history.clear()
            for entry in uptime_history_data[-30:]:
                uptime_history.append(entry)
            # لینک پیش‌فرضی که در نسخه‌های قبلی به‌صورت خودکار ساخته می‌شد دیگر
            # پشتیبانی نمی‌شود؛ اگر از قبل روی دیسک ذخیره شده باشد، حذفش می‌کنیم.
            legacy_default_uids = [uid for uid, l in LINKS.items() if l.get("is_default")]
            for uid in legacy_default_uids:
                LINKS.pop(uid, None)
            if legacy_default_uids:
                asyncio.create_task(save_state())
            logger.info(f"State loaded: {len(LINKS)} links, {len(SUBS)} subs")
    except Exception as e:
        logger.warning(f"Could not load state: {e}")

async def save_state():
    async with SAVE_LOCK:
        try:
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            data = {
                "links": dict(LINKS),
                "subs": dict(SUBS),
                "password_hash": AUTH["password_hash"],
                "saved_at": datetime.now().isoformat(),
                "restart_count": restart_count,
                "uptime_history": list(uptime_history),
            }
            tmp = DATA_FILE.with_suffix(".tmp")
            async with aiofiles.open(tmp, "w", encoding="utf-8") as f:
                await f.write(json.dumps(data, ensure_ascii=False, indent=2))
            tmp.replace(DATA_FILE)
        except Exception as e:
            logger.warning(f"Could not save state: {e}")

# ── In-memory state ───────────────────────────────────────────────────────────
connections: dict = {}
stats = {
    "total_bytes": 0,
    "total_requests": 0,
    "total_errors": 0,
    "start_time": time.time(),
}
error_logs: deque = deque(maxlen=50)
activity_logs: deque = deque(maxlen=200)
hourly_traffic: dict = defaultdict(int)
# ── Analytics state ───────────────────────────────────────────────────────────
daily_traffic: dict = defaultdict(int)       # "YYYY-MM-DD" -> bytes
weekly_traffic: dict = defaultdict(int)      # "YYYY-Wxx" -> bytes
geoip_cache: dict = {}                       # ip -> {data, cached_at}
GEOIP_CACHE_TTL = 86400                      # 24 hours
restart_count: int = 0
uptime_history: deque = deque(maxlen=30)     # last 30 restart entries
http_client: httpx.AsyncClient | None = None
LINKS: dict = {}
LINKS_LOCK = asyncio.Lock()
SUBS: dict = {}
SUBS_LOCK = asyncio.Lock()

# ── Speed Test State ────────────────────────────────────────────────────────
speedtest_results: dict = {
    "speed_mbps": 0.0,
    "latency_ms": 0.0,
    "last_test": None,
    "running": False,
}

# ── Xray Update State ──────────────────────────────────────────────────────
xray_state: dict = {
    "current_version": None,
    "latest_version": None,
    "update_available": False,
    "last_check": None,
    "updating": False,
    "error": None,
}

# پروتکل‌های پشتیبانی‌شده برای هر کانفیگ
PROTOCOLS = ("vless-ws", "xhttp", "hysteria2")
DEFAULT_PROTOCOL = "vless-ws"

# Fingerprint (uTLS) های قابل انتخاب برای هر کانفیگ
FINGERPRINTS = ("chrome", "firefox", "safari", "ios", "android", "edge", "360", "qq", "random", "randomized")
DEFAULT_FINGERPRINT = "chrome"

# پیش‌فرض ALPN بر اساس نوع ترابرد (اگر کاربر مقدار دستی نده)
DEFAULT_ALPN_BY_PROTOCOL = {
    "vless-ws": "http/1.1",
    "xhttp": "h2,http/1.1",
    "hysteria2": "",
}
DEFAULT_PORT = 443
MIN_PORT, MAX_PORT = 1, 65535

# Config Templates — predefined link configurations
CONFIG_TEMPLATES = {
    "unlimited": {
        "name": "نامحدود",
        "icon": "ti-infinity",
        "color": "green",
        "desc": "بدون محدودیت ترافیک، بدون انقضا",
        "limit_bytes": 0,
        "expires_days": 0,
        "speed_limit_bytes": 0,
    },
    "limited-10gb": {
        "name": "۱۰ گیگابایت",
        "icon": "ti-database",
        "color": "cyan",
        "desc": "۱۰ گیگابایت ترافیک، ۳۰ روز اعتبار",
        "limit_bytes": 10 * 1024 ** 3,
        "expires_days": 30,
        "speed_limit_bytes": 0,
    },
    "trial": {
        "name": "آزمایشی",
        "icon": "ti-flask",
        "color": "amber",
        "desc": "۱ گیگابایت ترافیک، ۷ روز اعتبار",
        "limit_bytes": 1 * 1024 ** 3,
        "expires_days": 7,
        "speed_limit_bytes": 0,
    },
    "premium": {
        "name": "پریمیوم",
        "icon": "ti-crown",
        "color": "purple",
        "desc": "۱۰۰ گیگابایت، ۹۰ روز، سرعت ۵۰ مگابیت",
        "limit_bytes": 100 * 1024 ** 3,
        "expires_days": 90,
        "speed_limit_bytes": 50 * 1024 * 1024 / 8,
    },
    "basic": {
        "name": "پایه",
        "icon": "ti-package",
        "color": "blue",
        "desc": "۵ گیگابایت، ۳۰ روز، سرعت ۱۰ مگابیت",
        "limit_bytes": 5 * 1024 ** 3,
        "expires_days": 30,
        "speed_limit_bytes": 10 * 1024 * 1024 / 8,
    },
}

# محدودیت سرعت (0 = نامحدود). واحد ذخیره‌سازی داخلی همیشه بایت‌بر‌ثانیه است.
DEFAULT_SPEED_LIMIT = 0

def log_activity(kind: str, message: str, level: str = "info"):
    """ثبت یک رخداد در لاگ فعالیت‌ها (ساخت/حذف/ویرایش کانفیگ، ورود، و...)."""
    activity_logs.append({
        "kind": kind,
        "level": level,
        "message": message,
        "time": datetime.now().isoformat(),
    })

# ── Auth ──────────────────────────────────────────────────────────────────────
SESSION_COOKIE = "x4g_session"
SESSION_TTL = 60 * 60 * 24 * 365

def hash_password(pw: str) -> str:
    return hashlib.sha256(f"{pw}{CONFIG['secret']}".encode()).hexdigest()

AUTH = {"password_hash": hash_password(os.environ.get("ADMIN_PASSWORD", "X4GKING"))}
SESSIONS: dict = {}
SESSIONS_LOCK = asyncio.Lock()

# Brute Force Protection
LOGIN_ATTEMPTS: dict = {}
BRUTE_FORCE_MAX_ATTEMPTS = 5
BRUTE_FORCE_BLOCK_SECONDS = 15 * 60  # 15 minutes

# GeoIP Lookup
async def geo_ip_lookup(ip: str) -> dict:
    if ip in geoip_cache and time.time() - geoip_cache[ip].get("cached_at", 0) < GEOIP_CACHE_TTL:
        return geoip_cache[ip]
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            r = await client.get(f"http://ip-api.com/json/{ip}?fields=status,country,countryCode")
            if r.status_code == 200:
                data = r.json()
                if data.get("status") == "success":
                    result = {"country": data.get("countryCode", ""), "country_name": data.get("country", ""), "cached_at": time.time()}
                    geoip_cache[ip] = result
                    return result
    except Exception:
        pass
    return {}

def check_login_brute_force(ip: str) -> dict | None:
    entry = LOGIN_ATTEMPTS.get(ip)
    if not entry:
        return None
    if entry.get("blocked_until", 0) > time.time():
        remaining = int(entry["blocked_until"] - time.time())
        return {"blocked": True, "remaining": remaining}
    if entry.get("blocked_until", 0) > 0 and entry["blocked_until"] <= time.time():
        LOGIN_ATTEMPTS[ip] = {"count": 0, "last_attempt": time.time(), "blocked_until": 0}
    return None

def record_failed_login(ip: str) -> dict:
    entry = LOGIN_ATTEMPTS.get(ip, {"count": 0, "last_attempt": 0, "blocked_until": 0})
    entry["count"] = entry.get("count", 0) + 1
    entry["last_attempt"] = time.time()
    if entry["count"] >= BRUTE_FORCE_MAX_ATTEMPTS:
        entry["blocked_until"] = time.time() + BRUTE_FORCE_BLOCK_SECONDS
        LOGIN_ATTEMPTS[ip] = entry
        return {"blocked": True, "remaining": BRUTE_FORCE_BLOCK_SECONDS, "count": entry["count"]}
    LOGIN_ATTEMPTS[ip] = entry
    return {"blocked": False, "remaining": 0, "count": entry["count"]}

def reset_login_attempts(ip: str):
    if ip in LOGIN_ATTEMPTS:
        LOGIN_ATTEMPTS[ip]["count"] = 0
        LOGIN_ATTEMPTS[ip]["blocked_until"] = 0

async def create_session() -> str:
    token = secrets.token_urlsafe(32)
    async with SESSIONS_LOCK:
        SESSIONS[token] = time.time() + SESSION_TTL
    return token

async def is_valid_session(token: str | None) -> bool:
    if not token:
        return False
    async with SESSIONS_LOCK:
        exp = SESSIONS.get(token)
        if exp is None:
            return False
        if exp < time.time():
            SESSIONS.pop(token, None)
            return False
        return True

async def destroy_session(token: str | None):
    if not token:
        return
    async with SESSIONS_LOCK:
        SESSIONS.pop(token, None)

async def require_auth(request: Request):
    token = request.cookies.get(SESSION_COOKIE)
    if not await is_valid_session(token):
        raise HTTPException(status_code=401, detail="unauthorized")
    return token

# ── Startup / Shutdown ────────────────────────────────────────────────────────
@app.on_event("startup")
async def startup():
    global http_client, restart_count
    limits = httpx.Limits(max_connections=500, max_keepalive_connections=100)
    timeout = httpx.Timeout(30.0, connect=10.0)
    http_client = httpx.AsyncClient(
        limits=limits, timeout=timeout, follow_redirects=True,
    )
    await load_state()
    restart_count += 1
    stats["start_time"] = time.time()
    uptime_history.append({
        "time": datetime.now().isoformat(),
        "restart_number": restart_count,
    })
    await _tg_start_bot()
    asyncio.create_task(_auto_backup_loop())
    log_activity("system", "سرور راه‌اندازی شد", "ok")
    logger.info(f"X4G v9.8 started on port {CONFIG['port']} (restart #{restart_count})")

@app.on_event("shutdown")
async def shutdown():
    await save_state()
    await _tg_stop_bot()
    if http_client:
        await http_client.aclose()

# ── Helpers ───────────────────────────────────────────────────────────────────
def get_host(request: Request | None = None) -> str:
    """آدرس دامنه رو ترجیحاً از خودِ درخواست HTTP می‌گیره (هدر Host/X-Forwarded-Host)
    چون این همیشه دقیقاً همون دامنه‌ایه که کاربر واقعاً بهش وصل شده. متغیر محیطی
    RAILWAY_PUBLIC_DOMAIN فقط به‌عنوان fallback استفاده می‌شه، چون گاهی موقع بالا اومدن
    کانتینر هنوز مقداردهی نشده و باعث می‌شد لینک‌ها گاهی با "localhost" ساخته بشن."""
    if request is not None:
        h = request.headers.get("x-forwarded-host") or request.headers.get("host")
        if h:
            h = h.split(":")[0]
            CONFIG["host"] = h  # کش آخرین دامنه‌ی واقعی دیده‌شده، برای جاهایی که request نداریم (مثل ربات تلگرام)
            return h
    return os.environ.get("RAILWAY_PUBLIC_DOMAIN", CONFIG["host"])

def generate_uuid() -> str:
    h = secrets.token_hex(16)
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
    """می‌سازد VLESS share-link متناسب با پروتکل انتخاب‌شده (WS کلاسیک یا یکی از مدهای XHTTP).
    fingerprint / alpn / port در صورت ندادن، از پیش‌فرض‌های خود پروتکل استفاده می‌شوند."""
    fp = (fingerprint or DEFAULT_FINGERPRINT).strip() or DEFAULT_FINGERPRINT
    if fp not in FINGERPRINTS:
        fp = DEFAULT_FINGERPRINT
    alpn_val = (alpn or "").strip() or DEFAULT_ALPN_BY_PROTOCOL.get(protocol, "http/1.1")
    port_val = port or DEFAULT_PORT
    if not (MIN_PORT <= port_val <= MAX_PORT):
        port_val = DEFAULT_PORT

    if protocol == "vless-ws":
        path = f"/ws/{uuid}"
        params = {
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
        # xhttp — مود auto: خود کلاینت بر اساس نوع اتصال (H2/REALITY یا نه)
        # بین packet-up و stream-up انتخاب می‌کنه؛ مسیر سرور به مود بستگی نداره.
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
    query = "&".join(f"{k}={quote(str(v))}" for k, v in params.items())
    return f"vless://{uuid}@{host}:{port_val}?{query}#{quote(remark)}"

def vless_link_for_link(link: dict, uid: str, host: str) -> str:
    """generate_vless_link رو با تنظیمات دستی همون کانفیگ (fingerprint/alpn/port) صدا می‌زنه."""
    proto = link.get("protocol", DEFAULT_PROTOCOL)
    return generate_vless_link(
        uid, host,
        remark=f"X4G-{link.get('label','')}",
        protocol=proto,
        fingerprint=link.get("fingerprint"),
        alpn=link.get("alpn"),
        port=link.get("port"),
    )

def uptime() -> str:
    secs = int(time.time() - stats["start_time"])
    h, m, s = secs // 3600, (secs % 3600) // 60, secs % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def parse_size_to_bytes(value: float, unit: str) -> int:
    unit = unit.upper()
    if unit == "GB": return int(value * 1024 ** 3)
    if unit == "MB": return int(value * 1024 ** 2)
    if unit == "KB": return int(value * 1024)
    return int(value)

def parse_speed_to_bytes(value: float, unit: str) -> int:
    """محدودیت سرعت رو به بایت‌بر‌ثانیه تبدیل می‌کنه.
    واحدهای پشتیبانی‌شده: MBIT (مگابیت‌بر‌ثانیه، رایج‌ترین)، KB (کیلوبایت‌بر‌ثانیه)، MB (مگابایت‌بر‌ثانیه)."""
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

def is_link_expired(link: dict) -> bool:
    exp = link.get("expires_at")
    if not exp:
        return False
    try:
        return datetime.now() > datetime.fromisoformat(exp)
    except Exception:
        return False

def is_link_allowed(link: dict | None) -> bool:
    if link is None:
        return False
    if not link.get("active", True):
        return False
    if is_link_expired(link):
        return False
    lb = link.get("limit_bytes", 0)
    if lb > 0 and link.get("used_bytes", 0) >= lb:
        return False
    return True

def fmt_bytes(b: int) -> str:
    if b < 1024: return f"{b} B"
    if b < 1024**2: return f"{b/1024:.1f} KB"
    if b < 1024**3: return f"{b/1024**2:.2f} MB"
    return f"{b/1024**3:.2f} GB"

def unique_ips_for_uuid(uuid: str) -> set:
    """آی‌پی‌های یکتای همین لحظه متصل به یک UUID خاص (بر اساس dict اتصالات زنده)."""
    return {c.get("ip") for c in connections.values() if c.get("uuid") == uuid and c.get("ip")}

def is_ip_allowed(link: dict | None, uuid: str, ip: str) -> bool:
    """محدودیت تعداد آی‌پی/کاربر هم‌زمان برای هر کانفیگ. ip_limit=0 یعنی نامحدود.
    اگر همین آی‌پی از قبل روی این کانفیگ سشن باز داشته باشه، همیشه مجازه (برای چند اتصال
    هم‌زمان از یک دستگاه/مرورگر مشکلی پیش نمیاد)."""
    if link is None:
        return False
    limit = int(link.get("ip_limit", 0) or 0)
    if limit <= 0:
        return True
    ips = unique_ips_for_uuid(uuid)
    if ip in ips:
        return True
    return len(ips) < limit

def client_ip(request: Request) -> str:
    """آی‌پی واقعی کلاینت رو با احتساب هدرهای پراکسی (Railway/Cloudflare) برمی‌گردونه."""
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = request.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "نامشخص"

# ── Default link ──────────────────────────────────────────────────────────────

# ── Basic endpoints ───────────────────────────────────────────────────────────
@app.get("/")
async def root():
    return {"service": "X4G", "version": "9.5", "status": "active", "channel": "https://t.me/X4GHUB"}

@app.get("/health")
async def health():
    return {"status": "ok", "connections": len(connections), "uptime": uptime()}

# ── Subscription (single link) ────────────────────────────────────────────────
@app.get("/sub/{uuid}")
async def subscription_single(uuid: str, request: Request):
    import base64
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not link or not is_link_allowed(link):
        raise HTTPException(status_code=404, detail="not found or inactive")
    host = get_host(request)
    vless = vless_link_for_link(link, uuid, host)
    content = base64.b64encode(vless.encode()).decode()
    return Response(content=content, media_type="text/plain",
                    headers={"profile-title": quote(link["label"]), "support-url": "https://t.me/X4GHUB"})

@app.get("/sub-all")
async def subscription_all(request: Request, _=Depends(require_auth)):
    import base64
    host = get_host(request)
    async with LINKS_LOCK:
        lines = [
            vless_link_for_link(d, uid, host)
            for uid, d in LINKS.items()
            if is_link_allowed(d)
        ]
    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain")

# ── Auth endpoints ────────────────────────────────────────────────────────────
@app.post("/api/login")
async def api_login(request: Request):
    body = await request.json()
    ip = client_ip(request)

    # Brute force check
    bf = check_login_brute_force(ip)
    if bf and bf.get("blocked"):
        log_activity("auth", f"مسدود شدن ورود از {ip}", "err")
        raise HTTPException(status_code=429, detail=f"حساب شما موقتاً مسدود شد. {bf['remaining']} ثانیه باقی‌مانده")

    if hash_password(str(body.get("password", ""))) != AUTH["password_hash"]:
        info = record_failed_login(ip)
        log_activity("auth", f"تلاش ورود ناموفق از {ip} ({info['count']}/{BRUTE_FORCE_MAX_ATTEMPTS})", "err")
        if info.get("blocked"):
            raise HTTPException(status_code=429, detail=f"حساب شما موقتاً مسدود شد. {info['remaining']} ثانیه باقی‌مانده")
        raise HTTPException(status_code=401, detail="رمز عبور اشتباه است")

    # 2FA check
    if AUTH.get("totp_enabled") and AUTH.get("totp_secret"):
        totp_code = str(body.get("totp_code", ""))
        if not totp_code:
            return JSONResponse({"need_totp": True, "message": "کد ۲ عاملی را وارد کنید"})
        totp = pyotp.TOTP(AUTH["totp_secret"])
        if not totp.verify(totp_code):
            log_activity("auth", f"تلاش ورود 2FA ناموفق از {ip}", "err")
            raise HTTPException(status_code=401, detail="کد ۲ عاملی اشتباه است")

    reset_login_attempts(ip)
    token = await create_session()
    log_activity("auth", f"ورود موفق به پنل از {ip}", "ok")
    resp = JSONResponse({"ok": True})
    resp.set_cookie(SESSION_COOKIE, token, max_age=SESSION_TTL, httponly=True, samesite="lax", path="/")
    return resp

@app.post("/api/logout")
async def api_logout(request: Request):
    await destroy_session(request.cookies.get(SESSION_COOKIE))
    resp = JSONResponse({"ok": True})
    resp.delete_cookie(SESSION_COOKIE, path="/")
    return resp

@app.get("/api/me")
async def api_me(request: Request):
    return {"authenticated": await is_valid_session(request.cookies.get(SESSION_COOKIE))}

@app.post("/api/change-password")
async def api_change_password(request: Request, token=Depends(require_auth)):
    body = await request.json()
    if hash_password(str(body.get("current_password", ""))) != AUTH["password_hash"]:
        raise HTTPException(status_code=400, detail="رمز فعلی اشتباه است")
    new = str(body.get("new_password", ""))
    if len(new) < 4:
        raise HTTPException(status_code=400, detail="رمز جدید باید حداقل ۴ کاراکتر باشد")
    AUTH["password_hash"] = hash_password(new)
    async with SESSIONS_LOCK:
        SESSIONS.clear()
        SESSIONS[token] = time.time() + SESSION_TTL
    await save_state()
    log_activity("auth", "رمز عبور پنل تغییر کرد", "ok")
    return {"ok": True}

# ── 2FA Endpoints ────────────────────────────────────────────────────────────
@app.post("/api/2fa/enable")
async def api_2fa_enable(_=Depends(require_auth)):
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    qr_url = totp.provisioning_uri(name="admin", issuer_name="X4G-Panel")
    AUTH["totp_secret"] = secret
    AUTH["totp_enabled"] = False  # Not enabled until verified
    await save_state()
    log_activity("auth", "2FA setup initiated", "info")
    return {"secret": secret, "qr_url": qr_url, "message": "Enter code in authenticator app, then verify"}

@app.post("/api/2fa/verify")
async def api_2fa_verify(request: Request, _=Depends(require_auth)):
    body = await request.json()
    code = str(body.get("code", ""))
    if not AUTH.get("totp_secret"):
        raise HTTPException(status_code=400, detail="Call /api/2fa/enable first")
    totp = pyotp.TOTP(AUTH["totp_secret"])
    if totp.verify(code):
        AUTH["totp_enabled"] = True
        await save_state()
        log_activity("auth", "2FA enabled", "ok")
        return {"ok": True, "message": "2FA enabled successfully"}
    raise HTTPException(status_code=401, detail="Invalid code")

@app.post("/api/2fa/disable")
async def api_2fa_disable(request: Request, _=Depends(require_auth)):
    body = await request.json()
    password = str(body.get("password", ""))
    if hash_password(password) != AUTH["password_hash"]:
        raise HTTPException(status_code=400, detail="Wrong password")
    AUTH["totp_enabled"] = False
    AUTH["totp_secret"] = ""
    await save_state()
    log_activity("auth", "2FA disabled", "warn")
    return {"ok": True, "message": "2FA disabled"}

@app.get("/api/2fa/status")
async def api_2fa_status(_=Depends(require_auth)):
    return {"enabled": AUTH.get("totp_enabled", False), "has_secret": bool(AUTH.get("totp_secret"))}

@app.get("/api/security/brute-force")
async def api_brute_force(_=Depends(require_auth)):
    now = time.time()
    blocked = []
    for ip, entry in list(LOGIN_ATTEMPTS.items()):
        if entry.get("blocked_until", 0) > now:
            remaining = int(entry["blocked_until"] - now)
            blocked.append({"ip": ip, "count": entry.get("count", 0), "remaining_seconds": remaining})
    return {"blocked_ips": blocked, "total_blocked": len(blocked)}

# ── Stats ─────────────────────────────────────────────────────────────────────
@app.get("/stats")
async def get_stats(_=Depends(require_auth)):
    async with LINKS_LOCK:
        snap = dict(LINKS)
    return {
        "active_connections": len(connections),
        "total_traffic_mb": round(stats["total_bytes"] / (1024 ** 2), 2),
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
async def get_activity(_=Depends(require_auth)):
    return {"logs": list(activity_logs)[-150:]}

# ── Live connections (با دسته‌بندی بر اساس کانفیگ) ────────────────────────────
@app.get("/api/connections")
async def get_connections(_=Depends(require_auth)):
    """
    خروجی این endpoint حالا بر اساس کانفیگ (uuid) گروه‌بندی شده: هر کانفیگ
    یک آیتم با تعداد آی‌پی/سشن و مجموع ترافیکشه، و داخل هرکدوم لیست
    آی‌پی‌های متصل به همون کانفیگ (با جمع بایت و تعداد سشن هر آی‌پی) هست.
    raw_count همچنان تعداد واقعی اتصالات باز (سشن‌های خام) را برمی‌گرداند.
    """
    async with LINKS_LOCK:
        snap = dict(LINKS)

    by_uuid: dict[str, dict] = {}
    for conn_id, c in connections.items():
        uid = c.get("uuid", "نامشخص")
        ip = c.get("ip", "نامشخص")
        link = snap.get(uid)
        label = link.get("label") if link else "کانفیگ حذف‌شده"
        proto = link.get("protocol", DEFAULT_PROTOCOL) if link else "?"

        cfg = by_uuid.get(uid)
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

        ip_entry = cfg["ips"].get(ip)
        if ip_entry is None:
            ip_entry = {
                "ip": ip, "sessions": 0, "bytes": 0, "transports": set(),
                "first_connected_at": c.get("connected_at"),
                "last_connected_at": c.get("connected_at"),
            }
            cfg["ips"][ip] = ip_entry
        ip_entry["sessions"] += 1
        ip_entry["bytes"] += c.get("bytes", 0)
        ip_entry["transports"].add(c.get("transport", "vless-ws"))

        ca = c.get("connected_at")
        for entry in (cfg, ip_entry):
            if ca:
                if not entry["first_connected_at"] or ca < entry["first_connected_at"]:
                    entry["first_connected_at"] = ca
                if not entry["last_connected_at"] or ca > entry["last_connected_at"]:
                    entry["last_connected_at"] = ca

    configs = []
    for uid, cfg in by_uuid.items():
        ip_list = []
        for ip, e in cfg["ips"].items():
            ip_list.append({
                "ip": ip,
                "sessions": e["sessions"],
                "bytes": e["bytes"],
                "bytes_fmt": fmt_bytes(e["bytes"]),
                "transports": sorted(e["transports"]),
                "connected_at": e["first_connected_at"],
                "last_connected_at": e["last_connected_at"],
            })
        ip_list.sort(key=lambda x: x.get("last_connected_at") or "", reverse=True)
        configs.append({
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
        })
    configs.sort(key=lambda x: x.get("last_connected_at") or "", reverse=True)

    return {
        "configs": configs,
        "count": len(configs),          # تعداد کانفیگ‌های دارای اتصال فعال
        "raw_count": len(connections),  # تعداد کل اتصالات باز (بدون گروه‌بندی)
    }

# ── Shared link create/delete helpers (استفاده مشترک API و ربات تلگرام) ───────
# ── Shared link create/delete helpers (استفاده مشترک API و ربات تلگرام) ───────
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
    config_password: str = "",
    allowed_countries: list = None,
) -> tuple[str, dict]:
    if protocol not in PROTOCOLS:
        protocol = DEFAULT_PROTOCOL
    fingerprint = (fingerprint or DEFAULT_FINGERPRINT).strip().lower()
    if fingerprint not in FINGERPRINTS:
        fingerprint = DEFAULT_FINGERPRINT
    if not (MIN_PORT <= port <= MAX_PORT):
        port = DEFAULT_PORT
    uid = generate_uuid()
    async with LINKS_LOCK:
        LINKS[uid] = {
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
            "config_password": (config_password or "").strip()[:100],
            "allowed_countries": allowed_countries if allowed_countries is not None else [],
        }
    asyncio.create_task(save_state())
    log_activity("link", f"کانفیگ «{LINKS[uid]['label']}» ساخته شد", "ok")
    return uid, LINKS[uid]

async def remove_link(uid: str) -> str | None:
    async with LINKS_LOCK:
        if uid not in LINKS:
            return None
        label = LINKS[uid].get("label", uid)
        del LINKS[uid]
    asyncio.create_task(save_state())
    log_activity("link", f"کانفیگ «{label}» حذف شد", "err")
    return label

async def set_link_active(uid: str, active: bool) -> dict | None:
    async with LINKS_LOCK:
        if uid not in LINKS:
            return None
        LINKS[uid]["active"] = bool(active)
        label = LINKS[uid]["label"]
    log_activity("link", f"کانفیگ «{label}» {'فعال' if active else 'غیرفعال'} شد", "ok" if active else "warn")
    asyncio.create_task(save_state())
    return LINKS[uid]

# ── Link Management ───────────────────────────────────────────────────────────
@app.post("/api/links")
async def create_link(request: Request, _=Depends(require_auth)):
    body = await request.json()
    lv = float(body.get("limit_value") or 0)
    lu = body.get("limit_unit") or "GB"
    limit_bytes = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
    exp_days = int(body.get("expires_days") or 0)
    expires_at = (datetime.now() + timedelta(days=exp_days)).isoformat() if exp_days > 0 else None
    try:
        port = int(body.get("port") or DEFAULT_PORT)
    except (TypeError, ValueError):
        port = DEFAULT_PORT
    try:
        ip_limit = int(body.get("ip_limit") or 0)
    except (TypeError, ValueError):
        ip_limit = 0

    sv = float(body.get("speed_limit_value") or 0)
    su = body.get("speed_limit_unit") or "MBIT"
    speed_limit_bytes = 0 if sv <= 0 else parse_speed_to_bytes(sv, su)

    config_password = body.get("config_password") or ""
    allowed_countries = body.get("allowed_countries") or []

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
        config_password=config_password,
        allowed_countries=allowed_countries,
        group=body.get("group") or "default",
    )

    host = get_host(request)
    return {
        "uuid": uid,
        **link,
        "expired": False,
        "vless_link": vless_link_for_link(link, uid, host),
        "sub_url": f"https://{host}/p/{uid}",
        "raw_sub_url": f"https://{host}/sub/{uid}",
    }

@app.get("/api/links")
async def list_links(request: Request, _=Depends(require_auth)):
    host = get_host(request)
    async with LINKS_LOCK:
        snap = dict(LINKS)
    result = []
    for uid, d in snap.items():
        proto = d.get("protocol", DEFAULT_PROTOCOL)
        result.append({
            "uuid": uid,
            **d,
            "protocol": proto,
            "expired": is_link_expired(d),
            "vless_link": vless_link_for_link(d, uid, host),
            "sub_url": f"https://{host}/p/{uid}",
            "raw_sub_url": f"https://{host}/sub/{uid}",
            "connected_ips": len(unique_ips_for_uuid(uid)),
        })
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"links": result}

@app.patch("/api/links/{uid}")
async def update_link(uid: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    async with LINKS_LOCK:
        if uid not in LINKS:
            raise HTTPException(status_code=404, detail="link not found")
        link = LINKS[uid]
        label = link.get("label")
        if "active" in body:
            link["active"] = bool(body["active"])
            log_activity("link", f"کانفیگ «{label}» {'فعال' if link['active'] else 'غیرفعال'} شد", "ok" if link["active"] else "warn")
        if "label" in body:
            link["label"] = str(body["label"])[:60]
        if "note" in body:
            link["note"] = str(body["note"])[:200]
        if "reset_usage" in body and body["reset_usage"]:
            link["used_bytes"] = 0
            log_activity("link", f"مصرف کانفیگ «{label}» ریست شد", "info")
        if "limit_value" in body:
            lv = float(body.get("limit_value") or 0)
            lu = body.get("limit_unit") or "GB"
            link["limit_bytes"] = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
        if "expires_days" in body:
            ed = int(body["expires_days"] or 0)
            link["expires_at"] = (datetime.now() + timedelta(days=ed)).isoformat() if ed > 0 else None
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
            sv = float(body.get("speed_limit_value") or 0)
            su = body.get("speed_limit_unit") or "MBIT"
            link["speed_limit_bytes"] = 0 if sv <= 0 else parse_speed_to_bytes(sv, su)
            from speed_limit import reset_bucket
            reset_bucket(uid)
        if "group" in body:
            link["group"] = (str(body["group"]) or "default").strip()[:60] or "default"
        if "config_password" in body:
            link["config_password"] = str(body["config_password"] or "").strip()[:100]
        if "allowed_countries" in body:
            link["allowed_countries"] = body["allowed_countries"] if isinstance(body["allowed_countries"], list) else []
        if any(k in body for k in ("label", "note", "limit_value", "expires_days", "fingerprint", "alpn", "port", "ip_limit", "speed_limit_value", "config_password", "allowed_countries")):
            log_activity("link", f"کانفیگ «{link['label']}» ویرایش شد", "info")

    asyncio.create_task(save_state())
    return {"ok": True}

@app.delete("/api/links/{uid}")
async def delete_link(uid: str, _=Depends(require_auth)):
    label = await remove_link(uid)
    if label is None:
        raise HTTPException(status_code=404, detail="link not found")
    return {"ok": True, "deleted": uid}

# ── Backup helpers ──────────────────────────────────────────────────────────
async def _create_backup_file(tag: str = "auto") -> str | None:
    """Create a JSON backup file and return its path."""
    try:
        BACKUPS_DIR.mkdir(parents=True, exist_ok=True)
        now = datetime.now()
        fname = f"backup_{now.strftime('%Y-%m-%d_%H-%M')}_{tag}.json"
        path = BACKUPS_DIR / fname
        async with SAVE_LOCK:
            data = {
                "links": dict(LINKS),
                "subs": dict(SUBS),
                "password_hash": AUTH["password_hash"],
                "saved_at": now.isoformat(),
                "backup_tag": tag,
            }
            async with aiofiles.open(path, "w", encoding="utf-8") as f:
                await f.write(json.dumps(data, ensure_ascii=False, indent=2))
        # Keep last 30 backups
        backups = sorted(BACKUPS_DIR.glob("backup_*.json"), key=lambda p: p.name, reverse=True)
        for old in backups[30:]:
            old.unlink(missing_ok=True)
        return str(path)
    except Exception as e:
        logger.warning(f"Backup failed: {e}")
        return None

async def _auto_backup_loop():
    """Background task: create backup every 24 hours."""
    while True:
        await asyncio.sleep(24 * 60 * 60)
        try:
            path = await _create_backup_file("auto")
            if path:
                logger.info(f"Auto backup created: {path}")
        except Exception as e:
            logger.warning(f"Auto backup error: {e}")

# ── Backup API ───────────────────────────────────────────────────────────────
@app.post("/api/backup/create")
async def api_backup_create(_=Depends(require_auth)):
    path = await _create_backup_file("manual")
    if path:
        log_activity("system", "پشتیبانی دستی ایجاد شد", "ok")
        return {"ok": True, "path": path}
    raise HTTPException(status_code=500, detail="backup failed")

@app.get("/api/backup/list")
async def api_backup_list(_=Depends(require_auth)):
    try:
        BACKUPS_DIR.mkdir(parents=True, exist_ok=True)
        backups = []
        for f in sorted(BACKUPS_DIR.glob("backup_*.json"), key=lambda p: p.name, reverse=True):
            stat = f.stat()
            backups.append({
                "name": f.name,
                "path": str(f),
                "size": stat.st_size,
                "size_fmt": fmt_bytes(stat.st_size),
                "created": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            })
        return {"backups": backups[:30]}
    except Exception as e:
        return {"backups": [], "error": str(e)}

@app.post("/api/backup/restore")
async def api_backup_restore(request: Request, _=Depends(require_auth)):
    body = await request.json()
    backup_path = body.get("path", "")
    if not backup_path:
        raise HTTPException(status_code=400, detail="backup path required")
    bp = Path(backup_path)
    if not bp.exists() or not str(bp).startswith(str(BACKUPS_DIR)):
        raise HTTPException(status_code=400, detail="invalid backup path")
    # Read and validate backup
    async with aiofiles.open(bp, "r", encoding="utf-8") as f:
        raw = await f.read()
    backup_data = json.loads(raw)
    required_keys = {"links", "password_hash"}
    if not required_keys.issubset(backup_data.keys()):
        raise HTTPException(status_code=400, detail="invalid backup structure")
    # Create pre-restore backup
    pre_path = await _create_backup_file("pre-restore")
    # Apply restore
    async with SAVE_LOCK:
        LINKS.clear()
        LINKS.update(backup_data.get("links", {}))
        if "subs" in backup_data:
            SUBS.clear()
            SUBS.update(backup_data["subs"])
        AUTH["password_hash"] = backup_data["password_hash"]
        data = {
            "links": dict(LINKS),
            "subs": dict(SUBS),
            "password_hash": AUTH["password_hash"],
            "totp_secret": AUTH.get("totp_secret", ""),
            "totp_enabled": AUTH.get("totp_enabled", False),
            "saved_at": datetime.now().isoformat(),
        }
        tmp = DATA_FILE.with_suffix(".tmp")
        async with aiofiles.open(tmp, "w", encoding="utf-8") as f:
            await f.write(json.dumps(data, ensure_ascii=False, indent=2))
        tmp.replace(DATA_FILE)
    log_activity("system", f"بازیابی از پشتیبان انجام شد: {bp.name}", "ok")
    return {"ok": True, "pre_restore_backup": pre_path, "restored_from": str(bp)}

# ── Config Templates API ────────────────────────────────────────────────────
@app.get("/api/templates")
async def api_templates(_=Depends(require_auth)):
    return {"templates": CONFIG_TEMPLATES}

@app.post("/api/links/from-template")
async def api_create_from_template(request: Request, _=Depends(require_auth)):
    body = await request.json()
    template_id = body.get("template", "")
    if template_id not in CONFIG_TEMPLATES:
        raise HTTPException(status_code=400, detail="template not found")
    tmpl = CONFIG_TEMPLATES[template_id]
    label = body.get("label") or tmpl["name"]
    expires_at = None
    if tmpl["expires_days"] > 0:
        expires_at = (datetime.now() + timedelta(days=tmpl["expires_days"])).isoformat()
    uid, link = await make_link(
        label=label,
        limit_bytes=tmpl["limit_bytes"],
        expires_at=expires_at,
        note=body.get("note") or f"Template: {template_id}",
        protocol=body.get("protocol") or DEFAULT_PROTOCOL,
        fingerprint=body.get("fingerprint") or DEFAULT_FINGERPRINT,
        alpn=body.get("alpn") or "",
        port=int(body.get("port") or DEFAULT_PORT),
        ip_limit=int(body.get("ip_limit") or 0),
        speed_limit_bytes=int(tmpl.get("speed_limit_bytes", 0)),
        group=body.get("group") or "default",
    )
    host = get_host(request)
    return {
        "uuid": uid,
        **link,
        "expired": False,
        "vless_link": vless_link_for_link(link, uid, host),
        "sub_url": f"https://{host}/p/{uid}",
        "raw_sub_url": f"https://{host}/sub/{uid}",
    }

# ── Groups API ───────────────────────────────────────────────────────────────
@app.get("/api/groups")
async def api_list_groups(_=Depends(require_auth)):
    async with LINKS_LOCK:
        snap = dict(LINKS)
    groups: dict[str, int] = {}
    for uid, link in snap.items():
        g = link.get("group", "default")
        groups[g] = groups.get(g, 0) + 1
    return {"groups": [{"name": g, "count": c} for g, c in sorted(groups.items())]}

@app.get("/api/groups/{group_name}/links")
async def api_group_links(group_name: str, request: Request, _=Depends(require_auth)):
    host = get_host(request)
    async with LINKS_LOCK:
        snap = dict(LINKS)
    result = []
    for uid, d in snap.items():
        if d.get("group", "default") != group_name:
            continue
        proto = d.get("protocol", DEFAULT_PROTOCOL)
        result.append({
            "uuid": uid,
            **d,
            "protocol": proto,
            "expired": is_link_expired(d),
            "vless_link": vless_link_for_link(d, uid, host),
            "sub_url": f"https://{host}/p/{uid}",
            "raw_sub_url": f"https://{host}/sub/{uid}",
            "connected_ips": len(unique_ips_for_uuid(uid)),
        })
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"links": result, "group": group_name}

@app.post("/api/groups/{group_name}/rename")
async def api_rename_group(group_name: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    new_name = (body.get("new_name") or "").strip()[:60]
    if not new_name:
        raise HTTPException(status_code=400, detail="new_name required")
    async with LINKS_LOCK:
        count = 0
        for uid, link in LINKS.items():
            if link.get("group", "default") == group_name:
                link["group"] = new_name
                count += 1
    if count:
        await save_state()
        log_activity("link", f"گروه «{group_name}» به «{new_name}» تغییر نام داده شد ({count} کانفیگ)", "info")
    return {"ok": True, "renamed": count}

@app.delete("/api/groups/{group_name}")
async def api_delete_group(group_name: str, _=Depends(require_auth)):
    if group_name == "default":
        raise HTTPException(status_code=400, detail="cannot delete default group")
    async with LINKS_LOCK:
        count = 0
        for uid, link in LINKS.items():
            if link.get("group", "default") == group_name:
                link["group"] = "default"
                count += 1
    if count:
        await save_state()
        log_activity("link", f"گروه «{group_name}» حذف شد ({count} کانفیگ به default منتقل شدند)", "info")
    return {"ok": True, "moved": count}

# ══════════════════════════════════════════════════════════════════════════════
# VLESS Relay — جدا شده به relay_vless.py (دست نخورده)
# ══════════════════════════════════════════════════════════════════════════════

from relay_vless import (
    RELAY_BUF,
    parse_vless_header,
    check_and_use,
    relay_ws_to_tcp,
    relay_tcp_to_ws,
    websocket_tunnel,
)

app.add_api_websocket_route("/ws/{uuid}", websocket_tunnel)

# ══════════════════════════════════════════════════════════════════════════════
# XHTTP — Siz10a XHTTP Ultra (ترابرد جدید، جدا از VLESS/WS، هر ۳ مد)
# ══════════════════════════════════════════════════════════════════════════════
from xhttp_siz10 import router as xhttp_router
app.include_router(xhttp_router)

# ══════════════════════════════════════════════════════════════════════════════
# Hysteria2 — پروتکل UDP/QUIC (در حال حاضر فقط stub)
# TODO: پیاده‌سازی کامل انتقال QUIC با aioquic
# ══════════════════════════════════════════════════════════════════════════════
from hysteria2 import router as hysteria2_router, generate_hysteria2_link
app.include_router(hysteria2_router)

# ══════════════════════════════════════════════════════════════════════════════
# ربات مدیریت تلگرام (اختیاری — فقط اگه TELEGRAM_BOT_TOKEN ست شده باشه فعال می‌شه)
# ══════════════════════════════════════════════════════════════════════════════
from telegram_bot import start_bot as _tg_start_bot, stop_bot as _tg_stop_bot

# ── HTTP Proxy ────────────────────────────────────────────────────────────────
_HOP = {"connection","keep-alive","proxy-authenticate","proxy-authorization",
        "te","trailers","transfer-encoding","upgrade","content-encoding","content-length"}

@app.api_route("/proxy/{target_url:path}", methods=["GET","POST","PUT","DELETE","PATCH","HEAD","OPTIONS"])
async def http_proxy(target_url: str, request: Request):
    if not target_url.startswith("http"):
        target_url = "https://" + target_url
    try:
        body = await request.body()
        headers = {k: v for k, v in request.headers.items() if k.lower() not in _HOP and k.lower() != "host"}
        resp = await http_client.request(method=request.method, url=target_url, headers=headers, content=body)
        stats["total_bytes"] += len(resp.content)
        stats["total_requests"] += 1
        now = now_ir()
        hourly_traffic[now.strftime("%H:00")] += len(resp.content)
        daily_traffic[now.strftime("%Y-%m-%d")] += len(resp.content)
        weekly_traffic[now.strftime("%Y-W%W")] += len(resp.content)
        return Response(content=resp.content, status_code=resp.status_code,
                        headers={k: v for k, v in resp.headers.items() if k.lower() not in _HOP})
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "url": target_url, "time": datetime.now().isoformat()})
        raise HTTPException(status_code=502, detail=f"Proxy error: {exc}")


# ══════════════════════════════════════════════════════════════════════════════
# Speed Test Endpoints — تست سرعت داخلی
# ══════════════════════════════════════════════════════════════════════════════

@app.get("/api/speedtest")
async def speedtest_get(_=Depends(require_auth)):
    """Get latest speed test results."""
    return {
        "speed_mbps": speedtest_results["speed_mbps"],
        "latency_ms": speedtest_results["latency_ms"],
        "last_test": speedtest_results["last_test"],
        "running": speedtest_results["running"],
    }


async def _run_speed_test():
    """Internal speed test: generate 10MB of random data, measure transfer speed."""
    import random
    try:
        speedtest_results["running"] = True
        speedtest_results["error"] = None

        # Generate 10MB of random data
        chunk_size = 1024 * 1024  # 1MB chunks
        total_size = 10 * chunk_size  # 10MB
        data = os.urandom(total_size)

        # Measure latency with a small request first
        host = get_host()
        base_url = f"https://{host}"

        latency_start = time.monotonic()
        try:
            resp = await http_client.get(f"{base_url}/health", timeout=5.0)
            latency_ms = round((time.monotonic() - latency_start) * 1000, 2)
        except Exception:
            latency_ms = -1.0

        # Measure download speed by POSTing the data and reading the response
        start_time = time.monotonic()
        try:
            # Send data to proxy endpoint as a speed test payload
            test_url = f"{base_url}/proxy/https://httpbin.org/post"
            resp = await http_client.post(
                test_url,
                content=data,
                headers={"Content-Type": "application/octet-stream"},
                timeout=60.0,
            )
            elapsed = time.monotonic() - start_time
            speed_mbps = round((total_size * 8) / (elapsed * 1_000_000), 2) if elapsed > 0 else 0.0
        except Exception as e:
            # If external proxy fails, measure with internal loopback
            elapsed = time.monotonic() - start_time
            speed_mbps = round((total_size * 8) / (elapsed * 1_000_000), 2) if elapsed > 0 else 0.0
            logger.warning(f"Speed test proxy failed (using loopback): {e}")

        speedtest_results.update({
            "speed_mbps": speed_mbps,
            "latency_ms": latency_ms,
            "last_test": datetime.now().isoformat(),
            "running": False,
        })
        log_activity("system", f"تست سرعت انجام شد: {speed_mbps} Mbps, latency: {latency_ms}ms", "ok")
        logger.info(f"Speed test complete: {speed_mbps} Mbps, {latency_ms} ms")

    except Exception as e:
        speedtest_results["running"] = False
        speedtest_results["error"] = str(e)
        logger.error(f"Speed test error: {e}")
        log_activity("system", f"خطا در تست سرعت: {e}", "err")


@app.post("/api/speedtest/run")
async def speedtest_run(_=Depends(require_auth)):
    """Trigger a speed test (non-blocking)."""
    if speedtest_results["running"]:
        raise HTTPException(status_code=429, detail="Speed test already running")
    asyncio.create_task(_run_speed_test())
    return {"ok": True, "message": "Speed test started"}


# ══════════════════════════════════════════════════════════════════════════════
# Xray Core Auto-Update Endpoints
# ══════════════════════════════════════════════════════════════════════════════

XRAY_GITHUB_API = "https://api.github.com/repos/XTLS/Xray-core/releases/latest"
XRAY_GITHUB_DOWNLOAD = "https://github.com/XTLS/Xray-core/releases/download"


async def _get_xray_version() -> str | None:
    """Get current Xray version by running 'xray version'."""
    try:
        result = await asyncio.to_thread(
            subprocess.run,
            [CONFIG["xray_binary"], "version"],
            capture_output=True, text=True, timeout=10,
        )
        output = result.stdout + result.stderr
        # Parse version like "Xray 25.6.6 (Xray, Penetrates Everything.) ..."
        for line in output.splitlines():
            if "Xray" in line and "." in line:
                parts = line.split()
                for p in parts:
                    if p[0].isdigit() and "." in p:
                        return p
        return output.strip().splitlines()[0] if output.strip() else None
    except FileNotFoundError:
        return None
    except Exception as e:
        logger.warning(f"Could not get Xray version: {e}")
        return None


async def _check_xray_update() -> dict:
    """Check GitHub for latest Xray release."""
    try:
        resp = await http_client.get(
            XRAY_GITHUB_API,
            headers={"Accept": "application/vnd.github.v3+json"},
            timeout=15.0,
        )
        resp.raise_for_status()
        data = resp.json()
        latest = data.get("tag_name", "").lstrip("v")
        xray_state["latest_version"] = latest
        xray_state["last_check"] = datetime.now().isoformat()
        current = xray_state.get("current_version") or await _get_xray_version()
        xray_state["current_version"] = current
        xray_state["update_available"] = current != latest if current else False
        xray_state["error"] = None
        return {
            "current_version": current,
            "latest_version": latest,
            "update_available": xray_state["update_available"],
            "download_url": f"{XRAY_GITHUB_DOWNLOAD}/v{latest}/Xray-linux-64.zip",
        }
    except Exception as e:
        xray_state["error"] = str(e)
        logger.error(f"Xray update check failed: {e}")
        return {"error": str(e)}


@app.get("/api/system/xray-version")
async def xray_version(_=Depends(require_auth)):
    """Get current Xray version."""
    if not xray_state["current_version"]:
        xray_state["current_version"] = await _get_xray_version()
    return {
        "current_version": xray_state["current_version"],
        "binary_path": CONFIG["xray_binary"],
    }


@app.get("/api/system/xray-update")
async def xray_update_check(_=Depends(require_auth)):
    """Check for Xray updates on GitHub."""
    return await _check_xray_update()


@app.post("/api/system/xray-update")
async def xray_update_install(_=Depends(require_auth)):
    """Download and install the latest Xray version."""
    if xray_state["updating"]:
        raise HTTPException(status_code=429, detail="Update already in progress")

    async def _do_update():
        try:
            xray_state["updating"] = True
            xray_state["error"] = None
            log_activity("system", "شروع بروزرسانی Xray Core", "info")

            # Check latest version
            info = await _check_xray_update()
            if "error" in info:
                xray_state["error"] = info["error"]
                return
            if not xray_state["update_available"]:
                log_activity("system", "Xray در جدیدترین نسخه است", "info")
                return

            latest = xray_state["latest_version"]
            download_url = f"{XRAY_GITHUB_DOWNLOAD}/v{latest}/Xray-linux-64.zip"
            zip_path = Path("/tmp/xray-update.zip")

            # Download
            logger.info(f"Downloading Xray {latest}...")
            resp = await http_client.get(download_url, timeout=120.0, follow_redirects=True)
            resp.raise_for_status()
            zip_path.write_bytes(resp.content)

            # Extract
            import zipfile
            with zipfile.ZipFile(zip_path, "r") as zf:
                for name in zf.namelist():
                    if name.endswith("xray"):
                        # Extract binary
                        data = zf.read(name)
                        tmp_bin = Path("/tmp/xray-new")
                        tmp_bin.write_bytes(data)
                        tmp_bin.chmod(0o755)

                        # Replace binary
                        xray_path = Path(CONFIG["xray_binary"])
                        xray_path.parent.mkdir(parents=True, exist_ok=True)
                        tmp_bin.replace(xray_path)
                        logger.info(f"Xray {latest} installed to {xray_path}")
                        break

            zip_path.unlink(missing_ok=True)
            xray_state["current_version"] = latest
            xray_state["update_available"] = False
            log_activity("system", f"Xray Core بروزرسانی شد به نسخه {latest}", "ok")
            logger.info(f"Xray updated to {latest}")

        except Exception as e:
            xray_state["error"] = str(e)
            logger.error(f"Xray update failed: {e}")
            log_activity("system", f"خطا در بروزرسانی Xray: {e}", "err")
        finally:
            xray_state["updating"] = False

    asyncio.create_task(_do_update())
    return {"ok": True, "message": "Update started"}


# ══════════════════════════════════════════════════════════════════════════════
# Hysteria2 Share Link Generation
# ══════════════════════════════════════════════════════════════════════════════

HY2_DEFAULT_PORT = 8443


@app.get("/api/hysteria2/link/{uuid}")
async def get_hysteria2_link(uuid: str, request: Request, _=Depends(require_auth)):
    """Generate a Hysteria2 share link for a given UUID."""
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    host = get_host(request)
    port = link.get("port", HY2_DEFAULT_PORT) if link.get("protocol") == "hysteria2" else HY2_DEFAULT_PORT
    hy2_link = generate_hysteria2_link(
        uuid=uuid,
        host=host,
        port=port,
        remark=f"X4G-{link.get('label', '')}",
        sni=host,
    )
    return {"link": hy2_link, "uuid": uuid}


# ── Public sub page (یک صفحه‌ی زیبا و مستقل به‌ازای هر کانفیگ) ────────────────
@app.get("/p/{uuid_key}", response_class=HTMLResponse)
async def public_sub_page(uuid_key: str, request: Request):
    from pages import get_public_page_html
    async with LINKS_LOCK:
        exists = uuid_key in LINKS
    if not exists:
        return HTMLResponse("<h2 style='font-family:sans-serif;padding:40px'>کانفیگ پیدا نشد</h2>", status_code=404)
    return HTMLResponse(content=get_public_page_html(uuid_key))

@app.get("/api/public/sub/{uuid_key}")
async def public_sub_data(uuid_key: str, request: Request):
    async with LINKS_LOCK:
        link = LINKS.get(uuid_key)
    if not link:
        raise HTTPException(status_code=404, detail="not found")

    host = get_host(request)
    allowed = is_link_allowed(link)
    conn_count = sum(1 for c in connections.values() if c.get("uuid") == uuid_key)
    proto = link.get("protocol", DEFAULT_PROTOCOL)
    link_out = {
        "uuid": uuid_key,
        "label": link["label"],
        "active": allowed,
        "protocol": proto,
        "used_bytes": link.get("used_bytes", 0),
        "used_fmt": fmt_bytes(link.get("used_bytes", 0)),
        "limit_bytes": link.get("limit_bytes", 0),
        "limit_fmt": "∞" if link.get("limit_bytes", 0) == 0 else fmt_bytes(link["limit_bytes"]),
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

# ── Analytics API Endpoints ───────────────────────────────────────────────────

@app.get("/api/reports/traffic")
async def get_traffic_reports(_=Depends(require_auth)):
    """Daily + weekly traffic reports."""
    now = now_ir()
    today = now.strftime("%Y-%m-%d")
    yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
    last_week = (now - timedelta(weeks=1)).strftime("%Y-W%W")
    this_week = now.strftime("%Y-W%W")

    # Last 7 days of daily traffic
    last_7_days = {}
    for i in range(7):
        d = (now - timedelta(days=i)).strftime("%Y-%m-%d")
        last_7_days[d] = daily_traffic.get(d, 0)

    # Protocol breakdown from connections
    protocol_breakdown = defaultdict(int)
    for conn in connections.values():
        proto = conn.get("transport", "vless-ws")
        protocol_breakdown[proto] += conn.get("bytes", 0)

    return {
        "daily": dict(daily_traffic),
        "weekly": dict(weekly_traffic),
        "last_7_days": last_7_days,
        "today_bytes": daily_traffic.get(today, 0),
        "yesterday_bytes": daily_traffic.get(yesterday, 0),
        "this_week_bytes": weekly_traffic.get(this_week, 0),
        "last_week_bytes": weekly_traffic.get(last_week, 0),
        "protocol_breakdown": dict(protocol_breakdown),
        "today_fmt": fmt_bytes(daily_traffic.get(today, 0)),
        "yesterday_fmt": fmt_bytes(daily_traffic.get(yesterday, 0)),
        "this_week_fmt": fmt_bytes(weekly_traffic.get(this_week, 0)),
        "last_week_fmt": fmt_bytes(weekly_traffic.get(last_week, 0)),
    }


@app.get("/api/connections/map")
async def get_connection_map(_=Depends(require_auth)):
    """GeoIP map of active connections."""
    now_ts = time.time()
    ip_counts: dict[str, int] = defaultdict(int)

    for conn in connections.values():
        ip = conn.get("ip")
        if ip:
            ip_counts[ip] += 1

    results = []
    for ip, count in ip_counts.items():
        # Check cache
        cached = geoip_cache.get(ip)
        if cached and (now_ts - cached.get("cached_at", 0)) < GEOIP_CACHE_TTL:
            geo = cached
        else:
            # Skip private IPs for GeoIP
            if ip.startswith("127.") or ip.startswith("10.") or ip.startswith("192.168.") or ip == "::1":
                geo = {
                    "ip": ip,
                    "lat": 0, "lon": 0,
                    "country": "Local", "city": "Local",
                    "cached_at": now_ts,
                }
            else:
                try:
                    resp = await http_client.get(f"http://ip-api.com/json/{ip}?fields=status,country,countryCode,city,lat,lon", timeout=5.0)
                    data = resp.json()
                    if data.get("status") == "success":
                        geo = {
                            "ip": ip,
                            "lat": data.get("lat", 0),
                            "lon": data.get("lon", 0),
                            "country": data.get("country", "Unknown"),
                            "country_code": data.get("countryCode", ""),
                            "city": data.get("city", "Unknown"),
                            "cached_at": now_ts,
                        }
                    else:
                        geo = {
                            "ip": ip, "lat": 0, "lon": 0,
                            "country": "Unknown", "country_code": "",
                            "city": "Unknown", "cached_at": now_ts,
                        }
                except Exception:
                    geo = {
                        "ip": ip, "lat": 0, "lon": 0,
                        "country": "Unknown", "country_code": "",
                        "city": "Unknown", "cached_at": now_ts,
                    }
            geoip_cache[ip] = geo

        results.append({
            "ip": ip,
            "lat": geo.get("lat", 0),
            "lon": geo.get("lon", 0),
            "country": geo.get("country", "Unknown"),
            "country_code": geo.get("country_code", ""),
            "city": geo.get("city", "Unknown"),
            "count": count,
        })

    return {"locations": results, "total_ips": len(results)}


@app.get("/api/reports/predict")
async def get_usage_predictions(_=Depends(require_auth)):
    """Predict when links will hit quota or expire."""
    now = now_ir()
    predictions = []

    async with LINKS_LOCK:
        snap = dict(LINKS)

    for uid, link in snap.items():
        days_until_quota = None
        days_until_expiry = None

        # Calculate average daily usage from daily_traffic (total, not per-link)
        # For per-link prediction, use used_bytes and creation time
        created = link.get("created_at")
        used = link.get("used_bytes", 0)
        limit = link.get("limit_bytes", 0)

        if created and used > 0 and limit > 0:
            try:
                created_dt = datetime.fromisoformat(created)
                days_active = max(1, (now - created_dt).total_seconds() / 86400)
                avg_daily = used / days_active
                remaining = max(0, limit - used)
                if avg_daily > 0 and remaining > 0:
                    days_until_quota = int(remaining / avg_daily)
            except Exception:
                pass

        exp = link.get("expires_at")
        if exp:
            try:
                exp_dt = datetime.fromisoformat(exp)
                days_until_expiry = max(0, int((exp_dt - now).total_seconds() / 86400))
            except Exception:
                pass

        predictions.append({
            "uuid": uid,
            "label": link.get("label", ""),
            "used_bytes": used,
            "used_fmt": fmt_bytes(used),
            "limit_bytes": limit,
            "limit_fmt": fmt_bytes(limit) if limit > 0 else "∞",
            "days_until_quota": days_until_quota,
            "days_until_expiry": days_until_expiry,
            "expires_at": exp,
        })

    predictions.sort(key=lambda x: (x["days_until_quota"] or 99999, x["days_until_expiry"] or 99999))
    return {"predictions": predictions}


@app.get("/api/system/uptime")
async def get_uptime(_=Depends(require_auth)):
    """Server uptime information."""
    secs = int(time.time() - stats["start_time"])
    days = secs // 86400
    hours = (secs % 86400) // 3600
    minutes = (secs % 3600) // 60
    seconds = secs % 60

    parts = []
    if days > 0:
        parts.append(f"{days}d")
    if hours > 0 or days > 0:
        parts.append(f"{hours}h")
    if minutes > 0 or hours > 0 or days > 0:
        parts.append(f"{minutes}m")
    parts.append(f"{seconds}s")
    uptime_human = " ".join(parts)

    return {
        "start_time": datetime.fromtimestamp(stats["start_time"]).isoformat(),
        "uptime_seconds": secs,
        "uptime_human": uptime_human,
        "restart_count": restart_count,
        "uptime_history": list(uptime_history)[-30:],
    }


# ── PWA Manifest & Service Worker ─────────────────────────────────────────────
@app.get("/manifest.json")
async def pwa_manifest(request: Request):
    logo_b64 = ""
    try:
        from pages import LOGO_B64
        logo_b64 = LOGO_B64
    except Exception:
        pass
    icon_data_uri = f"data:image/png;base64,{logo_b64}" if logo_b64 else ""
    manifest = {
        "name": "X4G Panel",
        "short_name": "X4G",
        "description": "X4G Panel Management Dashboard",
        "start_url": "/dashboard",
        "display": "standalone",
        "theme_color": "#0F0B1A",
        "background_color": "#0F0B1A",
        "orientation": "any",
        "icons": [{"src": icon_data_uri, "sizes": "192x192", "type": "image/png", "purpose": "any maskable"}] if icon_data_uri else []
    }
    return JSONResponse(content=manifest)

SW_JS = """
const CACHE_NAME = 'x4g-panel-v1';
const CRITICAL_ASSETS = ['/', '/login', '/dashboard'];
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(CRITICAL_ASSETS)).then(() => self.skipWaiting())
  );
});
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))).then(() => self.clients.claim())
  );
});
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  if (event.request.url.includes('/api/') || event.request.url.includes('/ws/')) return;
  event.respondWith(
    fetch(event.request).then(response => {
      const clone = response.clone();
      caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
      return response;
    }).catch(() => caches.match(event.request).then(r => r || caches.match('/')))
  );
});
"""

@app.get("/sw.js")
async def service_worker():
    return Response(content=SW_JS, media_type="application/javascript")

# ── Notifications API ─────────────────────────────────────────────────────────
notif_subscribers: list = []

@app.get("/api/notifications")
async def get_notifications(request: Request):
    if not await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        raise HTTPException(status_code=401)
    return JSONResponse(content={"notifications": []})

@app.websocket("/ws/notifications")
async def ws_notifications(websocket: WebSocket):
    await websocket.accept()
    notif_subscribers.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        notif_subscribers.remove(websocket)
    except Exception:
        if websocket in notif_subscribers:
            notif_subscribers.remove(websocket)

# ── HTML Pages (login + dashboard) ───────────────────────────────────────────
from pages import LOGIN_HTML, DASHBOARD_HTML

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    if await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        return RedirectResponse(url="/dashboard")
    return HTMLResponse(content=LOGIN_HTML)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    if not await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        return RedirectResponse(url="/login")
    return HTMLResponse(content=DASHBOARD_HTML)

@app.get("/test-ws", response_class=HTMLResponse)
async def test_ws_redirect():
    return HTMLResponse(content="<script>location.href='/dashboard'</script>")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=CONFIG["port"], log_level="info", workers=1)
