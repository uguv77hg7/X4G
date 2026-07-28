# telegram_bot.py
# ══════════════════════════════════════════════════════════════════════════════
# ربات مدیریت تلگرام — ساخت/حذف/فعال‌غیرفعال/مشاهده‌ی کانفیگ‌ها، فقط برای ادمین‌های
# مجاز (TELEGRAM_ADMIN_IDS). با long polling کار می‌کنه، نیازی به دامنه/webhook نداره.
# ══════════════════════════════════════════════════════════════════════════════

import asyncio
import os
import re
import math

import httpx

from datetime import datetime, timedelta, timezone

from main import (
    LINKS,
    make_link,
    remove_link,
    set_link_active,
    vless_link_for_link,
    get_host,
    fmt_bytes,
    is_link_allowed,
    logger,
    PROTOCOLS,
    DEFAULT_PROTOCOL,
    FINGERPRINTS,
    DEFAULT_FINGERPRINT,
    DEFAULT_ALPN_BY_PROTOCOL,
    DEFAULT_PORT,
    DEFAULT_SPEED_LIMIT,
    MIN_PORT,
    MAX_PORT,
    parse_size_to_bytes,
    parse_speed_to_bytes,
)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
_admin_ids_raw = os.environ.get("TELEGRAM_ADMIN_IDS", "").strip()
ADMIN_IDS = {int(x) for x in _admin_ids_raw.replace(" ", "").split(",") if x.isdigit()} if _admin_ids_raw else set()

API_BASE = f"https://api.telegram.org/bot{BOT_TOKEN}"
PAGE_SIZE = 6

_client: httpx.AsyncClient | None = None
_poll_task: asyncio.Task | None = None
_running = False
_pending: dict = {}   # chat_id -> {"action": "wizard", "step": "...", "data": {...}}

# ── Config creation wizard ────────────────────────────────────────────────────
WIZARD_STEPS = ["label", "protocol", "fingerprint", "alpn", "port", "volume", "speed", "iplimit", "days"]

PROTOCOL_LABELS = {
    "vless-ws": "VLESS + WebSocket",
    "xhttp": "XHTTP (mode: auto)",
}

def _protocol_label(p: str) -> str:
    return PROTOCOL_LABELS.get(p, p)

def _fp_label(fp: str) -> str:
    return fp.capitalize()

_VOLUME_RE = re.compile(r"^([\d.]+)\s*(GB|MB|KB)?$", re.IGNORECASE)
_SPEED_RE = re.compile(r"^([\d.]+)\s*(MBIT|MBPS|MB|KB)?$", re.IGNORECASE)

def _parse_volume_text(text: str):
    m = _VOLUME_RE.match(text.strip())
    if not m:
        return None
    try:
        value = float(m.group(1))
    except ValueError:
        return None
    if value <= 0:
        return 0
    unit = (m.group(2) or "GB").upper()
    return parse_size_to_bytes(value, unit)

def _parse_speed_text(text: str):
    m = _SPEED_RE.match(text.strip())
    if not m:
        return None
    try:
        value = float(m.group(1))
    except ValueError:
        return None
    if value <= 0:
        return 0
    unit_raw = (m.group(2) or "MBIT").upper()
    unit = "MBIT" if unit_raw in ("MBIT", "MBPS") else unit_raw
    return parse_speed_to_bytes(value, unit)

def _parse_nonneg_int(text: str):
    try:
        n = int(text.strip())
    except ValueError:
        return None
    return max(0, n)

# ── Appearance helpers ─────────────────────────────────────────────────────────

def _progress_bar(used: int, total: int) -> str:
    """Render a Unicode progress bar for bandwidth usage."""
    if total <= 0:
        return "░░░░░░░░  ——"
    pct = min(used / total, 1.0)
    filled = round(pct * 8)
    empty = 8 - filled
    bar = "█" * filled + "░" * empty
    if pct < 0.5:
        color_bar = f"🟢 {bar}"
    elif pct < 0.8:
        color_bar = f"🟡 {bar}"
    else:
        color_bar = f"🔴 {bar}"
    return f"{color_bar} {pct*100:.0f}%"

def _status_emoji(link: dict) -> str:
    """Return a color-coded status emoji based on link state and expiration."""
    if not is_link_allowed(link):
        return "🔴"
    exp = link.get("expires_at")
    if exp:
        try:
            exp_dt = datetime.fromisoformat(exp)
            now = datetime.now(timezone.utc) if exp_dt.tzinfo else datetime.now()
            days_left = (exp_dt.replace(tzinfo=None) - datetime.now()).days if not exp_dt.tzinfo else (exp_dt - datetime.now(timezone.utc)).days
            if days_left <= 3:
                return "🟡"
        except Exception:
            pass
    return "🟢"

def _expiration_warning(link: dict) -> str:
    """Return a warning string if config is expiring within 3 days, else empty."""
    exp = link.get("expires_at")
    if not exp:
        return ""
    try:
        exp_dt = datetime.fromisoformat(exp)
        now = datetime.now(timezone.utc) if exp_dt.tzinfo else datetime.now()
        days_left = (exp_dt.replace(tzinfo=None) - datetime.now()).days if not exp_dt.tzinfo else (exp_dt - datetime.now(timezone.utc)).days
        if days_left <= 3:
            if days_left <= 0:
                return "\n⚠️ <b>انقضا رسیده!</b>"
            return f"\n⚠️ <b>منقضی می‌شه تا {days_left} روز دیگه!</b>"
    except Exception:
        pass
    return ""

def _days_until_expiry(link: dict) -> int | None:
    """Return days until expiry, or None if no expiry."""
    exp = link.get("expires_at")
    if not exp:
        return None
    try:
        exp_dt = datetime.fromisoformat(exp)
        now = datetime.now(timezone.utc) if exp_dt.tzinfo else datetime.now()
        days = (exp_dt.replace(tzinfo=None) - datetime.now()).days if not exp_dt.tzinfo else (exp_dt - datetime.now(timezone.utc)).days
        return max(0, days)
    except Exception:
        return None

def _box_header(title: str, width: int = 22) -> str:
    """Create a beautiful box-drawing header. CJK chars count as 2 width units."""
    def _display_width(s):
        w = 0
        for ch in s:
            if ord(ch) > 0x2e80:
                w += 2
            else:
                w += 1
        return w

    title_w = _display_width(title)
    inner = width - 2
    pad_left = max(0, (inner - title_w) // 2)
    pad_right = max(0, inner - title_w - pad_left)
    top = "╔" + "═" * inner + "╗"
    mid = "║" + " " * pad_left + title + " " * pad_right + "║"
    bot = "╚" + "═" * inner + "╝"
    return f"{top}\n{mid}\n{bot}"

def _separator() -> str:
    return "────────────────────────"

def _double_separator() -> str:
    return "══════════════════════════"

# ── Telegram API helpers ────────────────────────────────────────────────────────
async def _call(method: str, **params):
    if _client is None:
        return None
    try:
        r = await _client.post(f"{API_BASE}/{method}", json=params, timeout=40)
        data = r.json()
        if not data.get("ok"):
            logger.warning(f"Telegram API {method} failed: {data}")
        return data
    except Exception as e:
        logger.warning(f"Telegram API {method} error: {e}")
        return None

async def _send(chat_id: int, text: str, kb: dict | None = None):
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True}
    if kb:
        payload["reply_markup"] = kb
    return await _call("sendMessage", **payload)

async def _edit(chat_id: int, message_id: int, text: str, kb: dict | None = None):
    payload = {"chat_id": chat_id, "message_id": message_id, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True}
    if kb:
        payload["reply_markup"] = kb
    res = await _call("editMessageText", **payload)
    if res is None or not res.get("ok"):
        await _send(chat_id, text, kb)

async def _answer_cb(cb_id: str, text: str = ""):
    await _call("answerCallbackQuery", callback_query_id=cb_id, text=text)

def _is_admin(chat_id: int) -> bool:
    return chat_id in ADMIN_IDS

# ── Keyboards ──────────────────────────────────────────────────────────────────
def _main_menu_kb():
    return {"inline_keyboard": [
        [{"text": "📋 لیست کانفیگ‌ها", "callback_data": "list:0"}],
        [{"text": "➕ ساخت کانفیگ جدید", "callback_data": "newcfg"}],
        [{"text": "📊 آمار و اطلاعات", "callback_data": "stats"}],
        [{"text": "🔍 جستجو", "callback_data": "searchask"}],
        [{"text": "📤 خروجی فعال‌ها", "callback_data": "export"}],
        [{"text": "🗑 حذف همه غیرفعال‌ها", "callback_data": "delall_inactive"}],
        [{"text": "❓ راهنما", "callback_data": "help"}],
        [{"text": "🔄 رفرش", "callback_data": "menu"}],
    ]}

def _links_list_kb(page: int):
    items = sorted(LINKS.items(), key=lambda kv: kv[1].get("created_at", ""), reverse=True)
    total = len(items)
    start = page * PAGE_SIZE
    chunk = items[start:start + PAGE_SIZE]
    rows = []
    for uid, l in chunk:
        dot = _status_emoji(l)
        label = l.get('label', '?')[:28]
        exp_warn = _expiration_warning(l)
        btn_text = f"{dot} {label}"
        if exp_warn and "⚠️" in exp_warn:
            btn_text = f"⏰ {label}"
        rows.append([{"text": btn_text, "callback_data": f"view:{uid}"}])
    nav = []
    if start > 0:
        nav.append({"text": "◀ قبلی", "callback_data": f"list:{page-1}"})
    if start + PAGE_SIZE < total:
        nav.append({"text": "بعدی ▶", "callback_data": f"list:{page+1}"})
    if nav:
        rows.append(nav)
    rows.append([{"text": "➕ ساخت کانفیگ جدید", "callback_data": "newcfg"}])
    rows.append([{"text": "⬅ منوی اصلی", "callback_data": "menu"}])
    return {"inline_keyboard": rows}

def _link_detail_kb(uid: str, active: bool):
    return {"inline_keyboard": [
        [{"text": "🔗 نمایش لینک اتصال", "callback_data": f"link:{uid}"}],
        [{"text": "📋 کپی لینک", "callback_data": f"copy:{uid}"},
         {"text": "📤 اشتراک‌گذاری", "callback_data": f"share:{uid}"}],
        [{"text": ("⛔ غیرفعال‌سازی" if active else "✅ فعال‌سازی"), "callback_data": f"toggle:{uid}"}],
        [{"text": "🗑 حذف کانفیگ", "callback_data": f"del:{uid}"}],
        [{"text": "⬅ بازگشت به لیست", "callback_data": "list:0"}],
    ]}

def _confirm_delete_kb(uid: str):
    return {"inline_keyboard": [
        [{"text": "✅ بله، حذف کن", "callback_data": f"delok:{uid}"},
         {"text": "❌ انصراف", "callback_data": f"view:{uid}"}],
    ]}

def _confirm_bulk_delete_kb():
    inactive_count = sum(1 for l in LINKS.values() if not l.get("active", True))
    return {"inline_keyboard": [
        [{"text": f"✅ بله، حذف {inactive_count} کانفیگ غیرفعال", "callback_data": "delall_confirm"}],
        [{"text": "❌ انصراف", "callback_data": "menu"}],
    ]}

def _export_done_kb():
    return {"inline_keyboard": [
        [{"text": "📋 لیست کانفیگ‌ها", "callback_data": "list:0"}],
        [{"text": "⬅ منوی اصلی", "callback_data": "menu"}],
    ]}

def _stats_kb():
    return {"inline_keyboard": [
        [{"text": "🔄 بروزرسانی", "callback_data": "stats"}],
        [{"text": "⬅ منوی اصلی", "callback_data": "menu"}],
    ]}

def _help_kb():
    return {"inline_keyboard": [
        [{"text": "📋 لیست کانفیگ‌ها", "callback_data": "list:0"}],
        [{"text": "➕ ساخت کانفیگ جدید", "callback_data": "newcfg"}],
        [{"text": "⬅ منوی اصلی", "callback_data": "menu"}],
    ]}

def _search_results_kb(query: str, results: list, page: int):
    """Pagination keyboard for search results."""
    per_page = 5
    total = len(results)
    start = page * per_page
    chunk = results[start:start + per_page]
    rows = []
    for uid, l in chunk:
        dot = _status_emoji(l)
        label = l.get('label', '?')[:30]
        rows.append([{"text": f"{dot} {label}", "callback_data": f"view:{uid}"}])
    nav = []
    if start > 0:
        nav.append({"text": "◀ قبلی", "callback_data": f"searchpage:{query}:{page-1}"})
    if start + per_page < total:
        nav.append({"text": "بعدی ▶", "callback_data": f"searchpage:{query}:{page+1}"})
    if nav:
        rows.append(nav)
    rows.append([{"text": "🔍 جستجوی جدید", "callback_data": "searchask"}])
    rows.append([{"text": "⬅ منوی اصلی", "callback_data": "menu"}])
    return {"inline_keyboard": rows}

# ── Wizard keyboards ───────────────────────────────────────────────────────────
def _wizard_cancel_kb():
    return {"inline_keyboard": [[{"text": "❌ انصراف", "callback_data": "w:cancel"}]]}

def _wizard_protocol_kb():
    rows = [[{"text": _protocol_label(p), "callback_data": f"w:proto:{p}"}] for p in PROTOCOLS]
    rows.append([{"text": "❌ انصراف", "callback_data": "w:cancel"}])
    return {"inline_keyboard": rows}

def _wizard_fp_kb():
    rows, row = [], []
    for fp in FINGERPRINTS:
        row.append({"text": _fp_label(fp), "callback_data": f"w:fp:{fp}"})
        if len(row) == 3:
            rows.append(row); row = []
    if row:
        rows.append(row)
    rows.append([{"text": "❌ انصراف", "callback_data": "w:cancel"}])
    return {"inline_keyboard": rows}

def _wizard_skip_kb(step_key: str, label: str):
    return {"inline_keyboard": [
        [{"text": label, "callback_data": f"w:skip:{step_key}"}],
        [{"text": "❌ انصراف", "callback_data": "w:cancel"}],
    ]}

ALPN_PRESET_MAP = {"p1": "http/1.1", "p2": "h2,http/1.1", "p3": "h2"}

def _wizard_alpn_kb():
    return {"inline_keyboard": [
        [{"text": "🔤 http/1.1 (پیشنهادی)", "callback_data": "w:alpnpreset:p1"}],
        [{"text": "🔤 h2,http/1.1", "callback_data": "w:alpnpreset:p2"}],
        [{"text": "🔤 h2", "callback_data": "w:alpnpreset:p3"}],
        [{"text": "⏭ پیش‌فرض پروتکل", "callback_data": "w:skip:alpn"}],
        [{"text": "❌ انصراف", "callback_data": "w:cancel"}],
    ]}

def _wizard_unlimited_kb(step_key: str):
    return _wizard_skip_kb(step_key, "♾ نامحدود")

def _wizard_confirm_kb():
    return {"inline_keyboard": [
        [{"text": "✅ ساخت کانفیگ", "callback_data": "w:confirm"}],
        [{"text": "❌ انصراف", "callback_data": "w:cancel"}],
    ]}

def _wizard_prompt(step: str, data: dict) -> str:
    n = WIZARD_STEPS.index(step) + 1 if step in WIZARD_STEPS else len(WIZARD_STEPS)
    head = f"🧩 ساخت کانفیگ جدید — مرحله {n}/{len(WIZARD_STEPS)}\n\n"
    if step == "label":
        return head + "✏️ اسم/برچسب کانفیگ رو بفرست:"
    if step == "protocol":
        return head + "🌐 پروتکل رو از دکمه‌های زیر انتخاب کن:"
    if step == "fingerprint":
        return head + "🖐 Fingerprint (uTLS) رو انتخاب کن:"
    if step == "alpn":
        return head + ("🔤 ALPN رو از دکمه‌های زیر انتخاب کن (پیشنهادی: <code>http/1.1</code>)\n"
                        "یا خودت هر مقدار دلخواهی رو تایپ و ارسال کن (مثلاً h2,http/1.1):")
    if step == "port":
        return head + f"🔌 شماره پورت (بین {MIN_PORT} تا {MAX_PORT}) رو بفرست\nیا پیش‌فرض ({DEFAULT_PORT}) رو انتخاب کن:"
    if step == "volume":
        return head + "📦 محدودیت حجم مصرفی رو بفرست، مثلاً:\n<code>10GB</code> یا <code>500MB</code>\nیا دکمه‌ی نامحدود رو بزن:"
    if step == "speed":
        return head + "🚀 محدودیت سرعت رو به مگابیت‌بر‌ثانیه بفرست، مثلاً <code>20</code>\nیا دکمه‌ی نامحدود رو بزن:"
    if step == "iplimit":
        return head + "👥 حداکثر تعداد آی‌پی/کاربر هم‌زمان مجاز رو بفرست\nیا دکمه‌ی نامحدود رو بزن:"
    if step == "days":
        return head + "📅 تعداد روزهای اعتبار کانفیگ رو بفرست\nیا دکمه‌ی نامحدود (بدون انقضا) رو بزن:"
    return head

def _wizard_summary(data: dict) -> str:
    limit = "نامحدود" if not data.get("limit_bytes") else fmt_bytes(data["limit_bytes"])
    speed = "نامحدود" if not data.get("speed_limit_bytes") else f"{data['speed_limit_bytes']*8/1024/1024:.1f} Mbps"
    iplim = data.get("ip_limit", 0) or "نامحدود"
    days = data.get("expires_days", 0)
    days_txt = "بدون انقضا" if not days else f"{days} روز"
    proto = data.get("protocol", DEFAULT_PROTOCOL)
    alpn = data.get("alpn") or f"پیش‌فرض ({DEFAULT_ALPN_BY_PROTOCOL.get(proto, 'http/1.1')})"
    return (
        f"{_double_separator()}\n"
        f"🧩 خلاصه‌ی کانفیگ جدید — تایید کن\n"
        f"{_double_separator()}\n\n"
        f"📛 برچسب: <b>{data.get('label','?')}</b>\n"
        f"🌐 پروتکل: {_protocol_label(proto)}\n"
        f"🖐 Fingerprint: {_fp_label(data.get('fingerprint', DEFAULT_FINGERPRINT))}\n"
        f"🔤 ALPN: {alpn}\n"
        f"🔌 پورت: {data.get('port', DEFAULT_PORT)}\n"
        f"📦 حجم: {limit}\n"
        f"🚀 سرعت: {speed}\n"
        f"👥 آی‌پی: {iplim}\n"
        f"📅 انقضا: {days_txt}\n"
        f"{_double_separator()}"
    )

# ── View builders ──────────────────────────────────────────────────────────────

def _format_detail(uid: str, l: dict) -> str:
    """Enhanced detail view with sections, progress bar, and more info."""
    status_emoji = _status_emoji(l)
    status_text = "🟢 فعال" if is_link_allowed(l) else "🔴 غیرفعال/منقضی"
    limit = "نامحدود" if not l.get("limit_bytes") else fmt_bytes(l["limit_bytes"])
    used = l.get('used_bytes', 0)
    speed = "نامحدود" if not l.get("speed_limit_bytes") else f"{l['speed_limit_bytes']*8/1024/1024:.1f} Mbps"
    exp = l.get("expires_at")
    exp_txt = exp.split("T")[0] if exp else "بدون انقضا"
    proto = l.get("protocol", DEFAULT_PROTOCOL)
    alpn = l.get("alpn") or f"پیش‌فرض ({DEFAULT_ALPN_BY_PROTOCOL.get(proto, 'http/1.1')})"
    created = l.get("created_at", "").split("T")[0] if l.get("created_at") else "—"
    last_seen = l.get("last_seen", "")
    last_seen_txt = last_seen.split("T")[0] if last_seen else "هرگز"
    conn_count = l.get("conn_count", 0)
    host = get_host()
    exp_warning = _expiration_warning(l)

    # Progress bar
    bar = _progress_bar(used, l.get("limit_bytes", 0)) if l.get("limit_bytes") else "♾ نامحدود"

    lines = [
        f"{_box_header(l.get('label', '?')[:18])}",
        "",
        f"{_separator()}",
        f"📌 <b>وضعیت:</b> {status_emoji} {status_text}",
        f"{_separator()}",
        "",
        f"📦 <b>مصرف پهنای باند:</b>",
        f"   {bar}",
        f"   {fmt_bytes(used)} / {limit}",
        "",
    ]

    if exp_warning:
        lines.append(f"{exp_warning}")
        lines.append("")

    lines += [
        f"🌐 <b>اتصالات:</b>",
        f"   {conn_count} اتصال فعال",
        "",
        f"👤 <b>محدودیت آی‌پی:</b> {l.get('ip_limit',0) or 'نامحدود'}",
        f"🚀 <b>محدودیت سرعت:</b> {speed}",
        "",
        f"{_double_separator()}",
        f"⚙️ <b>تنظیمات فنی:</b>",
        f"{_separator()}",
        f"   📡 پروتکل: {_protocol_label(proto)}",
        f"   🖐 Fingerprint: {_fp_label(l.get('fingerprint', DEFAULT_FINGERPRINT))}",
        f"   🔤 ALPN: {alpn}",
        f"   🔌 پورت: {l.get('port', DEFAULT_PORT)}",
        f"   🖥 سرور: <code>{host}</code>",
        "",
        f"{_double_separator()}",
        f"📅 <b>تاریخچه:</b>",
        f"{_separator()}",
        f"   📆 ساخت: {created}",
        f"   🔗 آخرین اتصال: {last_seen_txt}",
        f"   ⏰ انقضا: {exp_txt}",
        "",
        f"🔑 <code>{uid}</code>",
    ]

    return "\n".join(lines)

def _format_stats() -> str:
    """Format statistics as a beautiful card."""
    total = len(LINKS)
    active = sum(1 for l in LINKS.values() if is_link_allowed(l))
    inactive = total - active
    total_used = sum(l.get("used_bytes", 0) for l in LINKS.values())
    total_limit = sum(l.get("limit_bytes", 0) for l in LINKS.values() if l.get("limit_bytes"))

    # Count expiring soon (within 7 days)
    expiring_soon = 0
    expiring_configs = []
    now = datetime.now()
    for uid, l in LINKS.items():
        exp = l.get("expires_at")
        if exp:
            try:
                exp_dt = datetime.fromisoformat(exp)
                days = (exp_dt.replace(tzinfo=None) - now).days if not exp_dt.tzinfo else (exp_dt - datetime.now(timezone.utc)).days
                if 0 < days <= 7:
                    expiring_soon += 1
                    expiring_configs.append(f"  ⏰ {l.get('label', '?')[:20]} — {days} روز دیگه")
            except Exception:
                pass

    bar = _progress_bar(total_used, total_limit) if total_limit > 0 else "♾ نامحدود"

    lines = [
        f"{_box_header('📊 آمار و اطلاعات')}",
        "",
        f"{_double_separator()}",
        f"📋 <b>تعداد کل کانفیگ‌ها:</b> <b>{total}</b>",
        f"{_separator()}",
        f"   🟢 فعال: <b>{active}</b>",
        f"   🔴 غیرفعال/منقضی: <b>{inactive}</b>",
        "",
        f"{_double_separator()}",
        f"📦 <b>مصرف کل پهنای باند:</b>",
        f"   {bar}",
        f"   {fmt_bytes(total_used)}" + (f" / {fmt_bytes(total_limit)}" if total_limit else ""),
        "",
        f"{_double_separator()}",
        f"⏰ <b>منقضی‌شونده تا ۷ روز آینده:</b> <b>{expiring_soon}</b>",
    ]

    if expiring_configs:
        lines.append(_separator())
        for line in expiring_configs[:5]:
            lines.append(line)
        if len(expiring_configs) > 5:
            lines.append(f"  ... و {len(expiring_configs) - 5} مورد دیگر")

    lines += [
        "",
        f"{_double_separator()}",
        f"🕐 <b>زمان سرور:</b> {now.strftime('%Y-%m-%d %H:%M')}",
    ]

    return "\n".join(lines)

def _format_export() -> str:
    """Export all active configs as vless links."""
    host = get_host()
    active_links = []
    for uid, l in LINKS.items():
        if is_link_allowed(l):
            vless = vless_link_for_link(l, uid, host)
            active_links.append((l.get('label', '?'), vless))

    if not active_links:
        return "📭 هیچ کانفیگ فعالی برای خروجی وجود نداره."

    lines = [
        f"{_box_header('📤 خروجی کانفیگ‌ها')}",
        "",
        f"تعداد: <b>{len(active_links)}</b> کانفیگ فعال",
        f"{_separator()}",
        "",
    ]

    for i, (label, vless) in enumerate(active_links, 1):
        lines.append(f"<b>{i}. {label}</b>")
        lines.append(f"<code>{vless}</code>")
        lines.append("")

    lines += [
        f"{_separator()}",
        "💡 <i>برای کپی روی لینک ضربه بزنید</i>",
    ]

    return "\n".join(lines)

def _format_help() -> str:
    """Show all available commands with descriptions."""
    lines = [
        f"{_box_header('❓ راهنمای ربات')}",
        "",
        f"<b>📝 دستورات:</b>",
        f"{_separator()}",
        "",
        f"📋 <b>/start</b>  — نمایش منوی اصلی",
        f"📊 <b>/stats</b>  — آمار و اطلاعات کانفیگ‌ها",
        f"🔍 <b>/search &lt;query&gt;</b>  — جستجوی کانفیگ‌ها",
        f"📤 <b>/export</b>  — خروجی لینک‌های فعال",
        f"❓ <b>/help</b>  — نمایش این راهنما",
        f"❌ <b>/cancel</b>  — لغو عملیات جاری",
        "",
        f"{_separator()}",
        f"<b>🔘 قابلیت‌ها:</b>",
        f"{_separator()}",
        "",
        f"➕ <b>ساخت کانفیگ:</b> با استفاده از ویزارد ۹ مرحله‌ای",
        f"👁 <b>مشاهده جزئیات:</b> اطلاعات کامل + نوار مصرف",
        f"🔗 <b>لینک اتصال:</b> vless + ساب ساده + ساب حرفه‌ای",
        f"📋 <b>کپی لینک:</b> کپی سریع لینک اتصال",
        f"📤 <b>اشتراک‌گذاری:</b> ارسال لینک اتصال",
        f"✅/⛔ <b>فعال/غیرفعال:</b> تغییر وضعیت کانفیگ",
        f"🗑 <b>حذف:</b> حذف کانفیگ با تایید",
        f"🗑 <b>حذف گروهی:</b> حذف همه کانفیگ‌های غیرفعال",
        "",
        f"{_separator()}",
        f"<b>📊 اطلاعات نمایشی:</b>",
        f"{_separator()}",
        "",
        f"🟢 کانفیگ فعال",
        f"🔴 کانفیگ غیرفعال/منقضی",
        f"🟡 انقضا نزدیک (≤۳ روز)",
        f"⏰ منقضی‌شونده (≤۷ روز)",
        "",
        f"█░ نوار پیشرفت مصرف",
        f"🟢 کمتر از ۵۰٪  |  🟡 ۵۰-۸۰٪  |  🔴 بیشتر از ۸۰٪",
    ]

    return "\n".join(lines)

# ── Update handling ────────────────────────────────────────────────────────────
async def _handle_message(msg: dict):
    chat_id = msg.get("chat", {}).get("id")
    text = (msg.get("text") or "").strip()
    if chat_id is None:
        return
    if not _is_admin(chat_id):
        await _send(chat_id, "⛔ شما اجازه‌ی دسترسی به این ربات رو ندارید.")
        return

    if text in ("/start", "/menu"):
        _pending.pop(chat_id, None)
        welcome = (
            f"{_box_header('🛡️ X4G ربات مدیریت')}\n\n"
            "👋 خوش اومدی!\n"
            "از دکمه‌های زیر استفاده کن:"
        )
        await _send(chat_id, welcome, _main_menu_kb())
        return

    if text == "/cancel":
        _pending.pop(chat_id, None)
        await _send(chat_id, "❌ عملیات لغو شد.", _main_menu_kb())
        return

    if text == "/stats":
        _pending.pop(chat_id, None)
        await _send(chat_id, _format_stats(), _stats_kb())
        return

    if text.startswith("/search"):
        _pending.pop(chat_id, None)
        query = text.replace("/search", "").strip()
        if not query:
            _pending[chat_id] = {"action": "search_input"}
            await _send(chat_id, "🔍 عبارت مورد جستجو رو تایپ کن:", _main_menu_kb())
            return
        _do_search(chat_id, query)
        return

    if text == "/export":
        _pending.pop(chat_id, None)
        await _send(chat_id, _format_export(), _export_done_kb())
        return

    if text == "/help":
        _pending.pop(chat_id, None)
        await _send(chat_id, _format_help(), _help_kb())
        return

    pending = _pending.get(chat_id)

    # Handle search text input
    if pending and pending.get("action") == "search_input" and text:
        _pending.pop(chat_id, None)
        _do_search(chat_id, text)
        return

    if pending and pending.get("action") == "wizard" and text:
        step = pending["step"]
        data = pending["data"]

        if step == "label":
            data["label"] = text[:60] or "کانفیگ جدید"
            pending["step"] = "protocol"
            await _send(chat_id, _wizard_prompt("protocol", data), _wizard_protocol_kb())
            return

        if step in ("protocol", "fingerprint"):
            kb = _wizard_protocol_kb() if step == "protocol" else _wizard_fp_kb()
            await _send(chat_id, "لطفاً از دکمه‌های بالا یکی رو انتخاب کن 👆", kb)
            return

        if step == "alpn":
            data["alpn"] = text.strip()[:100]
            pending["step"] = "port"
            await _send(chat_id, _wizard_prompt("port", data), _wizard_skip_kb("port", f"⏭ پیش‌فرض ({DEFAULT_PORT})"))
            return

        if step == "port":
            try:
                p = int(text.strip())
            except ValueError:
                p = None
            if p is None or not (MIN_PORT <= p <= MAX_PORT):
                await _send(chat_id, f"❗️ عدد پورت نامعتبره. یه عدد بین {MIN_PORT} تا {MAX_PORT} بفرست:\n💡 یا پیش‌فرض ({DEFAULT_PORT}) رو انتخاب کن.", _wizard_skip_kb("port", f"⏭ پیش‌فرض ({DEFAULT_PORT})"))
                return
            data["port"] = p
            pending["step"] = "volume"
            await _send(chat_id, _wizard_prompt("volume", data), _wizard_unlimited_kb("volume"))
            return

        if step == "volume":
            parsed = _parse_volume_text(text)
            if parsed is None:
                await _send(chat_id, "❗️ فرمت درست نیست. مثلاً بفرست: <code>10GB</code> یا <code>500MB</code>\n💡 فرمت صحیح: عدد + واحد (GB/MB/KB)", _wizard_unlimited_kb("volume"))
                return
            data["limit_bytes"] = parsed
            pending["step"] = "speed"
            await _send(chat_id, _wizard_prompt("speed", data), _wizard_unlimited_kb("speed"))
            return

        if step == "speed":
            parsed = _parse_speed_text(text)
            if parsed is None:
                await _send(chat_id, "❗️ فرمت درست نیست. یه عدد بفرست، مثلاً <code>20</code> (Mbps)\n💡 فرمت صحیح: عدد + واحد اختیاری (Mbit/MBps)", _wizard_unlimited_kb("speed"))
                return
            data["speed_limit_bytes"] = parsed
            pending["step"] = "iplimit"
            await _send(chat_id, _wizard_prompt("iplimit", data), _wizard_unlimited_kb("iplimit"))
            return

        if step == "iplimit":
            n = _parse_nonneg_int(text)
            if n is None:
                await _send(chat_id, "❗️ یه عدد صحیح بفرست:\n💡 مثلاً: ۱, ۲, ۵ و غیره", _wizard_unlimited_kb("iplimit"))
                return
            data["ip_limit"] = n
            pending["step"] = "days"
            await _send(chat_id, _wizard_prompt("days", data), _wizard_unlimited_kb("days"))
            return

        if step == "days":
            n = _parse_nonneg_int(text)
            if n is None:
                await _send(chat_id, "❗️ یه عدد صحیح بفرست (تعداد روز):\n💡 مثلاً: ۳۰ (روز)", _wizard_unlimited_kb("days"))
                return
            data["expires_days"] = n
            pending["step"] = "confirm"
            await _send(chat_id, _wizard_summary(data), _wizard_confirm_kb())
            return

    # Unknown message → show menu
    await _send(chat_id, "👆 از دکمه‌های زیر استفاده کن:", _main_menu_kb())

def _do_search(chat_id: int, query: str):
    """Search configs by label name."""
    q = query.lower()
    results = [(uid, l) for uid, l in LINKS.items() if q in l.get("label", "").lower()]

    if not results:
        msg = (
            f"🔍 نتیجه‌ای برای «<b>{query}</b>» پیدا نشد.\n\n"
            "💡 <i>نکته: جستجو بر اساس نام برچسب انجام می‌شه.</i>"
        )
        _pending[chat_id] = {"action": "search_input"}
        # Can't use await here, need to schedule
        asyncio.ensure_future(_send(chat_id, msg, _main_menu_kb()))
        return

    per_page = 5
    total_pages = math.ceil(len(results) / per_page)

    header = (
        f"🔍 <b>نتایج جستجو:</b> «<b>{query}</b>»\n"
        f"تعداد: <b>{len(results)}</b> مورد | صفحه ۱/{total_pages}\n"
        f"{_separator()}"
    )
    asyncio.ensure_future(_send(chat_id, header, _search_results_kb(query, results, 0)))

async def _handle_callback(cb: dict):
    chat_id = cb.get("message", {}).get("chat", {}).get("id")
    message_id = cb.get("message", {}).get("message_id")
    data = cb.get("data", "")
    cb_id = cb.get("id")

    if chat_id is None or not _is_admin(chat_id):
        await _answer_cb(cb_id, "⛔ دسترسی نداری")
        return
    await _answer_cb(cb_id)

    # ── Menu ──────────────────────────────────────────────────────────────
    if data == "menu":
        _pending.pop(chat_id, None)
        welcome = (
            f"{_box_header('🛡️ X4G ربات مدیریت')}\n\n"
            "👋 خوش اومدی!\n"
            "از دکمه‌های زیر استفاده کن:"
        )
        await _edit(chat_id, message_id, welcome, _main_menu_kb())
        return

    # ── Stats ─────────────────────────────────────────────────────────────
    if data == "stats":
        await _edit(chat_id, message_id, _format_stats(), _stats_kb())
        return

    # ── Help ──────────────────────────────────────────────────────────────
    if data == "help":
        await _edit(chat_id, message_id, _format_help(), _help_kb())
        return

    # ── Export ────────────────────────────────────────────────────────────
    if data == "export":
        await _edit(chat_id, message_id, _format_export(), _export_done_kb())
        return

    # ── Search ask ────────────────────────────────────────────────────────
    if data == "searchask":
        _pending[chat_id] = {"action": "search_input"}
        await _edit(chat_id, message_id, "🔍 عبارت مورد جستجو رو تایپ کن:", _main_menu_kb())
        return

    # ── Search pagination ─────────────────────────────────────────────────
    if data.startswith("searchpage:"):
        parts = data.split(":", 2)
        query = parts[1] if len(parts) > 1 else ""
        page = int(parts[2]) if len(parts) > 2 else 0
        q = query.lower()
        results = [(uid, l) for uid, l in LINKS.items() if q in l.get("label", "").lower()]
        per_page = 5
        total_pages = max(1, math.ceil(len(results) / per_page))
        header = (
            f"🔍 <b>نتایج جستجو:</b> «<b>{query}</b>»\n"
            f"تعداد: <b>{len(results)}</b> مورد | صفحه {page+1}/{total_pages}\n"
            f"{_separator()}"
        )
        await _edit(chat_id, message_id, header, _search_results_kb(query, results, page))
        return

    # ── Bulk delete inactive ──────────────────────────────────────────────
    if data == "delall_inactive":
        inactive_count = sum(1 for l in LINKS.values() if not l.get("active", True))
        if inactive_count == 0:
            await _edit(chat_id, message_id, "✅ هیچ کانفیگ غیرفعالی وجود نداره.", _main_menu_kb())
            return
        await _edit(
            chat_id, message_id,
            f"⚠️ <b>حذف گروهی کانفیگ‌های غیرفعال</b>\n\n"
            f"تعداد: <b>{inactive_count}</b> کانفیگ\n"
            f"آیا از حذف همه‌ی کانفیگ‌های غیرفعال مطمئنی؟\n\n"
            f"❗️ <i>این عمل برگشت‌ناپذیره.</i>",
            _confirm_bulk_delete_kb()
        )
        return

    if data == "delall_confirm":
        to_delete = [uid for uid, l in LINKS.items() if not l.get("active", True)]
        deleted = 0
        for uid in to_delete:
            label = await remove_link(uid)
            if label is not None:
                deleted += 1
        await _edit(
            chat_id, message_id,
            f"🗑 <b>{deleted}</b> کانفیگ غیرفعال حذف شد.",
            _main_menu_kb()
        )
        return

    # ── Config list ───────────────────────────────────────────────────────
    if data.startswith("list:"):
        page = int(data.split(":", 1)[1] or 0)
        if not LINKS:
            await _edit(chat_id, message_id,
                f"{_box_header('📋 لیست کانفیگ‌ها')}\n\n"
                "📭 هنوز هیچ کانفیگی ساخته نشده.\n\n"
                "💡 از دکمه «➕ ساخت کانفیگ جدید» استفاده کن.",
                _main_menu_kb())
            return
        active_count = sum(1 for l in LINKS.values() if is_link_allowed(l))
        await _edit(chat_id, message_id,
            f"📋 <b>لیست کانفیگ‌ها</b>\n"
            f"تعداد: {len(LINKS)} | فعال: {active_count} | غیرفعال: {len(LINKS) - active_count}\n"
            f"{_separator()}",
            _links_list_kb(page))
        return

    # ── New config wizard ─────────────────────────────────────────────────
    if data == "newcfg":
        _pending[chat_id] = {"action": "wizard", "step": "label", "data": {}}
        await _edit(chat_id, message_id, _wizard_prompt("label", {}), _wizard_cancel_kb())
        return

    if data == "w:cancel":
        _pending.pop(chat_id, None)
        await _edit(chat_id, message_id, "❌ ساخت کانفیگ لغو شد.", _main_menu_kb())
        return

    if data.startswith("w:"):
        pending = _pending.get(chat_id)
        if not pending or pending.get("action") != "wizard":
            await _edit(chat_id, message_id, "⚠️ این مرحله دیگه معتبر نیست، از منوی زیر دوباره شروع کن.", _main_menu_kb())
            return

        step = pending["step"]
        wdata = pending["data"]

        if data.startswith("w:proto:") and step == "protocol":
            proto = data.split(":", 2)[2]
            wdata["protocol"] = proto if proto in PROTOCOLS else DEFAULT_PROTOCOL
            pending["step"] = "fingerprint"
            await _edit(chat_id, message_id, _wizard_prompt("fingerprint", wdata), _wizard_fp_kb())
            return

        if data.startswith("w:fp:") and step == "fingerprint":
            fp = data.split(":", 2)[2]
            wdata["fingerprint"] = fp if fp in FINGERPRINTS else DEFAULT_FINGERPRINT
            pending["step"] = "alpn"
            await _edit(chat_id, message_id, _wizard_prompt("alpn", wdata), _wizard_alpn_kb())
            return

        if data.startswith("w:alpnpreset:") and step == "alpn":
            code = data.split(":", 2)[2]
            wdata["alpn"] = ALPN_PRESET_MAP.get(code, "")
            pending["step"] = "port"
            await _edit(chat_id, message_id, _wizard_prompt("port", wdata), _wizard_skip_kb("port", f"⏭ پیش‌فرض ({DEFAULT_PORT})"))
            return

        if data == "w:skip:alpn" and step == "alpn":
            wdata["alpn"] = ""
            pending["step"] = "port"
            await _edit(chat_id, message_id, _wizard_prompt("port", wdata), _wizard_skip_kb("port", f"⏭ پیش‌فرض ({DEFAULT_PORT})"))
            return

        if data == "w:skip:port" and step == "port":
            wdata["port"] = DEFAULT_PORT
            pending["step"] = "volume"
            await _edit(chat_id, message_id, _wizard_prompt("volume", wdata), _wizard_unlimited_kb("volume"))
            return

        if data == "w:skip:volume" and step == "volume":
            wdata["limit_bytes"] = 0
            pending["step"] = "speed"
            await _edit(chat_id, message_id, _wizard_prompt("speed", wdata), _wizard_unlimited_kb("speed"))
            return

        if data == "w:skip:speed" and step == "speed":
            wdata["speed_limit_bytes"] = 0
            pending["step"] = "iplimit"
            await _edit(chat_id, message_id, _wizard_prompt("iplimit", wdata), _wizard_unlimited_kb("iplimit"))
            return

        if data == "w:skip:iplimit" and step == "iplimit":
            wdata["ip_limit"] = 0
            pending["step"] = "days"
            await _edit(chat_id, message_id, _wizard_prompt("days", wdata), _wizard_unlimited_kb("days"))
            return

        if data == "w:skip:days" and step == "days":
            wdata["expires_days"] = 0
            pending["step"] = "confirm"
            await _edit(chat_id, message_id, _wizard_summary(wdata), _wizard_confirm_kb())
            return

        if data == "w:confirm" and step == "confirm":
            expires_days = wdata.get("expires_days", 0)
            expires_at = (datetime.now() + timedelta(days=expires_days)).isoformat() if expires_days > 0 else None
            uid, link = await make_link(
                label=wdata.get("label") or "کانفیگ جدید",
                limit_bytes=wdata.get("limit_bytes", 0),
                expires_at=expires_at,
                protocol=wdata.get("protocol", DEFAULT_PROTOCOL),
                fingerprint=wdata.get("fingerprint", DEFAULT_FINGERPRINT),
                alpn=wdata.get("alpn", ""),
                port=wdata.get("port", DEFAULT_PORT),
                ip_limit=wdata.get("ip_limit", 0),
                speed_limit_bytes=wdata.get("speed_limit_bytes", 0),
            )
            _pending.pop(chat_id, None)
            await _edit(chat_id, message_id,
                f"✅ <b>کانفیگ ساخته شد!</b>\n\n{_format_detail(uid, link)}",
                _link_detail_kb(uid, link["active"]))
            return

        await _answer_cb(cb_id, "این دکمه دیگه معتبر نیست.")
        return

    # ── View config ───────────────────────────────────────────────────────
    if data.startswith("view:"):
        uid = data.split(":", 1)[1]
        l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "⚠️ این کانفیگ دیگه وجود نداره.", _main_menu_kb())
            return
        await _edit(chat_id, message_id, _format_detail(uid, l), _link_detail_kb(uid, l["active"]))
        return

    # ── Toggle active ─────────────────────────────────────────────────────
    if data.startswith("toggle:"):
        uid = data.split(":", 1)[1]
        l = await set_link_active(uid, not LINKS.get(uid, {}).get("active", True))
        if not l:
            await _edit(chat_id, message_id, "⚠️ این کانفیگ دیگه وجود نداره.", _main_menu_kb())
            return
        await _edit(chat_id, message_id, _format_detail(uid, l), _link_detail_kb(uid, l["active"]))
        return

    # ── Show link ─────────────────────────────────────────────────────────
    if data.startswith("link:"):
        uid = data.split(":", 1)[1]
        l = LINKS.get(uid)
        if not l:
            await _answer_cb(cb_id, "⚠️ کانفیگ پیدا نشد")
            return
        host = get_host()
        vless = vless_link_for_link(l, uid, host)
        sub_url = f"https://{host}/sub/{uid}"
        public_url = f"https://{host}/p/{uid}"
        msg = (
            f"{_box_header('🔗 لینک اتصال')}\n"
            f"📛 «{l.get('label')}»\n\n"
            f"<b>VLESS Link:</b>\n<code>{vless}</code>\n\n"
            f"<b>ساب ساده (متنی):</b>\n<code>{sub_url}</code>\n\n"
            f"<b>ساب حرفه‌ای (صفحه‌ی زیبا):</b>\n<code>{public_url}</code>"
        )
        await _send(chat_id, msg)
        return

    # ── Copy link (sends same as link but formatted for copying) ──────────
    if data.startswith("copy:"):
        uid = data.split(":", 1)[1]
        l = LINKS.get(uid)
        if not l:
            await _answer_cb(cb_id, "⚠️ کانفیگ پیدا نشد")
            return
        host = get_host()
        vless = vless_link_for_link(l, uid, host)
        await _send(chat_id,
            f"📋 <b>لینک کپی شد:</b>\n\n"
            f"<code>{vless}</code>\n\n"
            f"💡 <i>روی لینک بالا ضربه بزنید تا کپی بشه.</i>",
            _link_detail_kb(uid, l["active"]))
        return

    # ── Share link ────────────────────────────────────────────────────────
    if data.startswith("share:"):
        uid = data.split(":", 1)[1]
        l = LINKS.get(uid)
        if not l:
            await _answer_cb(cb_id, "⚠️ کانفیگ پیدا نشد")
            return
        host = get_host()
        vless = vless_link_for_link(l, uid, host)
        # Send a shareable message that can be forwarded
        await _send(chat_id,
            f"📤 <b>پیام قابل اشتراک‌گذاری:</b>\n\n"
            f"📛 <b>{l.get('label')}</b>\n"
            f"🔗 <code>{vless}</code>\n\n"
            f"💡 <i>این پیام رو به کسی که می‌خواد وصل بشه فوروارد کنید.</i>",
            _link_detail_kb(uid, l["active"]))
        return

    # ── Delete ────────────────────────────────────────────────────────────
    if data.startswith("del:"):
        uid = data.split(":", 1)[1]
        l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "⚠️ این کانفیگ دیگه وجود نداره.", _main_menu_kb())
            return
        await _edit(chat_id, message_id,
            f"❗️ <b>از حذف مطمئنی؟</b>\n\n"
            f"📛 «{l.get('label')}»\n"
            f"🆔 <code>{uid}</code>\n\n"
            f"⚠️ <i>این عمل برگشت‌ناپذیره.</i>",
            _confirm_delete_kb(uid))
        return

    if data.startswith("delok:"):
        uid = data.split(":", 1)[1]
        label = await remove_link(uid)
        if label is None:
            await _edit(chat_id, message_id, "⚠️ این کانفیگ قبلاً حذف شده بود.", _main_menu_kb())
        else:
            await _edit(chat_id, message_id,
                f"🗑 <b>کانفیگ حذف شد!</b>\n\n"
                f"📛 «{label}»",
                _main_menu_kb())
        return

# ── Polling loop ───────────────────────────────────────────────────────────────
async def _poll_loop():
    global _running
    offset = 0
    logger.info(f"🤖 Telegram bot polling started (admins: {len(ADMIN_IDS)})")
    while _running:
        try:
            res = await _call("getUpdates", offset=offset, timeout=30, allowed_updates=["message", "callback_query"])
            if not res or not res.get("ok"):
                await asyncio.sleep(3)
                continue
            for upd in res.get("result", []):
                offset = upd["update_id"] + 1
                try:
                    if "message" in upd:
                        await _handle_message(upd["message"])
                    elif "callback_query" in upd:
                        await _handle_callback(upd["callback_query"])
                except Exception as e:
                    logger.warning(f"Telegram update handling error: {e}")
        except asyncio.CancelledError:
            break
        except Exception as e:
            logger.warning(f"Telegram poll loop error: {e}")
            await asyncio.sleep(3)

# ── Lifecycle ──────────────────────────────────────────────────────────────────
async def start_bot():
    global _client, _poll_task, _running
    if not BOT_TOKEN:
        logger.info("Telegram bot: TELEGRAM_BOT_TOKEN تنظیم نشده، ربات غیرفعاله.")
        return
    if not ADMIN_IDS:
        logger.warning("Telegram bot: TELEGRAM_ADMIN_IDS تنظیم نشده، هیچ‌کس اجازه‌ی مدیریت نداره (ربات روشنه ولی همه رد می‌شن).")
    _client = httpx.AsyncClient(timeout=httpx.Timeout(40.0, connect=10.0))
    _running = True
    _poll_task = asyncio.create_task(_poll_loop())

async def stop_bot():
    global _running, _client
    _running = False
    if _poll_task:
        _poll_task.cancel()
    if _client:
        await _client.aclose()
        _client = None
