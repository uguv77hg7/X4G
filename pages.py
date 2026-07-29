# pages.py  -  X4G v9.8
# Modern Dark Neon Redesign

# لوگوی X4G
LOGO_B64 = "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"



LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · X4G</title>
<meta name="theme-color" content="#0F0B1A">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="/manifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0A0A0A;--bg2:#111111;--card:rgba(17,17,17,0.95);--card-b:rgba(212,175,55,0.2);--card-bh:rgba(212,175,55,0.5);--accent:#D4AF37;--accent2:#FFD700;--accent3:#B8860B;--cyan:#D4AF37;--green:#22C55E;--red:#EF4444;--red-bg:rgba(239,68,68,0.1);--t1:#FFFFFF;--t2:#B0B0B0;--t3:#666666}
[data-theme="light"]{--bg:#F5F0E0;--bg2:#EDE5D0;--card:rgba(255,255,255,0.95);--card-b:rgba(180,130,30,0.2);--card-bh:rgba(180,130,30,0.4);--accent:#B8860B;--accent2:#8B6914;--accent3:#D4AF37;--t1:#1A1A1A;--t2:#555555;--t3:#888888}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px;position:relative}
.aurora{position:fixed;inset:0;z-index:0;overflow:hidden}
.aurora::before,.aurora::after{content:'';position:absolute;border-radius:50%;filter:blur(100px);animation:drift 20s ease-in-out infinite}
.aurora::before{width:600px;height:600px;background:radial-gradient(circle,rgba(212,175,55,0.08),transparent 70%);top:-200px;right:-150px}
.aurora::after{width:500px;height:500px;background:radial-gradient(circle,rgba(184,134,11,0.06),transparent 70%);bottom:-200px;left:-150px;animation-delay:-10s}
@keyframes drift{0%,100%{transform:translate(0,0) scale(1)}25%{transform:translate(40px,-30px) scale(1.05)}50%{transform:translate(-20px,40px) scale(0.95)}75%{transform:translate(30px,20px) scale(1.02)}}
.stars{position:fixed;inset:0;z-index:0}
.star{position:absolute;width:2px;height:2px;background:#FFD700;border-radius:50%;animation:twinkle var(--d,3s) ease-in-out infinite var(--dl,0s);opacity:0}
@keyframes twinkle{0%,100%{opacity:0;transform:scale(0.5)}50%{opacity:var(--o,0.6);transform:scale(1)}}
.ring{position:fixed;border-radius:50%;border:1px solid;opacity:0;animation:ringFloat 15s ease-in-out infinite var(--dl,0s);z-index:0;pointer-events:none}
@keyframes ringFloat{0%{transform:translateY(100vh) rotate(0deg);opacity:0}10%{opacity:var(--o,0.15)}90%{opacity:var(--o,0.15)}100%{transform:translateY(-100px) rotate(360deg);opacity:0}}
.wrap{position:relative;z-index:10;width:100%;max-width:420px}
.card{position:relative;background:var(--card);backdrop-filter:blur(40px) saturate(1.5);-webkit-backdrop-filter:blur(40px) saturate(1.5);border:1px solid rgba(212,175,55,0.2);border-radius:28px;padding:44px 36px 36px;overflow:hidden;transition:all .4s cubic-bezier(.4,0,.2,1)}
.card::before{content:'';position:absolute;top:-1px;left:20%;right:20%;height:1px;background:linear-gradient(90deg,transparent,#D4AF37,transparent);opacity:0;transition:opacity .4s}
.card:hover::before{opacity:1}
.card::after{content:'';position:absolute;inset:-1px;border-radius:28px;padding:1px;background:linear-gradient(135deg,rgba(212,175,55,0.3),transparent 40%,transparent 60%,rgba(184,134,11,0.2));-webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;opacity:0;transition:opacity .4s}
.card:hover::after{opacity:1}
.glow-tl{position:absolute;top:-60px;left:-60px;width:180px;height:180px;background:radial-gradient(circle,rgba(212,175,55,0.12),transparent 70%);border-radius:50%;filter:blur(40px);animation:pulse 4s ease-in-out infinite;pointer-events:none}
.glow-br{position:absolute;bottom:-60px;right:-60px;width:160px;height:160px;background:radial-gradient(circle,rgba(184,134,11,0.08),transparent 70%);border-radius:50%;filter:blur(40px);animation:pulse 4s ease-in-out infinite 2s;pointer-events:none}
@keyframes pulse{0%,100%{opacity:.6;transform:scale(1)}50%{opacity:1;transform:scale(1.1)}}
.logo-section{display:flex;flex-direction:column;align-items:center;margin-bottom:32px;position:relative}
.logo-ring{width:88px;height:88px;border-radius:50%;padding:3px;background:conic-gradient(from 0deg,#D4AF37,#FFD700,#B8860B,#D4AF37);animation:logoSpin 8s linear infinite;position:relative}
@keyframes logoSpin{to{transform:rotate(360deg)}}
.logo-inner{width:100%;height:100%;border-radius:50%;background:var(--bg);display:flex;align-items:center;justify-content:center;position:relative}
.logo-inner img{width:60px;height:60px;border-radius:50%;object-fit:cover}
.logo-pulse{position:absolute;inset:-8px;border-radius:50%;border:1px solid rgba(212,175,55,0.3);animation:logoPulse 2s ease-in-out infinite}
@keyframes logoPulse{0%,100%{transform:scale(1);opacity:.3}50%{transform:scale(1.15);opacity:0}}
.logo-text{margin-top:16px;text-align:center}
.logo-title{font-size:28px;font-weight:900;background:linear-gradient(135deg,#D4AF37,#FFD700,#B8860B);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;letter-spacing:-.03em;line-height:1.2}
.logo-ver{font-size:11px;color:var(--t3);margin-top:4px;font-weight:500;letter-spacing:.1em}
.heading{text-align:center;margin-bottom:28px}
.heading h1{font-size:22px;font-weight:700;color:var(--t1);margin-bottom:8px;letter-spacing:-.02em}
.heading p{font-size:13px;color:var(--t2);line-height:1.7}
.hint{display:flex;align-items:center;gap:10px;background:rgba(212,175,55,0.06);border:1px solid rgba(212,175,55,0.15);border-radius:14px;padding:11px 14px;margin-bottom:24px;transition:all .3s}
.hint:hover{background:rgba(212,175,55,0.1);border-color:rgba(212,175,55,0.3)}
.hint-label{font-size:11px;color:var(--t3);flex:1}
.hint-val{font-family:'SF Mono',ui-monospace,monospace;font-size:13px;font-weight:700;color:var(--accent);background:rgba(212,175,55,0.08);border:1px solid rgba(212,175,55,0.2);padding:4px 12px;border-radius:8px;cursor:pointer;transition:all .2s;letter-spacing:.06em}
.hint-val:hover{background:rgba(212,175,55,0.15);transform:scale(1.05)}
.field{margin-bottom:22px}
.field label{display:block;font-size:11px;font-weight:600;color:var(--t2);margin-bottom:8px;text-transform:uppercase;letter-spacing:.08em}
.inp-wrap{position:relative}
.inp-wrap input{width:100%;padding:15px 48px 15px 18px;border-radius:14px;border:1.5px solid rgba(212,175,55,0.12);background:rgba(6,10,20,0.6);color:var(--t1);font-family:inherit;font-size:14px;outline:none;transition:all .3s;backdrop-filter:blur(10px)}
.inp-wrap input:focus{border-color:var(--accent);background:rgba(6,10,20,0.8);box-shadow:0 0 0 4px rgba(212,175,55,0.1),0 0 30px rgba(212,175,55,0.05)}
.inp-wrap input::placeholder{color:var(--t3)}
.inp-wrap .ic{position:absolute;left:16px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:18px;pointer-events:none;transition:all .3s}
.inp-wrap input:focus~.ic{color:var(--accent);filter:drop-shadow(0 0 6px rgba(212,175,55,0.5))}
.inp-line{position:absolute;bottom:0;left:50%;width:0;height:2px;background:linear-gradient(90deg,#D4AF37,#FFD700);border-radius:1px;transition:all .3s;transform:translateX(-50%)}
.inp-wrap input:focus~.inp-line{width:calc(100% - 32px)}
.err{display:none;background:var(--red-bg);border:1px solid rgba(248,113,113,0.15);border-radius:12px;padding:11px 14px;margin-bottom:16px;font-size:12px;color:var(--red);align-items:center;gap:8px;animation:shake .4s ease-in-out}
.err.show{display:flex}
@keyframes shake{0%,100%{transform:translateX(0)}20%{transform:translateX(-8px)}40%{transform:translateX(8px)}60%{transform:translateX(-4px)}80%{transform:translateX(4px)}}
.btn-wrap{position:relative}
.btn{width:100%;padding:15px;border-radius:14px;border:none;cursor:pointer;background:linear-gradient(135deg,#D4AF37,#FFD700,#B8860B);color:#fff;font-family:inherit;font-size:15px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:10px;position:relative;overflow:hidden;transition:all .3s;box-shadow:0 4px 24px rgba(212,175,55,0.3)}
.btn::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.15),transparent);transition:left .5s}
.btn:hover::before{left:100%}
.btn:hover{transform:translateY(-2px);box-shadow:0 8px 32px rgba(212,175,55,0.4)}
.btn:active{transform:translateY(0) scale(.98)}
.btn:disabled{opacity:.5;cursor:not-allowed;transform:none}
.btn .spinner{display:none;width:18px;height:18px;border:2px solid rgba(255,255,255,0.3);border-top-color:#fff;border-radius:50%;animation:spin .6s linear infinite}
.btn.loading .btn-text{display:none}
.btn.loading .spinner{display:block}
@keyframes spin{to{transform:rotate(360deg)}}
.footer{margin-top:28px;padding-top:20px;border-top:1px solid rgba(212,175,55,0.1);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11px;color:var(--t3)}
.footer a{color:var(--accent);font-weight:600;text-decoration:none;display:flex;align-items:center;gap:5px;transition:color .2s}
.footer a:hover{color:var(--cyan)}
.theme-btn{position:fixed;top:20px;left:20px;z-index:20;width:40px;height:40px;border-radius:12px;border:1px solid rgba(212,175,55,0.2);background:var(--card);backdrop-filter:blur(20px);color:var(--t2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:18px;transition:all .3s}
.theme-btn:hover{border-color:var(--accent);color:var(--accent);transform:rotate(30deg)}
@media(max-width:480px){.card{padding:36px 24px 28px;border-radius:24px}.logo-ring{width:76px;height:76px}.logo-inner img{width:50px;height:50px}.logo-title{font-size:24px}}
</style>
</head>
<body>
<div class="aurora"></div>
<div class="stars" id="stars"></div>
<div class="ring" style="width:60px;height:60px;border-color:rgba(212,175,55,0.15);left:10%;--dl:0s;--o:0.12"></div>
<div class="ring" style="width:40px;height:40px;border-color:rgba(212,175,55,0.12);left:70%;--dl:4s;--o:0.1"></div>
<div class="ring" style="width:80px;height:80px;border-color:rgba(184,134,11,0.1);left:40%;--dl:8s;--o:0.08"></div>
<div class="ring" style="width:30px;height:30px;border-color:rgba(212,175,55,0.1);left:85%;--dl:12s;--o:0.1"></div>
<button class="theme-btn" id="theme-toggle" onclick="toggleTheme()"><i class="ti ti-moon"></i></button>
<div class="wrap">
  <div class="card">
    <div class="glow-tl"></div>
    <div class="glow-br"></div>
    <div class="logo-section">
      <div class="logo-ring">
        <div class="logo-inner">
          <div class="logo-pulse"></div>
          <img src="data:image/png;base64,__LOGO_B64__" alt="X4G">
        </div>
      </div>
      <div class="logo-text">
        <div class="logo-title">X4G Panel</div>
        <div class="logo-ver">AURORA EDITION · v9.8</div>
      </div>
    </div>
    <div class="heading">
      <h1>خوش آمدید</h1>
      <p>برای دسترسی به داشبورد، رمز عبور را وارد کنید</p>
    </div>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="hint">
      <span class="hint-label">رمز پیش‌فرض</span>
      <span class="hint-val" onclick="document.getElementById('pw').value='X4GKING';document.getElementById('pw').focus()">X4GKING</span>
    </div>
    <form id="form">
      <div class="field">
        <label>رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="رمز عبور خود را وارد کنید" autofocus required>
          <i class="ti ti-key ic"></i>
          <div class="inp-line"></div>
        </div>
      </div>
      <div class="field" id="totp-field" style="display:none">
        <label>کد ۲ عاملی</label>
        <div class="inp-wrap">
          <input type="text" id="totp" placeholder="کد ۶ رقمی را وارد کنید" maxlength="6" pattern="\d{6}" inputmode="numeric">
          <i class="ti ti-shield-lock ic"></i>
          <div class="inp-line"></div>
        </div>
      </div>
      <div class="err" id="lockout" style="display:none;background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.15);color:#F59E0B">
        <i class="ti ti-clock"></i>
        <span id="lockout-text"></span>
      </div>
      <div class="btn-wrap">
        <button class="btn" type="submit" id="btn">
          <span class="btn-text"><i class="ti ti-login-2"></i> ورود به داشبورد</span>
          <div class="spinner"></div>
        </button>
      </div>
    </form>
    <div class="footer">پشتیبانی <a href="https://t.me/X4GHUB" target="_blank"><i class="ti ti-brand-telegram"></i> @X4GHUB</a></div>
  </div>
</div>
<script>
(function(){const c=document.getElementById('stars');for(let i=0;i<50;i++){const s=document.createElement('div');s.className='star';s.style.cssText='left:'+Math.random()*100+'%;top:'+Math.random()*100+'%;--d:'+(2+Math.random()*4)+'s;--dl:'+Math.random()*5+'s;--o:'+(0.2+Math.random()*0.5);c.appendChild(s);}})();
function toggleTheme(){const t=document.documentElement;const b=document.querySelector('.theme-btn i');if(t.getAttribute('data-theme')==='light'){t.removeAttribute('data-theme');b.className='ti ti-moon';}else{t.setAttribute('data-theme','light');b.className='ti ti-sun';}}
let _lockoutTimer=null;function _startLockout(secs){const lo=document.getElementById('lockout'),lt=document.getElementById('lockout-text');lo.style.display='flex';if(_lockoutTimer)clearInterval(_lockoutTimer);let rem=secs;lt.textContent='حساب شما موقتاً مسدود شد. '+rem+' ثانیه باقی‌مانده';_lockoutTimer=setInterval(()=>{rem--;if(rem<=0){clearInterval(_lockoutTimer);lo.style.display='none';document.getElementById('btn').disabled=false;}else{lt.textContent='حساب شما موقتاً مسدود شد. '+rem+' ثانیه باقی‌مانده';}},1000);}
document.getElementById('form').addEventListener('submit',async e=>{e.preventDefault();const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');err.classList.remove('show');btn.classList.add('loading');btn.disabled=true;try{const body={password:document.getElementById('pw').value};const totpField=document.getElementById('totp');if(totpField.offsetParent!==null)body.totp_code=totpField.value;const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});const d=await r.json().catch(()=>({}));if(r.status===200&&d.need_totp){document.getElementById('totp-field').style.display='block';document.getElementById('totp').focus();btn.classList.remove('loading');btn.disabled=false;return;}if(r.status===429){const match=d.detail.match(/(\d+)/);if(match)_startLockout(parseInt(match[1]));btn.classList.remove('loading');btn.disabled=true;return;}if(!r.ok)throw new Error(d.detail||'خطا');location.href='/dashboard';}catch(e){et.textContent=e.message;err.classList.add('show');btn.classList.remove('loading');btn.disabled=false;}});
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js').catch(function(e){});}
</script>
</body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>X4G</title>
<meta name="theme-color" content="#0F0B1A">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="/manifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
--bg:#0F0B1A;--bg2:#1A1428;--bg3:#241E34;
--card:rgba(20,15,35,0.95);--card-b:rgba(139,92,246,0.15);--card-bh:rgba(139,92,246,0.4);
--accent:#8B5CF6;--accent2:#A78BFA;--accent-d:rgba(139,92,246,0.1);
--cyan:#06B6D4;--cyan-d:rgba(6,182,212,0.1);
--blue:#3B82F6;--blue-bg:rgba(59,130,246,0.1);
--green:#10B981;--green-bg:rgba(16,185,129,0.1);
--amber:#F59E0B;--amber-bg:rgba(245,158,11,0.1);
--red:#EF4444;--red-bg:rgba(239,68,68,0.1);
--purple:#A855F7;--purple-bg:rgba(168,85,247,0.1);
--t1:#FFFFFF;--t2:#B0A0C8;--t3:#6B5B80;
--green-t:#34D399;--red-t:#FF7777;--amber-t:#FFCC33;--purple-t:#C084FC;
--radius:16px;
--shadow:0 4px 24px rgba(0,0,0,0.5);
--glass-b:rgba(139,92,246,0.12);
--nav-h:60px;
--grad-border:linear-gradient(135deg,#8B5CF6,#06B6D4);
}
[data-theme="light"]{
--bg:#F0ECF8;--bg2:#E8E2F2;--bg3:#DDD6EB;
--card:rgba(255,255,255,0.95);--card-b:rgba(139,92,246,0.12);--card-bh:rgba(139,92,246,0.25);
--accent:#7C3AED;--accent2:#A78BFA;--accent-d:rgba(124,58,237,0.08);
--cyan:#0891B2;--cyan-d:rgba(8,145,178,0.08);
--blue:#2563EB;--blue-bg:rgba(37,99,235,0.08);
--green:#059669;--green-bg:rgba(5,150,105,0.08);--green-t:#059669;
--amber:#D97706;--amber-bg:rgba(217,119,6,0.08);--amber-t:#D97706;
--red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#DC2626;
--purple:#7C3AED;--purple-bg:rgba(124,58,237,0.08);--purple-t:#7C3AED;
--t1:#0F172A;--t2:#475569;--t3:#94A3B8;
--shadow:0 4px 20px rgba(0,0,0,0.08);
--glass-b:rgba(124,58,237,0.1);
}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;flex-direction:column;font-size:14px;transition:background .3s,color .3s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}

/* ─── ANIMATED BACKGROUND ─── */
.neon-bg{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.neon-orb{position:absolute;border-radius:50%;filter:blur(140px);animation:orbFloat 20s ease-in-out infinite;pointer-events:none}
.neon-orb-1{width:500px;height:500px;background:rgba(139,92,246,0.08);top:-200px;right:-150px}
.neon-orb-2{width:400px;height:400px;background:rgba(6,182,212,0.06);bottom:-150px;left:-100px;animation-delay:7s}
.neon-orb-3{width:350px;height:350px;background:rgba(168,85,247,0.05);top:40%;left:30%;animation-delay:3s}
@keyframes orbFloat{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(40px,-30px) scale(1.08)}66%{transform:translate(-30px,40px) scale(0.92)}}
#particles-canvas{position:fixed;inset:0;z-index:0;pointer-events:none}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
@keyframes fi{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes breathe{0%,100%{transform:scale(1);opacity:.5}50%{transform:scale(1.08);opacity:0}}
@keyframes breathe2{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.12);opacity:0}}
@keyframes glowPulse{0%,100%{box-shadow:0 0 20px rgba(139,92,246,0.1)}50%{box-shadow:0 0 40px rgba(139,92,246,0.25)}}
@keyframes slideIn{from{opacity:0;transform:scale(.92)}to{opacity:1;transform:scale(1)}}
@keyframes gradientShift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@keyframes countUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}
@keyframes feedSlide{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}

/* ─── TOP NAVBAR ─── */
.topnav{position:fixed;top:0;left:0;right:0;height:var(--nav-h);background:rgba(15,11,26,0.92);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border-bottom:1px solid var(--card-b);display:flex;align-items:center;justify-content:space-between;padding:0 24px;z-index:200;transition:background .3s}
[data-theme="light"] .topnav{background:rgba(240,236,248,0.92)}
.tn-right{display:flex;align-items:center;gap:12px}
.tn-logo{display:flex;align-items:center;gap:10px;cursor:pointer}
.tn-logo-img{width:36px;height:36px;border-radius:11px;overflow:hidden;border:1.5px solid var(--accent);box-shadow:0 0 16px rgba(139,92,246,0.3);transition:.3s}
.tn-logo-img:hover{box-shadow:0 0 24px rgba(139,92,246,0.5);transform:scale(1.05)}
.tn-logo-img img{width:100%;height:100%;object-fit:cover}
.tn-brand{font-size:16px;font-weight:800;background:linear-gradient(135deg,#8B5CF6,#06B6D4);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.tn-center{display:flex;align-items:center;gap:4px}
.tn-link{display:flex;align-items:center;gap:6px;padding:8px 14px;border-radius:10px;font-size:12px;font-weight:600;color:var(--t3);cursor:pointer;transition:.25s;border:none;background:none;font-family:inherit;white-space:nowrap}
.tn-link i{font-size:15px}
.tn-link:hover{background:var(--accent-d);color:var(--t2)}
.tn-link.on{background:var(--accent);color:#fff;box-shadow:0 4px 16px rgba(139,92,246,0.35)}
.tn-badge{font-size:9px;padding:1px 6px;border-radius:20px;background:rgba(255,255,255,0.15);color:#fff;font-weight:700;margin-right:2px}
.tn-link:not(.on) .tn-badge{background:var(--accent-d);color:var(--accent)}
.tn-left{display:flex;align-items:center;gap:8px}
.tn-btn{display:flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:10px;border:1px solid var(--card-b);background:var(--accent-d);color:var(--t2);cursor:pointer;font-size:16px;transition:.3s}
.tn-btn:hover{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 4px 12px rgba(139,92,246,0.3)}
.tn-status{display:flex;align-items:center;gap:6px;padding:5px 12px;border-radius:50px;background:var(--green-bg);color:var(--green);font-size:10px;font-weight:700;border:1px solid rgba(16,185,129,0.15)}
.tn-status .dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite}
.tn-logout{background:var(--red-bg);color:var(--red);border:1px solid rgba(239,68,68,0.15);font-size:12px;font-weight:600;display:flex;align-items:center;gap:5px;padding:7px 14px;border-radius:50px;cursor:pointer;font-family:inherit;transition:.3s}
.tn-logout:hover{background:rgba(239,68,68,0.15);transform:translateY(-1px)}

/* ─── MOBILE NAV ─── */
.tn-mobile-btn{display:none;width:36px;height:36px;border-radius:10px;border:1px solid var(--card-b);background:var(--accent-d);color:var(--t2);cursor:pointer;font-size:18px;align-items:center;justify-content:center;transition:.3s}
.mobile-menu{display:none;position:fixed;top:var(--nav-h);left:0;right:0;background:rgba(15,11,26,0.98);backdrop-filter:blur(24px);border-bottom:1px solid var(--card-b);z-index:199;padding:12px 16px;flex-direction:column;gap:4px}
.mobile-menu.show{display:flex}
.mobile-menu .tn-link{width:100%;justify-content:flex-start;padding:12px 16px;border-radius:12px}
.mobile-menu .tn-logout{width:100%;justify-content:center;margin-top:8px}

/* ─── MAIN CONTENT ─── */
.main-wrap{flex:1;padding:calc(var(--nav-h) + 24px) 28px 60px;min-height:100vh;position:relative;z-index:1}
.pg{display:none}
.pg.on{display:block;animation:fi .25s ease}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:24px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:20px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:10px;letter-spacing:-.02em}
.tb-title i{color:var(--accent);font-size:22px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}

/* ─── STAT CARDS (horizontal row) ─── */
.stats-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:22px}
.stat-card{position:relative;background:var(--card);backdrop-filter:blur(20px);border:1px solid rgba(139,92,246,0.15);border-radius:var(--radius);padding:20px;transition:.3s;overflow:hidden;cursor:default}
.stat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--grad-border);opacity:0;transition:.3s}
.stat-card:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:0 12px 32px rgba(0,0,0,0.3),0 0 20px rgba(139,92,246,0.1)}
.stat-card:hover::before{opacity:1}
.stat-card-glow{position:absolute;top:-40px;right:-40px;width:120px;height:120px;border-radius:50%;filter:blur(40px);opacity:.15;pointer-events:none;transition:.3s}
.stat-card:hover .stat-card-glow{opacity:.3}
.stat-card-top{display:flex;align-items:center;gap:12px;margin-bottom:12px}
.stat-icon{width:42px;height:42px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:19px;transition:.3s}
.stat-card:hover .stat-icon{transform:scale(1.1);box-shadow:0 4px 16px rgba(139,92,246,0.3)}
.stat-icon.purple{background:var(--purple-bg);color:var(--purple)}
.stat-icon.cyan{background:var(--cyan-d);color:var(--cyan)}
.stat-icon.green{background:var(--green-bg);color:var(--green)}
.stat-icon.red{background:var(--red-bg);color:var(--red)}
.stat-icon.blue{background:var(--blue-bg);color:var(--blue)}
.stat-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.stat-val{font-size:28px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;display:flex;align-items:baseline;gap:4px}
.stat-unit{font-size:12px;font-weight:400;color:var(--t3)}
.stat-sub{font-size:10px;color:var(--t3);margin-top:7px;display:flex;align-items:center;gap:4px}
.stat-progress{height:4px;border-radius:3px;background:rgba(139,92,246,0.08);margin-top:8px;overflow:hidden}
.stat-progress-fill{height:100%;border-radius:3px;background:linear-gradient(90deg,#8B5CF6,#06B6D4);transition:width 1.2s cubic-bezier(.4,0,.2,1)}

/* ─── GRADIENT BORDER CARDS ─── */
.gcard{position:relative;background:var(--card);border-radius:var(--radius);padding:22px;transition:.3s;overflow:hidden;backdrop-filter:blur(20px)}
.gcard::before{content:'';position:absolute;inset:-1px;border-radius:var(--radius);padding:1px;background:linear-gradient(135deg,rgba(139,92,246,0.3),rgba(6,182,212,0.1),transparent);-webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;opacity:0;transition:opacity .4s}
.gcard:hover::before{opacity:1}
.gcard:hover{border-color:var(--card-bh);box-shadow:0 8px 32px rgba(0,0,0,0.2),0 0 20px rgba(139,92,246,0.06)}

/* ─── CARDS ─── */
.card{background:var(--card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid rgba(139,92,246,0.15);border-radius:var(--radius);padding:20px 22px;transition:border-color .3s,background .3s,box-shadow .3s}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:13px;font-weight:700;color:var(--t1);margin-bottom:16px;display:flex;align-items:center;gap:8px}
.card-title i{font-size:16px;color:var(--accent)}
.ml-auto{margin-right:auto}

/* ─── MAIN GRID (2-col) ─── */
.dash-grid{display:grid;grid-template-columns:1.5fr 1fr;gap:16px;margin-bottom:16px}
.dash-grid-bottom{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px}

/* ─── BADGES ─── */
.badge{font-size:10px;padding:4px 12px;border-radius:50px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green)}
.bg-blue{background:var(--blue-bg);color:var(--blue)}
.bg-amber{background:var(--amber-bg);color:var(--amber)}
.bg-red{background:var(--red-bg);color:var(--red)}
.bg-purple{background:var(--purple-bg);color:var(--purple)}
.bg-cyan{background:var(--cyan-d);color:var(--cyan)}
.dot{width:7px;height:7px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}

/* ─── SERVICE STATUS ROWS ─── */
.sr{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(139,92,246,0.06);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:7px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}

/* ─── PROGRESS BAR ─── */
.spbar{height:4px;border-radius:3px;background:rgba(139,92,246,0.08);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,#8B5CF6,#06B6D4);transition:width 1s}

/* ─── CHART CONTAINERS ─── */
.ch{position:relative;height:280px}
.ch-lg{position:relative;height:330px}
.ch-sm{position:relative;height:200px}

/* ─── QUICK ACTIONS ─── */
.quick-actions{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
.qa-btn{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;padding:18px 10px;border-radius:14px;border:1px solid rgba(139,92,246,0.12);background:rgba(0,0,0,.15);cursor:pointer;transition:.3s;font-family:inherit;color:var(--t2)}
[data-theme="light"] .qa-btn{background:rgba(139,92,246,0.03)}
.qa-btn:hover{border-color:var(--accent);background:var(--accent-d);color:var(--accent);transform:translateY(-3px);box-shadow:0 8px 24px rgba(139,92,246,0.15)}
.qa-icon{width:40px;height:40px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px;transition:.3s}
.qa-btn:hover .qa-icon{transform:scale(1.1);box-shadow:0 4px 12px rgba(139,92,246,0.3)}
.qa-icon.purple{background:var(--purple-bg);color:var(--purple)}
.qa-icon.cyan{background:var(--cyan-d);color:var(--cyan)}
.qa-icon.green{background:var(--green-bg);color:var(--green)}
.qa-icon.blue{background:var(--blue-bg);color:var(--blue)}
.qa-label{font-size:10px;font-weight:700;text-align:center}

/* ─── CONNECTION FEED ─── */
.feed-list{max-height:280px;overflow-y:auto;display:flex;flex-direction:column;gap:6px}
.feed-list::-webkit-scrollbar{width:3px}
.feed-list::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
.feed-item{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:10px;background:rgba(0,0,0,.12);border:1px solid rgba(139,92,246,0.08);font-size:11px;transition:.3s;animation:feedSlide .3s ease}
[data-theme="light"] .feed-item{background:rgba(139,92,246,0.03)}
.feed-item:hover{border-color:var(--accent);background:var(--accent-d)}
.feed-dot{width:6px;height:6px;border-radius:50%;background:var(--green);flex-shrink:0;animation:pulse 2s infinite}
.feed-ip{font-family:ui-monospace,monospace;font-size:11px;color:var(--t1);flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.feed-proto{font-size:9px;padding:2px 7px;border-radius:6px;font-weight:700;flex-shrink:0}
.feed-time{font-size:9px;color:var(--t3);flex-shrink:0}

/* ─── PROTO CHIPS ─── */
.proto-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;white-space:nowrap}
.pc-ws{background:var(--blue-bg);color:var(--blue)}
.pc-xhttp{background:var(--purple-bg);color:var(--purple)}
.pc-hy2{background:var(--amber-bg);color:var(--amber)}

/* ─── EXP CHIPS ─── */
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green)}
.ec-warn{background:var(--amber-bg);color:var(--amber)}
.ec-exp{background:var(--red-bg);color:var(--red)}
.ec-inf{background:var(--accent-d);color:var(--accent)}

/* ─── TOGGLE ─── */
.tog{width:20px;height:36px;border-radius:20px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.3s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:14px;height:14px;border-radius:50%;background:#8B5CF6;left:3px;bottom:3px;transition:.3s;box-shadow:0 1px 4px rgba(0,0,0,.3)}
.tog.on{background:var(--accent)}
.tog.on::after{bottom:19px}

/* ─── FORMS ─── */
.form-row{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:10px 13px;border-radius:10px;border:1px solid rgba(139,92,246,0.2);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.3s;min-width:100px}
[data-theme="light"] .fi,[data-theme="light"] .fs{background:rgba(0,0,0,.03)}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:var(--accent);background:rgba(0,0,0,.28);box-shadow:0 0 0 3px rgba(139,92,246,0.1)}
.fs option{background:var(--bg2)}

/* ─── BUTTONS ─── */
.btn{font-family:inherit;font-size:12px;font-weight:600;border-radius:50px;padding:9px 16px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:.3s;white-space:nowrap}
.btn i{font-size:13px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{background:linear-gradient(135deg,#8B5CF6,#06B6D4);color:#fff;box-shadow:0 4px 18px rgba(139,92,246,0.35)}
.btn-p:hover{box-shadow:0 8px 28px rgba(139,92,246,0.45);transform:translateY(-1px)}
.btn-o{background:transparent;border:1px solid rgba(139,92,246,0.2);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:var(--card-bh)}
.btn-g{background:var(--accent-d);color:var(--accent);border:1px solid rgba(139,92,246,0.12)}
.btn-g:hover{background:rgba(139,92,246,0.18)}
.btn-d{background:var(--red-bg);color:var(--red);border:1px solid rgba(239,68,68,0.15)}
.btn-d:hover{background:rgba(239,68,68,0.15)}
.btn-pur{background:var(--purple-bg);color:var(--purple);border:1px solid rgba(168,85,247,0.15)}
.btn-amber{background:var(--amber-bg);color:var(--amber);border:1px solid rgba(245,158,11,0.15)}
.btn-sm{padding:6px 11px;font-size:10.5px;border-radius:50px}
.btn-icon{width:32px;height:32px;padding:0;justify-content:center;border-radius:50px}

/* ─── CL (callout) ─── */
.cl{background:var(--accent-d);border:1px solid rgba(139,92,246,0.12);border-radius:12px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(245,158,11,0.15);color:var(--amber)}
.cl.amber i{color:var(--amber)}

/* ─── CREATE PANEL ─── */
.create-panel{position:relative;background:var(--card);border:1px solid rgba(139,92,246,0.15);border-radius:20px;padding:0;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px;backdrop-filter:blur(20px)}
.create-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:220px;height:220px;background:radial-gradient(circle,rgba(139,92,246,0.06),transparent 70%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px;position:relative;z-index:1}
.cp-head-icon{width:44px;height:44px;border-radius:14px;background:linear-gradient(135deg,#8B5CF6,#06B6D4);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 20px rgba(139,92,246,0.3)}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 24px 22px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,.15);border:1px solid rgba(139,92,246,0.12);border-radius:14px;padding:14px 16px}
[data-theme="light"] .cp-block{background:rgba(139,92,246,0.03)}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:11px}
.cp-block-label i{color:var(--accent);font-size:14px}
.cp-input-full{width:100%;padding:10px 13px;border-radius:10px;border:1px solid rgba(139,92,246,0.2);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.3s}
.cp-input-full:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(139,92,246,0.1)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:50px;background:var(--accent-d);color:var(--t2);border:1px solid rgba(139,92,246,0.2);cursor:pointer;transition:.3s;white-space:nowrap}
.chip:hover{background:rgba(139,92,246,0.18);color:var(--accent)}
.chip.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 12px rgba(139,92,246,0.3)}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.proto-card{border:1.5px solid var(--card-b);border-radius:14px;padding:13px 12px;cursor:pointer;transition:.3s;text-align:center;position:relative;background:rgba(0,0,0,.12)}
[data-theme="light"] .proto-card{background:rgba(139,92,246,0.03)}
.proto-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(139,92,246,0.1)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-check{position:absolute;top:7px;left:7px;width:16px;height:16px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.3s}
.proto-card-icon{width:32px;height:32px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;margin:0 auto 8px}
.proto-card.active .proto-card-icon{background:var(--accent);color:#fff}
.proto-card-title{font-size:11px;font-weight:800;color:var(--t1)}
.proto-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:15px;flex-shrink:0}
.cp-submit-btn{background:linear-gradient(135deg,#8B5CF6,#06B6D4);color:#fff;border:none;border-radius:50px;padding:13px 28px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 24px rgba(139,92,246,0.3);transition:.3s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 32px rgba(139,92,246,0.4)}

/* ─── TEMPLATE CARDS ─── */
.tmpl-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px;margin-bottom:16px}
.tmpl-card{border:1.5px solid var(--card-b);border-radius:14px;padding:14px;cursor:pointer;transition:.3s;text-align:center;position:relative;background:rgba(0,0,0,.12)}
[data-theme="light"] .tmpl-card{background:rgba(139,92,246,0.03)}
.tmpl-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.tmpl-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(139,92,246,0.1)}
.tmpl-card-icon{width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:16px;margin:0 auto 8px}
.tmpl-card-icon.green{background:var(--green-bg);color:var(--green)}
.tmpl-card-icon.cyan{background:var(--cyan-d);color:var(--cyan)}
.tmpl-card-icon.amber{background:var(--amber-bg);color:var(--amber)}
.tmpl-card-icon.purple{background:var(--purple-bg);color:var(--purple)}
.tmpl-card-icon.blue{background:var(--blue-bg);color:var(--blue)}
.tmpl-card-name{font-size:11px;font-weight:800;color:var(--t1)}
.tmpl-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}

/* ─── GROUP BADGES ─── */
.group-badge{font-size:9px;padding:2px 8px;border-radius:50px;background:var(--accent-d);color:var(--accent);font-weight:700;display:inline-flex;align-items:center;gap:4px;white-space:nowrap}

/* ─── BACKUP SECTION ─── */
.backup-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px;margin-top:14px}
.backup-card{background:var(--card);border:1px solid rgba(139,92,246,0.15);border-radius:14px;padding:14px;transition:.3s;cursor:pointer}
.backup-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.backup-card-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.backup-card-name{font-size:11px;font-weight:700;color:var(--t1);word-break:break-all}
.backup-card-meta{font-size:9px;color:var(--t3);display:flex;align-items:center;gap:6px}
.backup-card-actions{display:flex;gap:6px;margin-top:10px}

/* ─── CFG CARDS ─── */
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:var(--card);backdrop-filter:blur(20px);border:1px solid rgba(139,92,246,0.15);border-radius:14px;padding:0;transition:all .3s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 6px 24px rgba(0,0,0,.18)}
.cfg-card.is-off{opacity:.6}.cfg-card.is-exp{opacity:.78}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px}
.cfg-status-dot{width:9px;height:9px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:var(--t1)}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent);background:var(--accent-d);padding:2px 7px;border-radius:5px;cursor:pointer;transition:.3s}
.cfg-uuid-mini:hover{background:rgba(139,92,246,0.18)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:5px;border-radius:4px;background:rgba(139,92,246,0.08);overflow:hidden}
.ubar-f{height:100%;border-radius:4px;transition:width .4s ease}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.cfg-select{display:flex;align-items:center;flex-shrink:0}
.cfg-select input{width:17px;height:17px;accent-color:var(--accent);cursor:pointer}
.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:var(--purple);font-size:11px}

/* ─── LINKS TOOLBAR ─── */
.links-toolbar{display:flex;align-items:center;gap:14px;margin-bottom:12px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:11px 40px 11px 15px;border-radius:12px;border:1px solid rgba(139,92,246,0.2);background:var(--card);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.3s}
.subs-search input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(139,92,246,0.08)}
.subs-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}
.bulk-selall{display:flex;align-items:center;gap:7px;font-size:12px;color:var(--t2);cursor:pointer;user-select:none;flex-shrink:0}
.bulk-selall input{width:16px;height:16px;accent-color:var(--accent);cursor:pointer}
.bulk-bar{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;background:var(--card);border:1px solid rgba(139,92,246,0.15);border-radius:14px;padding:10px 16px;margin-bottom:12px}
.bulk-count{font-size:12.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:6px}
.bulk-actions{display:flex;gap:6px;flex-wrap:wrap}

/* ─── CFG DASHBOARD ─── */
.cfgdash-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.cfgdash-item{background:var(--card);border:1px solid rgba(139,92,246,0.15);border-radius:14px;padding:13px 14px;cursor:pointer;transition:.3s}
.cfgdash-item:hover{border-color:var(--card-bh)}
.cfgdash-item.on{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent) inset}
.cfgdash-item-top{display:flex;align-items:center;gap:7px;margin-bottom:8px}
.cfgdash-item-label{font-size:12.5px;font-weight:700;color:var(--t1);flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cfgdash-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.cfgdash-stat{background:var(--accent-d);border:1px solid rgba(139,92,246,0.12);border-radius:12px;padding:12px 13px}
.cfgdash-stat-l{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}
.cfgdash-stat-v{font-size:16px;font-weight:800;color:var(--t1)}
.cfgdash-ip-row{display:flex;align-items:center;gap:10px;padding:9px 11px;border-radius:10px;background:var(--accent-d);border:1px solid rgba(139,92,246,0.12);margin-bottom:6px;flex-wrap:wrap}
.cfgdash-ip-row .ip{font-family:ui-monospace,monospace;font-size:12px;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfgdash-ip-meta{display:flex;align-items:center;gap:12px;font-size:10.5px;color:var(--t3);margin-right:auto;flex-wrap:wrap}

/* ─── TRAFFIC PAGE ─── */
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:14px;margin-bottom:20px}
.traf-main-stat{position:relative;border:1px solid rgba(139,92,246,0.15);border-radius:20px;padding:24px;overflow:hidden;backdrop-filter:blur(20px);background:var(--card)}
.traf-main-stat::before{content:'';position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,rgba(139,92,246,0.08),transparent 70%);pointer-events:none}
.traf-main-label{font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:10px;position:relative;z-index:1}
.traf-main-val{font-size:36px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;display:flex;align-items:baseline;gap:6px;position:relative;z-index:1}
.traf-main-val span{font-size:14px;font-weight:500;color:var(--t3)}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 10px;border-radius:50px;margin-top:12px;position:relative;z-index:1}
.traf-trend.up{background:var(--green-bg);color:var(--green)}
.traf-mini{background:var(--card);backdrop-filter:blur(20px);border:1px solid rgba(139,92,246,0.15);border-radius:20px;padding:20px;display:flex;flex-direction:column;justify-content:space-between;transition:.3s}
.traf-mini:hover{border-color:var(--card-bh);transform:translateY(-3px)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.traf-mini-icon{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}
.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.traf-mini-val{font-size:22px;font-weight:800;color:var(--t1)}
.traf-mini-sub{font-size:9.5px;color:var(--t3);margin-top:3px}
.traf-chart-card{position:relative;background:var(--card);backdrop-filter:blur(20px);border:1px solid rgba(139,92,246,0.15);border-radius:22px;padding:24px 26px 20px;box-shadow:var(--shadow);margin-bottom:16px}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:18px}
.traf-chart-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.traf-legend{display:flex;gap:14px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--t2);font-weight:600}
.traf-legend-dot{width:8px;height:8px;border-radius:3px}
.traf-chart-body{height:320px;margin-top:14px;position:relative}

/* ─── CONNECTIONS PAGE ─── */
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:18px}
.conn-hero-tile{background:var(--card);backdrop-filter:blur(20px);border:1px solid rgba(139,92,246,0.15);border-radius:16px;padding:16px 18px;position:relative;overflow:hidden;transition:.3s}
.conn-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:var(--shadow)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--cyan),transparent)}
.conn-hero-icon{width:32px;height:32px;border-radius:10px;background:var(--cyan-d);color:var(--cyan);display:flex;align-items:center;justify-content:center;font-size:15px;margin-bottom:10px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--blue-bg);color:var(--blue)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.conn-hero-val{font-size:21px;font-weight:800;color:var(--t1);line-height:1}
.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}
.conn-toolbar-title i{color:var(--cyan);font-size:15px}
.conn-live-badge{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--cyan);background:var(--cyan-d);padding:5px 12px;border-radius:50px;border:1px solid rgba(6,182,212,0.15)}
.conn-live-dot{width:7px;height:7px;border-radius:50%;background:var(--cyan);animation:pulse 1.6s infinite}
.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.conn-card-v2{background:var(--card);backdrop-filter:blur(20px);border:1px solid rgba(139,92,246,0.15);border-radius:18px;padding:0;overflow:hidden;transition:all .3s cubic-bezier(.4,0,.2,1);position:relative}
.conn-card-v2:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 32px rgba(0,0,0,.22)}
.conn-card-v2-glow{position:absolute;top:-40px;left:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(139,92,246,0.06),transparent 70%);pointer-events:none}
.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 17px 13px;position:relative;z-index:1}
.conn-avatar{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,#8B5CF6,#06B6D4);display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;position:relative;box-shadow:0 4px 14px rgba(139,92,246,0.25)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:16px;border:1.5px solid var(--accent);opacity:.4;animation:breathe2 2.4s ease-in-out infinite}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1)}
.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:9px;font-weight:800;padding:4px 9px;border-radius:50px;background:var(--cyan-d);color:var(--cyan);display:flex;align-items:center;gap:4px;white-space:nowrap;flex-shrink:0}
.conn-card-v2-divider{height:1px;background:linear-gradient(90deg,transparent,var(--card-b) 15%,var(--card-b) 85%,transparent);margin:0 17px}
.conn-card-v2-body{padding:14px 17px 16px}
.conn-proto-row{margin-bottom:12px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.conn-stat-box{display:flex;align-items:center;gap:8px}
.conn-stat-icon{width:26px;height:26px;border-radius:8px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-text-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.conn-stat-text-val{font-size:11.5px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:20px}
.conn-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--t3);margin:0 auto 16px}
.conn-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.conn-empty-v2-sub{font-size:11px;color:var(--t3)}

/* ─── LOG TIMELINE ─── */
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid rgba(139,92,246,0.06)}
.log-item:last-child{border-bottom:none}
.log-ic{width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:var(--green-bg);color:var(--green)}
.log-ic.err{background:var(--red-bg);color:var(--red)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber)}
.log-ic.info{background:var(--accent-d);color:var(--accent)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:8.5px;padding:1px 7px;border-radius:10px;background:var(--accent-d);color:var(--accent);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.erow{padding:9px 0;border-bottom:1px solid rgba(139,92,246,0.06)}
.erow:last-child{border-bottom:none}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px;display:flex;align-items:center;gap:4px}
.emsg{color:var(--red);font-family:ui-monospace,monospace;background:var(--red-bg);padding:6px 9px;border-radius:6px;word-break:break-all;font-size:10.5px}

/* ─── SECURITY ─── */
.srv-panel{position:relative;background:var(--card);border:1px solid rgba(139,92,246,0.15);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);backdrop-filter:blur(20px)}
.srv-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,rgba(139,92,246,0.06),transparent 70%);pointer-events:none}
.srv-hero{display:flex;align-items:center;gap:14px;padding:22px 24px;position:relative;z-index:1;border-bottom:1px solid var(--card-b)}
.srv-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,#8B5CF6,#06B6D4);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 20px rgba(139,92,246,0.3)}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:15px;font-weight:800;color:var(--t1);word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px;position:relative;z-index:1}
.srv-tile{display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.15);border:1px solid rgba(139,92,246,0.12);border-radius:14px;padding:12px 14px;transition:.3s}
[data-theme="light"] .srv-tile{background:rgba(139,92,246,0.03)}
.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.srv-tile-icon{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12px;font-weight:700;color:var(--t1);word-break:break-word}

/* ─── PASSWORD PANEL ─── */
.pw-panel{position:relative;background:var(--card);border:1px solid rgba(139,92,246,0.15);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);backdrop-filter:blur(20px)}
.pw-panel::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,rgba(6,182,212,0.08),transparent 70%);pointer-events:none}
.pw-hero{display:flex;align-items:center;gap:14px;padding:22px 24px 18px;position:relative;z-index:1}
.pw-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,#06B6D4,#8B5CF6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 20px rgba(6,182,212,0.3)}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:15px;font-weight:800;color:var(--t1)}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:2px 24px 22px;position:relative;z-index:1}
.pw-field{position:relative;margin-bottom:13px}
.pw-field label{display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}
.pw-input{width:100%;padding:11px 42px 11px 14px;border-radius:12px;border:1px solid rgba(139,92,246,0.2);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.3s}
.pw-input:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(6,182,212,0.1)}
.pw-eye{position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.pw-eye:hover{color:var(--cyan)}
.pw-strength{height:4px;border-radius:3px;background:rgba(139,92,246,0.08);margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:rgba(100,116,139,.2);transition:.3s}
.pw-strength-label{font-size:9.5px;color:var(--t3);margin-top:5px;display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px}
.pw-req{font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.3s}
.pw-req.met{background:var(--green-bg);color:var(--green)}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,#06B6D4,#8B5CF6);color:#fff;border:none;border-radius:50px;padding:12px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(6,182,212,0.3);transition:.3s}
.pw-submit:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(6,182,212,0.4)}

/* ─── MODALS ─── */
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(8px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);backdrop-filter:blur(24px);border:1px solid rgba(139,92,246,0.2);border-radius:22px;padding:28px 26px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:slideIn .25s ease}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid rgba(139,92,246,0.2);color:var(--t2);width:30px;height:30px;border-radius:9px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;transition:.3s}
.modal-close:hover{background:var(--red-bg);color:var(--red)}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--accent)}

/* ─── TOAST ─── */
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);backdrop-filter:blur(20px);border:1px solid rgba(139,92,246,0.2);color:var(--t1);border-radius:12px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .3s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.3);background:var(--green-bg);color:var(--green)}
.toast.err{border-color:rgba(239,68,68,.3);background:var(--red-bg);color:var(--red)}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent);display:flex;align-items:center;gap:5px;font-weight:600}

/* ─── RESPONSIVE ─── */
@media(max-width:1050px){.tn-center{display:none}.tn-mobile-btn{display:flex}.tn-status{display:none}}
@media(max-width:900px){.stats-row{grid-template-columns:1fr 1fr}.dash-grid,.dash-grid-bottom{grid-template-columns:1fr}.traf-hero{grid-template-columns:1fr 1fr}.conn-hero{grid-template-columns:1fr 1fr}.cp-row{grid-template-columns:1fr}}
@media(max-width:768px){.main-wrap{padding:calc(var(--nav-h) + 16px) 14px 50px}.conn-grid-v2{grid-template-columns:1fr}.cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}.cfg-card{border-radius:16px}.cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}.cfg-identity{min-width:0;flex:1}.cfg-usage-col{min-width:0}.cfg-exp-col{min-width:0}.cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}.cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;margin-top:2;width:100%}.srv-tiles{grid-template-columns:1fr}}
@media(max-width:600px){.topnav{padding:0 12px}.tn-brand{font-size:14px}.stats-row{grid-template-columns:1fr}.traf-hero{grid-template-columns:1fr}.conn-hero{grid-template-columns:1fr}.proto-cards{grid-template-columns:1fr}.cp-footer{flex-direction:column;align-items:stretch}.cp-submit-btn{justify-content:center}.notif-panel{right:-10px;left:auto!important;width:calc(100vw - 20px)!important;max-width:380px!important}.theme-panel{margin:0 8px}}

/* ─── NOTIFICATION BELL & PANEL ─── */
.notif-bell{position:relative;cursor:pointer}
.notif-badge{position:absolute;top:-3px;right:-3px;background:var(--red);color:#fff;font-size:8px;font-weight:800;min-width:16px;height:16px;border-radius:8px;display:flex;align-items:center;justify-content:center;padding:0 4px;border:2px solid var(--bg);animation:badgePop .3s ease;pointer-events:none}
.notif-badge:empty,.notif-badge[data-count="0"]{display:none}
@keyframes badgePop{from{transform:scale(0)}50%{transform:scale(1.3)}to{transform:scale(1)}}
.notif-panel{display:none;position:fixed;top:calc(var(--nav-h) + 8px);left:50%;transform:translateX(-50%);width:420px;max-width:calc(100vw - 32px);max-height:480px;background:var(--card);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid rgba(139,92,246,0.2);border-radius:var(--radius);z-index:300;box-shadow:0 16px 48px rgba(0,0,0,.5);overflow:hidden;animation:slideIn .25s ease}
.notif-panel.open{display:block}
.notif-panel-head{display:flex;align-items:center;justify-content:space-between;padding:14px 16px;border-bottom:1px solid var(--card-b)}
.notif-panel-title{font-size:13px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:7px}
.notif-panel-title i{color:var(--accent);font-size:16px}
.notif-panel-actions{display:flex;gap:6px}
.notif-list{max-height:380px;overflow-y:auto;padding:8px}
.notif-list::-webkit-scrollbar{width:3px}
.notif-list::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
.notif-item{display:flex;align-items:flex-start;gap:10px;padding:10px 12px;border-radius:10px;margin-bottom:4px;transition:.2s;cursor:default;border:1px solid transparent;animation:feedSlide .3s ease}
.notif-item:hover{background:var(--accent-d);border-color:rgba(139,92,246,0.1)}
.notif-item.unread{background:rgba(139,92,246,0.06)}
.notif-icon{width:32px;height:32px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}
.notif-icon.conn{background:var(--green-bg);color:var(--green)}
.notif-icon.disc{background:var(--red-bg);color:var(--red)}
.notif-icon.exp{background:var(--amber-bg);color:var(--amber)}
.notif-icon.err{background:var(--red-bg);color:var(--red)}
.notif-icon.login{background:var(--purple-bg);color:var(--purple)}
.notif-icon.info{background:var(--accent-d);color:var(--accent)}
.notif-body{flex:1;min-width:0}
.notif-msg{font-size:11.5px;color:var(--t1);line-height:1.6;font-weight:500}
.notif-time{font-size:9px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:4px}
.notif-empty{text-align:center;padding:40px 20px;color:var(--t3);font-size:12px}
.notif-empty i{font-size:32px;display:block;margin-bottom:10px;opacity:.3}
.notif-sound-toggle{display:flex;align-items:center;gap:6px;font-size:10px;color:var(--t3);cursor:pointer;padding:4px 10px;border-radius:8px;transition:.2s;border:none;background:none;font-family:inherit}
.notif-sound-toggle:hover{background:var(--accent-d);color:var(--accent)}
.notif-sound-toggle i{font-size:14px}

/* ─── PWA INSTALL BANNER ─── */
.pwa-banner{display:none;position:fixed;bottom:0;left:0;right:0;background:linear-gradient(135deg,rgba(15,11,26,.97),rgba(26,20,40,.97));backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-top:1px solid rgba(139,92,246,0.2);padding:14px 20px;z-index:400;animation:slideUp .4s ease}
.pwa-banner.show{display:flex}
@keyframes slideUp{from{transform:translateY(100%)}to{transform:translateY(0)}}
.pwa-banner-content{display:flex;align-items:center;gap:12px;max-width:800px;margin:0 auto;width:100%}
.pwa-banner-icon{width:40px;height:40px;border-radius:10px;background:linear-gradient(135deg,#8B5CF6,#06B6D4);display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0}
.pwa-banner-text{flex:1}
.pwa-banner-title{font-size:12px;font-weight:700;color:var(--t1)}
.pwa-banner-sub{font-size:10px;color:var(--t3);margin-top:1px}
.pwa-banner-btns{display:flex;gap:8px;flex-shrink:0}
.pwa-install-btn{background:linear-gradient(135deg,#8B5CF6,#06B6D4);color:#fff;border:none;border-radius:50px;padding:8px 18px;font-family:inherit;font-size:11px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:5px;transition:.3s;white-space:nowrap}
.pwa-install-btn:hover{box-shadow:0 4px 16px rgba(139,92,246,0.4);transform:translateY(-1px)}
.pwa-dismiss{background:transparent;border:1px solid rgba(139,92,246,0.2);color:var(--t2);border-radius:50px;padding:8px 14px;font-family:inherit;font-size:11px;font-weight:600;cursor:pointer;transition:.2s}
.pwa-dismiss:hover{background:var(--accent-d);color:var(--accent)}

/* ─── COLOR THEME PANEL ─── */
.theme-panel{position:relative;background:var(--card);border:1px solid rgba(139,92,246,0.15);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);backdrop-filter:blur(20px)}
.theme-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,rgba(6,182,212,0.06),transparent 70%);pointer-events:none}
.theme-panel-hero{display:flex;align-items:center;gap:14px;padding:22px 24px 18px;position:relative;z-index:1}
.theme-panel-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,#8B5CF6,#06B6D4);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 20px rgba(139,92,246,0.3)}
.theme-panel-text{flex:1;min-width:0}
.theme-panel-title{font-size:15px;font-weight:800;color:var(--t1)}
.theme-panel-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.theme-panel-body{padding:2px 24px 22px;position:relative;z-index:1}
.theme-preset-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:16px}
.theme-preset{border:2px solid rgba(139,92,246,0.12);border-radius:12px;padding:10px;cursor:pointer;transition:.3s;text-align:center}
.theme-preset:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.theme-preset.active{border-color:var(--accent);background:var(--accent-d)}
.theme-preset-preview{width:100%;height:28px;border-radius:8px;margin-bottom:6px;position:relative;overflow:hidden}
.theme-preset-preview::before{content:'';position:absolute;inset:0;border-radius:8px;border:1px solid rgba(255,255,255,.08)}
.theme-preset-name{font-size:9px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.04em}
.theme-color-row{display:flex;align-items:center;gap:12px;margin-bottom:10px}
.theme-color-label{font-size:10px;font-weight:700;color:var(--t3);min-width:80px;text-transform:uppercase;letter-spacing:.05em}
.theme-color-picker{width:36px;height:36px;border-radius:10px;border:2px solid rgba(139,92,246,0.2);cursor:pointer;padding:0;background:none;overflow:hidden}
.theme-color-picker::-webkit-color-swatch-wrapper{padding:0}
.theme-color-picker::-webkit-color-swatch{border:none;border-radius:8px}
.theme-color-val{font-family:ui-monospace,monospace;font-size:10px;color:var(--t3);background:var(--accent-d);padding:3px 8px;border-radius:6px;min-width:70px;text-align:center}
.theme-actions{display:flex;gap:8px;margin-top:14px;padding-top:14px;border-top:1px solid var(--card-b);flex-wrap:wrap}
</style>
</head>
<body>
<div class="neon-bg"><div class="neon-orb neon-orb-1"></div><div class="neon-orb neon-orb-2"></div><div class="neon-orb neon-orb-3"></div></div>
<canvas id="particles-canvas"></canvas>
<div class="toast" id="toast"></div>
<div class="notif-panel" id="notif-panel"><div class="notif-panel-head"><div class="notif-panel-title"><i class="ti ti-bell"></i> اعلان‌ها</div><div class="notif-panel-actions"><button class="notif-sound-toggle" id="notif-sound-btn" onclick="toggleNotifSound()" title="صدای اعلان"><i class="ti ti-volume"></i></button><button class="btn btn-sm btn-o" onclick="clearAllNotifs()"><i class="ti ti-trash"></i></button><button class="btn btn-sm btn-o" onclick="toggleNotifPanel()"><i class="ti ti-x"></i></button></div></div><div class="notif-list" id="notif-list"><div class="notif-empty"><i class="ti ti-bell-off"></i><p>اعلانی نیست</p></div></div></div>
<div class="pwa-banner" id="pwa-banner"><div class="pwa-banner-content"><div class="pwa-banner-icon"><i class="ti ti-download"></i></div><div class="pwa-banner-text"><div class="pwa-banner-title">نصب X4G Panel</div><div class="pwa-banner-sub">افزودن به صفحه اصلی برای دسترسی سریع‌تر</div></div><div class="pwa-banner-btns"><button class="pwa-install-btn" id="pwa-install-btn" onclick="installPWA()"><i class="ti ti-download"></i> نصب</button><button class="pwa-dismiss" onclick="dismissPWA()">بعداً</button></div></div></div>
<div class="modal-bg" id="modal-edit-link"><div class="modal"><button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button><div class="modal-title"><i class="ti ti-edit"></i> ویرایش کانفیگ</div><input type="hidden" id="el-uuid"><div class="fg" style="margin-bottom:13px"><label>عنوان</label><input class="fi" id="el-label" style="width:100%"></div><div class="form-row" style="margin-bottom:13px"><div class="fg" style="flex:1"><label>سهمیه (0 = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div><div class="fg"><label>واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div></div><div class="fg" style="margin-bottom:13px"><label>انقضا (روز از الان، 0 = بدون تغییر/نامحدود)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div><div class="fg" style="margin-bottom:13px"><label>یادداشت</label><input class="fi" id="el-note" style="width:100%"></div><div class="form-row" style="margin-bottom:13px"><div class="fg" style="flex:1"><label>Fingerprint (uTLS)</label><select class="fs" id="el-fp" style="width:100%"><option value="chrome">chrome</option><option value="firefox">firefox</option><option value="safari">safari</option><option value="ios">ios</option><option value="android">android</option><option value="edge">edge</option><option value="360">360</option><option value="qq">qq</option><option value="random">random</option><option value="randomized">randomized</option></select></div><div class="fg" style="flex:1"><label>ALPN (خالی = پیش‌فرض)</label><input class="fi" id="el-alpn" placeholder="مثلاً: h2,http/1.1" style="width:100%"></div></div><div class="form-row" style="margin-bottom:16px"><div class="fg" style="flex:1"><label>پورت اتصال</label><input class="fi" id="el-port" type="number" min="1" max="65535" style="width:100%"></div><div class="fg" style="flex:1"><label>محدودیت آی‌پی (0 = نامحدود)</label><input class="fi" id="el-iplimit" type="number" min="0" step="1" style="width:100%"></div></div><div class="form-row" style="margin-bottom:16px"><div class="fg" style="flex:1"><label>محدودیت سرعت (0 = نامحدود)</label><input class="fi" id="el-speed" type="number" min="0" step="0.5" style="width:100%"></div><div class="fg"><label>واحد</label><select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div></div><div class="cl"><i class="ti ti-info-circle"></i><span>برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.</span></div><div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end"><button class="btn btn-o" onclick="closeModal('modal-edit-link')">انصراف</button><button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> ذخیره تغییرات</button></div></div></div>
<select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div></div><div class="fg" style="margin-bottom:13px"><label>گروه</label><input class="fi" id="el-group" placeholder="default" style="width:100%"></div><div class="cl"><i class="ti ti-info-circle"></i><span>برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.</span></div><div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end"><button class="btn btn-o" onclick="closeModal('modal-edit-link')">انصراف</button><button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> ذخیره تغییرات</button></div></div></div>
<div class="modal-bg" id="modal-link-chart"><div class="modal" style="max-width:640px"><button class="modal-close" onclick="closeModal('modal-link-chart')"><i class="ti ti-x"></i></button><div class="modal-title" id="lc-title"><i class="ti ti-chart-line"></i> نمودار مصرف</div><div style="height:280px;margin-top:10px"><canvas id="lc-canvas"></canvas></div></div></div>
<nav class="topnav" id="topnav"><div class="tn-right"><div class="tn-logo" onclick="navTo('overview')"><div class="tn-logo-img"><img src="data:image/png;base64,__LOGO_B64__" alt="X4G"></div><span class="tn-brand">X4G</span></div></div><div class="tn-center"><button class="tn-link on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</button><button class="tn-link" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="tn-badge" id="links-nb">0</span></button><button class="tn-link" data-pg="cfgdash"><i class="ti ti-chart-infographic"></i> کانفیگ‌ها</button><button class="tn-link" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</button><button class="tn-link" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="tn-badge" id="conns-nb">0</span></button><button class="tn-link" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</button><button class="tn-link" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</button></div><div class="tn-left"><span class="tn-status"><span class="dot"></span> فعال</span><div class="notif-bell" id="notif-bell" onclick="toggleNotifPanel()"><i class="ti ti-bell"></i><span class="notif-badge" id="notif-badge" data-count="0"></span></div><button class="tn-btn" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-moon" id="theme-icon"></i></button><button class="tn-logout" id="logout-btn"><i class="ti ti-logout"></i></button><button class="tn-mobile-btn" id="open-mobile"><i class="ti ti-menu-2"></i></button></div></nav>
<div class="mobile-menu" id="mobile-menu"><button class="tn-link on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</button><button class="tn-link" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها</button><button class="tn-link" data-pg="cfgdash"><i class="ti ti-chart-infographic"></i> کانفیگ‌ها</button><button class="tn-link" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</button><button class="tn-link" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات</button><button class="tn-link" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</button><button class="tn-link" data-pg="logs"><i class="ti ti-history"></i> لاگ</button><button class="tn-link" data-pg="errors"><i class="ti ti-alert-triangle"></i> خطاها</button><button class="tn-link" data-pg="testws"><i class="ti ti-wifi"></i> تست WebSocket</button><button class="tn-link" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</button><button class="tn-link" data-pg="support"><i class="ti ti-headset"></i> پشتیبانی</button><button class="tn-logout" id="logout-btn-mob"><i class="ti ti-logout"></i> خروج</button></div>
<main class="main-wrap">
<section class="pg on" id="pg-overview"><div class="topbar"><div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="tb-sub" id="last-upd">در حال بارگذاری...</div></div><div class="tb-right"><span class="badge bg-cyan"><span class="dot dg pulse"></span> فعال</span><span class="badge bg-purple" id="uptime-badge">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div></div>
<div class="stats-row"><div class="stat-card gcard"><div class="stat-card-glow" style="background:rgba(139,92,246,0.3)"></div><div class="stat-card-top"><div class="stat-icon purple"><i class="ti ti-plug-connected"></i></div></div><div class="stat-label">اتصالات فعال</div><div class="stat-val" id="m-conns">—</div><div class="stat-sub"><span class="dot dg pulse"></span> WebSocket / XHTTP زنده</div></div><div class="stat-card gcard"><div class="stat-card-glow" style="background:rgba(6,182,212,0.3)"></div><div class="stat-card-top"><div class="stat-icon cyan"><i class="ti ti-transfer"></i></div></div><div class="stat-label">کل ترافیک</div><div class="stat-val" id="m-traffic">—<span class="stat-unit">MB</span></div><div class="stat-sub">از راه‌اندازی</div></div><div class="stat-card gcard"><div class="stat-card-glow" style="background:rgba(16,185,129,0.3)"></div><div class="stat-card-top"><div class="stat-icon green"><i class="ti ti-link"></i></div></div><div class="stat-label">کانفیگ فعال</div><div class="stat-val" id="m-alinks">—</div><div class="stat-sub" id="m-lsub">از کل</div></div><div class="stat-card gcard" style="cursor:pointer" onclick="navTo('errors')"><div class="stat-card-glow" style="background:rgba(239,68,68,0.3)"></div><div class="stat-card-top"><div class="stat-icon red"><i class="ti ti-alert-triangle"></i></div></div><div class="stat-label">خطاها</div><div class="stat-val" id="m-errs">—</div><div class="stat-sub">از راه‌اندازی</div></div></div>
<div class="dash-grid"><div class="gcard"><div class="card-title"><i class="ti ti-chart-bar"></i> ترافیک ساعتی (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div><div class="gcard"><div class="card-title"><i class="ti ti-rss"></i> اتصالات اخیر</div><div class="feed-list" id="conn-feed"><div class="feed-item"><div class="feed-dot"></div><span class="feed-ip" style="color:var(--t3)">در حال بارگذاری...</span></div></div></div></div>
<div class="dash-grid-bottom"><div class="gcard"><div class="card-title"><i class="ti ti-activity"></i> وضعیت سرویس</div><div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● فعال · سخت‌گیرانه</span></div><div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS Tunnel</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div><div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> Siz10a XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● فعال · mode: auto</span></div><div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> Hysteria2 (UDP)</span><span class="sr-v" style="color:var(--amber-t)">● Stub · بزودی</span></div><div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> Subscription API</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div><div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptime-inline">—</span></div><div class="sr" style="flex-direction:column;align-items:flex-start;gap:4px"><div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> بار نسبی</span><span class="sr-v" id="bw-pct">—%</span></div><div class="spbar" style="width:100%"><div class="spfill" id="bw-bar" style="width:0%"></div></div></div></div><div class="gcard"><div class="card-title"><i class="ti ti-bolt"></i> دسترسی سریع</div><div class="quick-actions"><button class="qa-btn" onclick="navTo('links')"><div class="qa-icon purple"><i class="ti ti-link-plus"></i></div><div class="qa-label">ساخت کانفیگ</div></button><button class="qa-btn" onclick="navTo('connections')"><div class="qa-icon cyan"><i class="ti ti-plug-connected"></i></div><div class="qa-label">اتصالات زنده</div></button><button class="qa-btn" onclick="navTo('traffic')"><div class="qa-icon green"><i class="ti ti-chart-area"></i></div><div class="qa-label">ترافیک</div></button><button class="qa-btn" onclick="navTo('settings')"><div class="qa-icon blue"><i class="ti ti-settings"></i></div><div class="qa-label">تنظیمات</div></button></div><div style="margin-top:14px"><div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="ml-auto badge bg-purple" id="lsummary-badge">۰</span></div><div id="lsummary">—</div></div></div></div>
<div class="dash-grid-bottom"><div class="gcard"><div class="card-title"><i class="ti ti-chart-donut"></i> توزیع پروتکل</div><div class="ch-sm"><canvas id="ch2"></canvas></div></div><div class="gcard"><div class="card-title"><i class="ti ti-alert-triangle"></i> آخرین خطاها</div><div id="dash-errors" style="font-size:12px;color:var(--t3)">—</div></div></div>
<!-- ─── USAGE PREDICTION ─── -->
<div class="dash-grid-bottom"><div class="gcard"><div class="card-title"><i class="ti ti-crystal-ball"></i> پیش‌بینی مصرف</div><div id="pred-cards" style="font-size:12px;color:var(--t3)"><div class="empty"><i class="ti ti-clock-hour-4"></i><p>در حال بارگذاری...</p></div></div></div><div class="gcard"><div class="card-title"><i class="ti ti-server-2"></i> آپتایم سرور</div><div id="uptime-detail"><div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> مدت آپتایم</span><span class="sr-v" id="up-human">—</span></div><div class="sr"><span class="sr-k"><i class="ti ti-rotate"></i> تعداد ری‌استارت</span><span class="sr-v" id="up-restarts">—</span></div><div class="sr"><span class="sr-k"><i class="ti ti-calendar"></i> زمان شروع</span><span class="sr-v" id="up-start">—</span></div></div><div style="height:140px;margin-top:12px"><canvas id="ch-uptime"></canvas></div></div></div>
<!-- ─── TRAFFIC REPORTS (7-Day) ─── -->
<div class="gcard" style="margin-bottom:16px"><div class="card-title"><i class="ti ti-chart-bar"></i> گزارش ترافیک ۷ روز اخیر</div><div class="dash-grid" style="margin-bottom:0"><div><div style="display:flex;gap:10px;margin-bottom:12px;flex-wrap:wrap"><div class="cfgdash-stat"><div class="cfgdash-stat-l">امروز</div><div class="cfgdash-stat-v" id="rpt-today">—</div></div><div class="cfgdash-stat"><div class="cfgdash-stat-l">دیروز</div><div class="cfgdash-stat-v" id="rpt-yesterday">—</div></div><div class="cfgdash-stat"><div class="cfgdash-stat-l">این هفته</div><div class="cfgdash-stat-v" id="rpt-thisweek">—</div></div><div class="cfgdash-stat"><div class="cfgdash-stat-l">هفته قبل</div><div class="cfgdash-stat-v" id="rpt-lastweek">—</div></div></div><div class="ch"><canvas id="ch-daily7"></canvas></div></div><div><div class="card-title" style="margin-top:0"><i class="ti ti-chart-donut"></i> توزیع پروتکل</div><div class="ch-sm"><canvas id="ch-proto-report"></canvas></div></div></div></div>
<!-- ─── CONNECTION MAP ─── -->
<div class="gcard" style="margin-bottom:16px"><div class="card-title"><i class="ti ti-map-2"></i> نقشه اتصالات</div><div id="conn-map-wrap" style="position:relative;width:100%;height:320px;background:rgba(0,0,0,.15);border-radius:14px;overflow:hidden;border:1px solid var(--card-b)"><svg id="conn-map-svg" viewBox="0 0 1000 500" style="width:100%;height:100%"></svg><div id="map-legend" style="position:absolute;bottom:10px;right:10px;background:rgba(0,0,0,.6);border-radius:8px;padding:8px 12px;font-size:10px;color:var(--t2);backdrop-filter:blur(8px)"></div></div><div id="conn-map-list" style="margin-top:12px;font-size:12px;color:var(--t3)"></div></div>
<div class="dash-footer"><span class="df-text">X4G v9.8 · Neon Edition</span><a class="df-link" href="https://t.me/X4GHUB" target="_blank"><i class="ti ti-brand-telegram"></i> t.me/X4GHUB</a></div></section>
<section class="pg" id="pg-links"><div class="topbar"><div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ساخت و مدیریت کانفیگ با سهمیه و انقضا</div></div><div class="tb-right"><span class="badge bg-purple" id="links-pg-cnt">۰ کانفیگ</span></div></div>
<div class="create-panel"><div class="cp-head"><div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div><div class="cp-head-text"><div class="cp-head-title">ساخت کانفیگ جدید</div><div class="cp-head-sub">UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن</div></div></div><div class="cp-body"><div class="cp-block mb16"><div class="cp-block-label"><i class="ti ti-template"></i> قالب سریع</div><div class="tmpl-grid" id="tmpl-grid"><div class="tmpl-card" data-tmpl="unlimited" onclick="selectTemplate('unlimited',this)"><div class="tmpl-card-icon green"><i class="ti ti-infinity"></i></div><div class="tmpl-card-name">نامحدود</div><div class="tmpl-card-desc">بدون محدودیت</div></div><div class="tmpl-card" data-tmpl="limited-10gb" onclick="selectTemplate('limited-10gb',this)"><div class="tmpl-card-icon cyan"><i class="ti ti-database"></i></div><div class="tmpl-card-name">۱۰ گیگ</div><div class="tmpl-card-desc">۱۰GB · ۳۰ روز</div></div><div class="tmpl-card" data-tmpl="trial" onclick="selectTemplate('trial',this)"><div class="tmpl-card-icon amber"><i class="ti ti-flask"></i></div><div class="tmpl-card-name">آزمایشی</div><div class="tmpl-card-desc">۱GB · ۷ روز</div></div><div class="tmpl-card" data-tmpl="premium" onclick="selectTemplate('premium',this)"><div class="tmpl-card-icon purple"><i class="ti ti-crown"></i></div><div class="tmpl-card-name">پریمیوم</div><div class="tmpl-card-desc">۱۰۰GB · ۹۰ روز</div></div><div class="tmpl-card" data-tmpl="basic" onclick="selectTemplate('basic',this)"><div class="tmpl-card-icon blue"><i class="ti ti-package"></i></div><div class="tmpl-card-name">پایه</div><div class="tmpl-card-desc">۵GB · ۳۰ روز</div></div></div></div><div class="cp-row"><div class="cp-block"><div class="cp-block-label"><i class="ti ti-id-badge-2"></i> شناسه کانفیگ</div><input class="cp-input-full" id="nl-label" placeholder="مثلاً: کاربر علی"><div class="cp-mini-row"><input class="cp-input-full" id="nl-note" placeholder="یادداشت (اختیاری)"></div></div><div class="cp-block"><div class="cp-block-label"><i class="ti ti-calendar-due"></i> انقضا</div><div class="cp-mini-row"><input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="انقضا (روز) · 0 = نامحدود"></div><div class="chip-row" id="exp-chips"><span class="chip" onclick="setExpiry(0,this)">نامحدود</span><span class="chip" onclick="setExpiry(7,this)">۷ روز</span><span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span><span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span></div></div></div><div class="cp-block mb16"><div class="cp-block-label"><i class="ti ti-gauge"></i> سهمیه ترافیک</div><div class="cp-quota-inputs"><input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود"><select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select></div><div class="chip-row" id="quota-chips"><span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span><span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span><span class="chip active" onclick="setQuota(1,'GB',this)">۱ GB</span><span class="chip" onclick="setQuota(5,'GB',this)">۵ GB</span><span class="chip" onclick="setQuota(10,'GB',this)">۱۰ GB</span><span class="chip" onclick="setQuota(50,'GB',this)">۵۰ GB</span></div></div><div class="cp-block mb16"><div class="cp-block-label"><i class="ti ti-plug-connected"></i> پروتکل انتقال</div><select id="nl-proto" style="display:none"><option value="vless-ws">VLESS / WebSocket</option><option value="xhttp">XHTTP Ultra · mode: auto</option></select><div class="proto-cards" style="grid-template-columns:repeat(2,1fr)"><div class="proto-card active" data-val="vless-ws" onclick="selectProto('vless-ws',this)"><div class="proto-card-check"><i class="ti ti-check"></i></div><div class="proto-card-icon"><i class="ti ti-link"></i></div><div class="proto-card-title">VLESS / WS</div><div class="proto-card-desc">پایدار و همه‌منظوره</div></div><div class="proto-card" data-val="xhttp" onclick="selectProto('xhttp',this)"><div class="proto-card-check"><i class="ti ti-check"></i></div><div class="proto-card-icon"><i class="ti ti-bolt"></i></div><div class="proto-card-title">XHTTP · mode: auto</div><div class="proto-card-desc">انتخاب خودکار packet-up/stream-up</div></div><div class="proto-card" data-val="hysteria2" onclick="selectProto('hysteria2',this)"><div class="proto-card-check"><i class="ti ti-check"></i></div><div class="proto-card-icon" style="background:var(--amber-bg);color:var(--amber)"><i class="ti ti-bolt"></i></div><div class="proto-card-title">Hysteria2</div><div class="proto-card-desc">UDP/QUIC · سریع‌تر (بزودی)</div></div></div></div><div class="cp-row"><div class="cp-block"><div class="cp-block-label"><i class="ti ti-fingerprint"></i> Fingerprint (uTLS)</div><select class="cp-input-full fs" id="nl-fp"><option value="chrome" selected>chrome</option><option value="firefox">firefox</option><option value="safari">safari</option><option value="ios">ios</option><option value="android">android</option><option value="edge">edge</option><option value="360">360</option><option value="qq">qq</option><option value="random">random</option><option value="randomized">randomized</option></select></div><div class="cp-block"><div class="cp-block-label"><i class="ti ti-antenna-bars-5"></i> ALPN</div><select class="cp-input-full fs" id="nl-alpn-preset" onchange="onAlpnPresetChange()"><option value="">پیش‌فرض پروتکل</option><option value="h2,http/1.1">h2,http/1.1</option><option value="http/1.1">http/1.1</option><option value="h2">h2</option><option value="__custom__">دستی...</option></select><div class="cp-mini-row"><input class="cp-input-full" id="nl-alpn" placeholder="مقدار دستی ALPN" style="display:none"></div></div></div><div class="cp-row mb16" style="grid-template-columns:1fr"><div class="cp-block"><div class="cp-block-label"><i class="ti ti-users"></i> محدودیت آی‌پی / کاربر</div><input class="cp-input-full" id="nl-iplimit" type="number" min="0" step="1" placeholder="0 = نامحدود" value="0"><div class="chip-row" id="iplimit-chips"><span class="chip active" onclick="setIpLimit(0,this)">نامحدود</span><span class="chip" onclick="setIpLimit(1,this)">۱ کاربر</span><span class="chip" onclick="setIpLimit(2,this)">۲ کاربر</span><span class="chip" onclick="setIpLimit(5,this)">۵ کاربر</span></div></div></div><div class="cp-row mb16"><div class="cp-block" style="flex:1"><div class="cp-block-label"><i class="ti ti-gauge"></i> محدودیت سرعت</div><div class="form-row"><input class="cp-input-full" id="nl-speed" type="number" min="0" step="0.5" placeholder="0 = نامحدود" value="0" style="flex:1"><select class="fs" id="nl-speed-unit" style="flex:0 0 100px"><option value="MBIT" selected>Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div><div class="chip-row" id="speed-chips"><span class="chip active" onclick="setSpeedLimit(0,this)">نامحدود</span><span class="chip" onclick="setSpeedLimit(1,this)">۱ Mbps</span><span class="chip" onclick="setSpeedLimit(5,this)">۵ Mbps</span><span class="chip" onclick="setSpeedLimit(10,this)">۱۰ Mbps</span><span class="chip" onclick="setSpeedLimit(25,this)">۲۵ Mbps</span></div></div></div><div class="cp-footer"><div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند.</div><button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button></div></div></div>
<div class="links-toolbar"><div class="subs-search"><i class="ti ti-search"></i><input id="links-search" placeholder="جستجو..." oninput="renderLinksGrid()"></div><select id="links-sort" class="fs" style="min-width:180px" onchange="renderLinksGrid()"><option value="newest">جدیدترین</option><option value="name">نام</option><option value="usage_desc">بیشترین مصرف</option><option value="usage_asc">کمترین مصرف</option><option value="remaining_asc">کمترین باقی‌مانده</option><option value="active_first">فعال‌ها اول</option></select><label class="bulk-selall"><input type="checkbox" id="links-selall" onchange="toggleSelectAllLinks(this)"><span>انتخاب همه</span></label></div>
<div class="bulk-bar" id="links-bulkbar" style="display:none"><span class="bulk-count"><i class="ti ti-checkbox"></i> <span id="links-selcount">۰</span> انتخاب شده</span><div class="bulk-actions"><button class="btn btn-sm btn-g" onclick="bulkLinksAction('activate')"><i class="ti ti-circle-check"></i> فعال</button><button class="btn btn-sm btn-g" onclick="bulkLinksAction('deactivate')"><i class="ti ti-circle-x"></i> غیرفعال</button><button class="btn btn-sm btn-g" onclick="bulkLinksAction('reset')"><i class="ti ti-rotate"></i> ریست</button><button class="btn btn-sm btn-d" onclick="bulkLinksAction('delete')"><i class="ti ti-trash"></i> حذف</button><button class="btn btn-sm btn-o" onclick="clearLinksSelection()"><i class="ti ti-x"></i> لغو</button></div></div>
<div class="cfg-grid" id="links-grid"></div><div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی نیست</p></div><div class="empty" id="links-empty-search" style="display:none"><i class="ti ti-search-off"></i><p>موردی یافت نشد</p></div></section>
<section class="pg" id="pg-cfgdash"><div class="topbar"><div><div class="tb-title"><i class="ti ti-chart-infographic"></i> داشبورد کانفیگ‌ها</div><div class="tb-sub">آنالیز اختصاصی هر کانفیگ</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadCfgDash()"><i class="ti ti-refresh"></i> رفرش</button></div></div><div class="card" style="margin-bottom:16px"><div class="card-title"><i class="ti ti-list"></i> انتخاب <span class="ml-auto badge bg-purple" id="cfgdash-count">۰</span></div><div class="cfgdash-grid" id="cfgdash-list"></div><div class="empty" id="cfgdash-empty" style="display:none"><i class="ti ti-link-off"></i><p>کانفیگی نیست</p></div></div><div id="cfgdash-detail"><div class="card"><div class="empty"><i class="ti ti-hand-click"></i><p>یک کانفیگ انتخاب کنید</p></div></div></div></section>
<section class="pg" id="pg-traffic"><div class="topbar"><div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل مصرف پهنای باند</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div></div><div class="traf-hero"><div class="traf-main-stat"><div class="traf-main-label"><i class="ti ti-database"></i> کل ترافیک</div><div class="traf-main-val" id="t-traffic">—<span>MB</span></div><div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div></div><div class="traf-mini"><div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">میانگین ساعتی</span></div><div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB/hr</div></div></div><div class="traf-mini"><div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">پیک</span></div><div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">—</div></div></div><div class="traf-mini"><div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">کمترین</span></div><div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB/hr</div></div></div></div><div class="traf-chart-card"><div class="traf-chart-head"><div><div class="traf-chart-title"><i class="ti ti-activity"></i> روند مصرف</div><div class="traf-chart-sub">مگابایت در ساعت</div></div><div class="traf-legend"><div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> مصرف</div><div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--cyan)"></span> میانگین</div></div></div><div class="traf-chart-body"><canvas id="ch3"></canvas></div></div></section>
<section class="pg" id="pg-connections"><div class="topbar"><div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده</div></div><div class="tb-right"><span class="badge bg-cyan" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div></div><div class="conn-hero"><div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div><div class="conn-hero-label">اتصالات زنده</div><div class="conn-hero-val" id="ch-count">—</div></div><div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-transfer"></i></div><div class="conn-hero-label">ترافیک لحظه‌ای</div><div class="conn-hero-val" id="ch-traffic">—</div></div><div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-clock"></i></div><div class="conn-hero-label">میانگین مدت</div><div class="conn-hero-val" id="ch-avgdur">—</div></div><div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div><div class="conn-hero-label">آی‌پی یکتا</div><div class="conn-hero-val" id="ch-uniq">—</div></div></div><div class="conn-toolbar"><div class="conn-toolbar-title"><i class="ti ti-list-details"></i> لیست</div><div class="conn-live-badge"><span class="conn-live-dot"></span> بروزرسانی خودکار</div></div><div class="conn-grid-v2" id="conns-grid"></div><div class="conn-empty-v2" id="conns-empty" style="display:none"><div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div><div class="conn-empty-v2-title">اتصالی نیست</div></div></section>
<section class="pg" id="pg-security"><div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> امنیت</div></div></div><div class="dash-grid"><div class="card"><div class="card-title"><i class="ti ti-lock"></i> رمزنگاری</div><div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● فعال (443)</span></div><div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div><div class="sr"><span class="sr-k"><i class="ti ti-network"></i> پروتکل‌ها</span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div><div class="sr"><span class="sr-k"><i class="ti ti-key"></i> هش رمز</span><span class="sr-v">SHA-256+Salt</span></div><div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> سشن</span><span class="sr-v">HttpOnly · 7 روز</span></div></div><div class="card"><div class="card-title"><i class="ti ti-shield-check"></i> کنترل دسترسی</div><div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● فعال v9</span></div><div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> فعال/غیرفعال</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div><div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> سهمیه ترافیک</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div><div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> انقضا</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div><div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> رمز پابلیک</span><span class="sr-v" style="color:var(--green-t)">● اختیاری · SHA-256</span></div></div></div><div class="dash-grid-bottom"><div class="card"><div class="card-title"><i class="ti ti-shield-exclamation"></i> حفاظت در برابر Brute Force</div><div id="bf-blocked-list"><div style="color:var(--t3);font-size:12px;padding:8px 0">در حال بارگذاری...</div></div></div><div class="card"><div class="card-title"><i class="ti ti-shield-lock"></i> احراز هویت دو مرحله‌ای (2FA)</div><div id="2fa-status"><div style="color:var(--t3);font-size:12px;padding:8px 0">در حال بارگذاری...</div></div><div id="2fa-setup" style="display:none;margin-top:12px"><div class="fg" style="margin-bottom:10px"><label>کد ۶ رقمی</label><input class="fi" id="2fa-code" placeholder="کد را وارد کنید" maxlength="6" style="width:100%"></div><div style="display:flex;gap:8px"><button class="btn btn-p btn-sm" onclick="verify2FA()"><i class="ti ti-check"></i> تأیید</button><button class="btn btn-d btn-sm" onclick="disable2FA()"><i class="ti ti-x"></i> غیرفعال</button></div></div></div></div></section>
<section class="pg" id="pg-logs"><div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div><div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>لاگی نیست</p></div></div></section>
<section class="pg" id="pg-errors"><div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> خطاها</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div><div class="card"><div class="card-title"><i class="ti ti-bug"></i> لاگ خطاها</div><div id="errs-full">—</div></div></section>
<section class="pg" id="pg-testws"><div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> تست WebSocket</div></div></div><div class="card" style="max-width:660px"><div class="cl amber" style="margin-top:0;margin-bottom:12px"><i class="ti ti-alert-triangle"></i><span>فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند.</span></div><div class="form-row" style="margin-bottom:12px"><div class="fg" style="flex:1"><label>UUID</label><input class="fi" id="ws-uuid" placeholder="UUID" style="width:100%"></div><button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> اتصال</button><button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> قطع</button></div><div class="form-row" style="margin-bottom:12px"><input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1"><button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> ارسال</button></div><div style="background:rgba(0,0,0,.3);border:1px solid rgba(139,92,246,0.15);border-radius:10px;padding:14px;height:250px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log"><p style="color:var(--t3)">منتظر اتصال...</p></div></div></section>
<section class="pg" id="pg-settings"><div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div></div></div><div class="dash-grid"><div class="srv-panel"><div class="srv-hero"><div class="srv-hero-icon"><i class="ti ti-server-2"></i></div><div class="srv-hero-text"><div class="srv-hero-domain" id="set-host">—</div><div class="srv-hero-sub"><span class="dot dg pulse"></span> آنلاین · Railway</div></div></div><div class="srv-tiles"><div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پورت</div><div class="srv-tile-val">443 (TLS)</div></div></div><div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">نسخه</div><div class="srv-tile-val">v9.8</div></div></div><div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label">فریم‌ورک</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div><div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پلتفرم</div><div class="srv-tile-val">Railway</div></div></div><div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">ذخیره‌سازی</div><div class="srv-tile-val">JSON File (/data)</div></div></div></div></div><div class="pw-panel"><div class="pw-hero"><div class="pw-hero-icon"><i class="ti ti-key"></i></div><div class="pw-hero-text"><div class="pw-hero-title">تغییر رمز عبور</div><div class="pw-hero-sub">رمز قوی انتخاب کنید</div></div></div><div class="pw-body"><div class="pw-field"><label>رمز فعلی</label><input class="pw-input" type="password" id="cp-cur" placeholder="رمز فعلی"><button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button></div><div class="pw-field" style="margin-bottom:6px"><label>رمز جدید</label><input class="pw-input" type="password" id="cp-new" placeholder="حداقل ۴ کاراکتر" oninput="checkPwStrength(this.value)"><button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button></div><div class="pw-strength" id="pw-strength-bar"><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div></div><div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> قدرت رمز</div><div class="pw-reqs"><span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> حداقل ۴ کاراکتر</span><span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> شامل عدد</span><span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> حروف بزرگ/کوچک</span></div><div class="pw-field" style="margin-bottom:18px"><label>تکرار رمز جدید</label><input class="pw-input" type="password" id="cp-cf" placeholder="تکرار"><button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button></div><button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> ذخیره رمز جدید</button></div></div></div><div class="dash-grid"><div class="card" style="border:1px solid rgba(245,158,11,0.2)"><div class="card-title"><i class="ti ti-gauge"></i> تست سرعت</div><div style="text-align:center;padding:20px 0"><div style="font-size:32px;font-weight:800;color:var(--t1)" id="st-speed">—</div><div style="font-size:11px;color:var(--t3);margin-top:4px">Mbps</div><div style="display:flex;justify-content:center;gap:20px;margin-top:12px"><div><div style="font-size:10px;color:var(--t3)">تاخیر</div><div style="font-size:14px;font-weight:700;color:var(--accent)" id="st-latency">—</div></div><div><div style="font-size:10px;color:var(--t3)">آخرین تست</div><div style="font-size:10px;color:var(--t3)" id="st-time">—</div></div></div></div><button class="btn btn-amber" style="width:100%;justify-content:center;margin-top:8px" onclick="runSpeedTest()"><i class="ti ti-gauge"></i> اجرای تست سرعت</button></div><div class="card" style="border:1px solid rgba(16,185,129,0.2)"><div class="card-title"><i class="ti ti-refresh"></i> بروزرسانی Xray Core</div><div style="margin-bottom:12px"><div class="sr"><span class="sr-k"><i class="ti ti-versions"></i> نسخه فعلی</span><span class="sr-v" id="xray-cur">—</span></div><div class="sr"><span class="sr-k"><i class="ti ti-cloud-download"></i> جدیدترین نسخه</span><span class="sr-v" id="xray-latest">—</span></div><div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آخرین بررسی</span><span class="sr-v" id="xray-check-time">—</span></div></div><div style="display:flex;gap:8px"><button class="btn btn-o" style="flex:1;justify-content:center" onclick="checkXrayUpdate()"><i class="ti ti-search"></i> بررسی آپدیت</button><button class="btn btn-p" style="flex:1;justify-content:center" onclick="installXrayUpdate()"><i class="ti ti-download"></i> بروزرسانی</button></div><div id="xray-status" style="margin-top:10px;font-size:11px;color:var(--t3)"></div></div></div></div></div></section>
<section class="pg" id="pg-settings"><div class="topbar"><div><div class="tb-title"><i class="ti ti-palette"></i> رنگ و تم</div><div class="tb-sub">سفارشی‌سازی ظاهر پنل</div></div></div><div class="theme-panel"><div class="theme-panel-hero"><div class="theme-panel-icon"><i class="ti ti-palette"></i></div><div class="theme-panel-text"><div class="theme-panel-title">تنظیم رنگ پنل</div><div class="theme-panel-sub">رنگ اصلی، پس‌زمینه و کارت‌ها را تغییر دهید</div></div></div><div class="theme-panel-body"><div style="margin-bottom:14px"><div style="font-size:10px;font-weight:700;color:var(--t3);text-transform:uppercase;letter-spacing:.06em;margin-bottom:10px;display:flex;align-items:center;gap:6px"><i class="ti ti-star" style="color:var(--accent)"></i> تم‌های آماده</div><div class="theme-preset-grid" id="theme-presets"><div class="theme-preset" onclick="applyPreset('neon-purple')" data-preset="neon-purple"><div class="theme-preset-preview" style="background:linear-gradient(135deg,#8B5CF6,#06B6D4)"></div><div class="theme-preset-name">بنفش نئون</div></div><div class="theme-preset" onclick="applyPreset('ocean-blue')" data-preset="ocean-blue"><div class="theme-preset-preview" style="background:linear-gradient(135deg,#0EA5E9,#3B82F6)"></div><div class="theme-preset-name">آبی اقیانوسی</div></div><div class="theme-preset" onclick="applyPreset('sunset-orange')" data-preset="sunset-orange"><div class="theme-preset-preview" style="background:linear-gradient(135deg,#F97316,#EF4444)"></div><div class="theme-preset-name">نارنجی غروب</div></div><div class="theme-preset" onclick="applyPreset('forest-green')" data-preset="forest-green"><div class="theme-preset-preview" style="background:linear-gradient(135deg,#10B981,#059669)"></div><div class="theme-preset-name">سبز جنگلی</div></div><div class="theme-preset" onclick="applyPreset('rose-pink')" data-preset="rose-pink"><div class="theme-preset-preview" style="background:linear-gradient(135deg,#EC4899,#F43F5E)"></div><div class="theme-preset-name">صورتی رز</div></div><div class="theme-preset active" onclick="applyPreset('default')" data-preset="default"><div class="theme-preset-preview" style="background:linear-gradient(135deg,#8B5CF6,#A78BFA)"></div><div class="theme-preset-name">پیش‌فرض</div></div></div></div><div style="font-size:10px;font-weight:700;color:var(--t3);text-transform:uppercase;letter-spacing:.06em;margin-bottom:10px;display:flex;align-items:center;gap:6px"><i class="ti ti-color-picker" style="color:var(--cyan)"></i> رنگ‌های سفارشی</div><div class="theme-color-row"><span class="theme-color-label">رنگ اصلی</span><input type="color" class="theme-color-picker" id="tc-primary" value="#8B5CF6" oninput="previewCustomColor()"><span class="theme-color-val" id="tc-primary-val">#8B5CF6</span></div><div class="theme-color-row"><span class="theme-color-label">رنگ فرعی</span><input type="color" class="theme-color-picker" id="tc-secondary" value="#06B6D4" oninput="previewCustomColor()"><span class="theme-color-val" id="tc-secondary-val">#06B6D4</span></div><div class="theme-color-row"><span class="theme-color-label">پس‌زمینه</span><input type="color" class="theme-color-picker" id="tc-bg" value="#0F0B1A" oninput="previewCustomColor()"><span class="theme-color-val" id="tc-bg-val">#0F0B1A</span></div><div class="theme-color-row"><span class="theme-color-label">رنگ کارت</span><input type="color" class="theme-color-picker" id="tc-card" value="#140F23" oninput="previewCustomColor()"><span class="theme-color-val" id="tc-card-val">#140F23</span></div><div class="theme-actions"><button class="btn btn-p" onclick="applyCustomTheme()"><i class="ti ti-check"></i> اعمال رنگ</button><button class="btn btn-o" onclick="resetTheme()"><i class="ti ti-rotate"></i> بازگشت به پیش‌فرض</button></div></div></div></section>
<section class="pg" id="pg-support"><div class="topbar"><div><div class="tb-title"><i class="ti ti-headset"></i> پشتیبانی</div></div></div><div class="srv-panel"><div class="srv-hero"><div class="srv-hero-icon"><i class="ti ti-headset"></i></div><div class="srv-hero-text"><div class="srv-hero-domain">پشتیبانی X4G</div><div class="srv-hero-sub"><span class="dot dg pulse"></span> راه‌های ارتباطی</div></div></div><div class="srv-tiles"><a class="srv-tile" href="https://www.youtube.com/@X4GHUB" target="_blank" style="text-decoration:none"><div class="srv-tile-icon"><i class="ti ti-brand-youtube"></i></div><div class="srv-tile-text"><div class="srv-tile-label">یوتیوب</div><div class="srv-tile-val">youtube.com/@X4GHUB</div></div></a><a class="srv-tile" href="https://t.me/x4g_group" target="_blank" style="text-decoration:none"><div class="srv-tile-icon"><i class="ti ti-users-group"></i></div><div class="srv-tile-text"><div class="srv-tile-label">گروه</div><div class="srv-tile-val">t.me/x4g_group</div></div></a><a class="srv-tile" href="https://t.me/X4GHUB" target="_blank" style="text-decoration:none"><div class="srv-tile-icon"><i class="ti ti-speakerphone"></i></div><div class="srv-tile-text"><div class="srv-tile-label">کانال</div><div class="srv-tile-val">t.me/X4GHUB</div></div></a><a class="srv-tile" href="https://github.com/x4gKing" target="_blank" style="text-decoration:none"><div class="srv-tile-icon"><i class="ti ti-brand-github"></i></div><div class="srv-tile-text"><div class="srv-tile-label">گیت‌هاب</div><div class="srv-tile-val">github.com/x4gKing</div></div></a></div></div></section>
</main>
<script>
let isDark=localStorage.getItem('x4g-theme')!=='light';
function applyTheme(dark){document.documentElement.setAttribute('data-theme',dark?'dark':'light');const icon=dark?'ti-sun':'ti-moon';document.getElementById('theme-icon').className='ti '+icon;}
function toggleTheme(){isDark=!isDark;localStorage.setItem('x4g-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
function toast(msg,type=''){const t=document.getElementById('toast');t.textContent=msg;t.className='toast show'+(type?' '+type:'');setTimeout(()=>t.classList.remove('show'),2400);}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n)..pc-xhttp{background:var(--purple-bg);color:var(--purple)}(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'')..pc-xhttp{background:var(--purple-bg);color:var(--purple)}(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';const d=daysLeft(exp);if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';if(d<=3)return '<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> '+toFa(d)+' روز مانده</span>';return '<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> '+toFa(d)+' روز مانده</span>';}
function protoBadge(p){const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp':['XHTTP · auto','pc-xhttp'],'hysteria2':['HY2 · UDP','pc-hy2']};const v=m[p]||m['vless-ws'];return '<span class="proto-chip '+v[1]+'">'+v[0]+'</span>';}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
document.getElementById('logout-btn-mob').addEventListener('click',logout);
async function authF(url,opts={}){const r=await fetch(url,opts);if(r.status===401){location.href='/login';throw new Error('unauthorized')}return r}
function setQuota(val,unit,el){document.getElementById('nl-val').value=val===0?'':val;document.getElementById('nl-unit').value=unit;document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));el.classList.add('active');}
function setExpiry(days,el){document.getElementById('nl-exp').value=days===0?'':days;document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));el.classList.add('active');}
function selectProto(val,el){document.getElementById('nl-proto').value=val;document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));el.classList.add('active');}
function setIpLimit(n,el){document.getElementById('nl-iplimit').value=n;document.querySelectorAll('#iplimit-chips .chip').forEach(c=>c.classList.remove('active'));el.classList.add('active');}
function setSpeedLimit(n,el){document.getElementById('nl-speed').value=n;document.getElementById('nl-speed-unit').value='MBIT';document.querySelectorAll('#speed-chips .chip').forEach(c=>c.classList.remove('active'));el.classList.add('active');}
function onAlpnPresetChange(){const p=document.getElementById('nl-alpn-preset').value;const inp=document.getElementById('nl-alpn');if(p==='__custom__'){inp.style.display='block';inp.value='';inp.focus();}else{inp.style.display='none';inp.value=p;}}
const mobileMenu=document.getElementById('mobile-menu');
document.getElementById('open-mobile').addEventListener('click',()=>{mobileMenu.classList.toggle('show');});
mobileMenu.querySelectorAll('.tn-link').forEach(el=>el.addEventListener('click',()=>{mobileMenu.classList.remove('show');navTo(el.dataset.pg);}));
function navTo(name){document.querySelectorAll('.tn-link').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,logs:loadActivity,cfgdash:loadCfgDash};if(loaders[name])loaders[name]();mobileMenu.classList.remove('show');window.scrollTo({top:0,behavior:'smooth'});}
document.querySelectorAll('.tn-link').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}
function initParticles(){const c=document.getElementById('particles-canvas');if(!c)return;const ctx=c.getContext('2d');let W,H;const particles=[];function resize(){W=c.width=window.innerWidth;H=c.height=window.innerHeight;}resize();window.addEventListener('resize',resize);for(let i=0;i<40;i++){particles.push({x:Math.random()*W,y:Math.random()*H,r:Math.random()*2+0.5,dx:(Math.random()-0.5)*0.3,dy:(Math.random()-0.5)*0.3,o:Math.random()*0.4+0.1,color:Math.random()>.6?'rgba(139,92,246,':'rgba(6,182,212,'});}function draw(){ctx.clearRect(0,0,W,H);particles.forEach(p=>{p.x+=p.dx;p.y+=p.dy;if(p.x<0)p.x=W;if(p.x>W)p.x=0;if(p.y<0)p.y=H;if(p.y>H)p.y=0;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=p.color+p.o+')';ctx.fill();});for(let i=0;i<particles.length;i++){for(let j=i+1;j<particles.length;j++){const dx=particles[i].x-particles[j].x,dy=particles[i].y-particles[j].y;const dist=Math.sqrt(dx*dx+dy*dy);if(dist<120){ctx.beginPath();ctx.moveTo(particles[i].x,particles[i].y);ctx.lineTo(particles[j].x,particles[j].y);ctx.strokeStyle='rgba(139,92,246,'+(0.06*(1-dist/120))+')';ctx.lineWidth=0.5;ctx.stroke();}}}requestAnimationFrame(draw);}draw();}
let prevTraf=0,ch1,ch2,ch3;
async function fetchStats(){try{const r=await authF('/stats'),d=await r.json();document.getElementById('m-conns').textContent=d.active_connections;document.getElementById('conns-nb').textContent=d.active_connections;document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="stat-unit">MB</span>';document.getElementById('m-alinks').textContent=d.active_links??'—';document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';document.getElementById('m-errs').textContent=d.total_errors??'—';document.getElementById('errs-badge').textContent=d.total_errors+' خطا';document.getElementById('uptime-inline').textContent=d.uptime;document.getElementById('uptime-badge').textContent='Railway · '+d.uptime;document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' اتصال';document.getElementById('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="stat-unit">MB</span>';const delta=d.total_traffic_mb-prevTraf,pct=Math.min(100,Math.round((delta/50)*100));document.getElementById('bw-pct').textContent=pct+'%';document.getElementById('bw-bar').style.width=pct+'%';prevTraf=d.total_traffic_mb;if(d.hourly){const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));[ch1,ch3].forEach(c=>{if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});if(vals.length){const avg=vals.reduce((a,b)=>a+b,0)/vals.length,peak=Math.max(...vals);document.getElementById('t-avg').innerHTML=avg.toFixed(2)+'<span class="stat-unit">MB</span>';document.getElementById('t-peak').innerHTML=peak.toFixed(2)+'<span class="stat-unit">MB</span>';}}renderErrs(d.recent_errors||[]);renderDashErrors(d.recent_errors||[]);}catch(e){console.error(e)}}
function renderErrs(errs){const el=document.getElementById('errs-full');if(!el)return;if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}el.innerHTML=errs.slice().reverse().map(e=>'<div class="erow"><div class="etime"><i class="ti ti-clock"></i>'+new Date(e.time).toLocaleString('fa-IR')+'</div><div class="emsg">'+esc(e.error)+(e.url?' — '+esc(e.url):'')+'</div></div>').join('');}
function renderDashErrors(errs){const el=document.getElementById('dash-errors');if(!el)return;if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:8px 0;font-size:12px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}el.innerHTML=errs.slice(-4).reverse().map(e=>'<div style="padding:6px 0;border-bottom:1px solid rgba(139,92,246,0.06)"><div style="color:var(--t3);font-size:9.5px;margin-bottom:2px">'+new Date(e.time).toLocaleString('fa-IR')+'</div><div style="color:var(--red);font-family:ui-monospace,monospace;font-size:10px;background:var(--red-bg);padding:4px 8px;border-radius:4px;word-break:break-all">'+esc(e.error)+'</div></div>').join('');}
async function loadActivity(){try{const r=await authF('/api/activity'),d=await r.json();const logs=(d.logs||[]).slice().reverse();const el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');if(!logs.length){el.innerHTML='';em.style.display='block';return}em.style.display='none';const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};const kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};el.innerHTML=logs.map(l=>'<div class="log-item"><div class="log-ic '+l.level+'"><i class="ti '+(icMap[l.level]||'ti-info-circle')+'"></i></div><div class="log-body"><div class="log-msg">'+esc(l.message)+'</div><div class="log-time"><i class="ti ti-clock"></i> '+new Date(l.time).toLocaleString('fa-IR')+' <span class="log-kind">'+(kindFa[l.kind]||l.kind)+'</span></div></div></div>').join('');}catch(e){console.error(e)}}
let allLinksList=[];let selectedLinks=new Set();
async function loadLinks(){try{const r=await authF('/api/links');const {links=[]}=await r.json();allLinksList=links;const validUuids=new Set(links.map(l=>l.uuid));selectedLinks.forEach(u=>{if(!validUuids.has(u))selectedLinks.delete(u)});document.getElementById('links-nb').textContent=links.length;document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' کانفیگ';document.getElementById('lsummary-badge').textContent=toFa(links.length);document.getElementById('lsummary').innerHTML=links.length?links.slice(0,6).map(l=>'<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti '+(l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x')+'" style="color:'+(l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)')+'"></i>'+esc(l.label)+'</span><span class="sr-v" style="font-size:10px">'+fmtB(l.used_bytes)+' / '+(l.limit_bytes===0?'∞':fmtB(l.limit_bytes))+'</span></div>').join(''):'<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی نیست</p></div>';renderLinksGrid();}catch(e){console.error(e)}}
function filteredLinksList(){const q=(document.getElementById('links-search')?.value||'').trim().toLowerCase();let list=!q?allLinksList:allLinksList.filter(l=>(l.label||'').toLowerCase().includes(q)||(l.note||'').toLowerCase().includes(q)||(l.uuid||'').toLowerCase().includes(q));const sortBy=document.getElementById('links-sort')?.value||'newest';const remaining=l=>l.limit_bytes===0?Infinity:Math.max(0,l.limit_bytes-l.used_bytes);list=list.slice();if(sortBy==='name'){list.sort((a,b)=>(a.label||'').localeCompare(b.label||'','fa'))}else if(sortBy==='usage_desc'){list.sort((a,b)=>(b.used_bytes||0)-(a.used_bytes||0))}else if(sortBy==='usage_asc'){list.sort((a,b)=>(a.used_bytes||0)-(b.used_bytes||0))}else if(sortBy==='remaining_asc'){list.sort((a,b)=>remaining(a)-remaining(b))}else if(sortBy==='active_first'){list.sort((a,b)=>((b.active&&!b.expired)?1:0)-((a.active&&!a.expired)?1:0))}else{list.sort((a,b)=>(b.created_at||'').localeCompare(a.created_at||''))}return list;}
function renderLinksGrid(){const links=filteredLinksList();const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty'),emptySearch=document.getElementById('links-empty-search');if(!allLinksList.length){grid.innerHTML='';empty.style.display='block';emptySearch.style.display='none';updateBulkBar();return}if(!links.length){grid.innerHTML='';empty.style.display='none';emptySearch.style.display='block';updateBulkBar();return}empty.style.display='none';emptySearch.style.display='none';grid.innerHTML=links.map(l=>{const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';const allowed=l.active&&!l.expired;const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');const checked=selectedLinks.has(l.uuid)?'checked':'';return '<div class="cfg-card '+cardCls+'"><div class="cfg-row"><span class="cfg-select"><input type="checkbox" '+checked+' onchange="toggleLinkSelect(\''+l.uuid+'\',this)"></span><span class="cfg-status-dot '+(allowed?'pulse':'')+'"></span><div class="cfg-identity"><div class="cfg-label">'+esc(l.label)+'</div><div class="cfg-sub-meta"><span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText(\''+l.uuid+'\').then(()=>toast(\'UUID کپی شد\',\'ok\'))" title="'+l.uuid+'"><i class="ti ti-fingerprint"></i> '+l.uuid.slice(0,10)+'…</span><span>'+new Date(l.created_at).toLocaleDateString('fa-IR')+'</span></div></div><div class="cfg-divider-v"></div><div class="cfg-usage-col"><div class="ubar"><div class="ubar-f" style="width:'+pct+'%;background:'+bc+'"></div></div><div class="utxt"><span>'+fmtB(l.used_bytes)+'</span><span>از '+lim+'</span></div></div><div class="cfg-divider-v"></div><div class="cfg-exp-col">'+expChip(l.expires_at,l.expired)+'</div><div class="cfg-divider-v"></div><div class="cfg-badges-col">'+protoBadge(l.protocol)+'<span class="cfg-sub-tag"><i class="ti ti-route"></i> :'+(l.port||443)+'</span><span class="cfg-sub-tag"><i class="ti ti-fingerprint"></i> '+esc(l.fingerprint||'chrome')+'</span><span class="cfg-sub-tag"><i class="ti ti-users"></i> '+(l.connected_ips||0)+(l.ip_limit?('/'+l.ip_limit):' (∞)')+'</span><span class="cfg-sub-tag"><i class="ti ti-gauge"></i> '+(l.speed_limit_bytes?((l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps'):'نامحدود')+'</span></div><div class="cfg-divider-v"></div><div class="cfg-actions"><button class="tog'+(allowed?' on':'')+'" onclick="toggleActive(\''+l.uuid+'\','+(!l.active)+')"></button><button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText(\''+esc(l.vless_link)+'\').then(()=>toast(\'لینک کپی شد\',\'ok\'))" title="کپی"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="window.open(\''+esc(l.sub_url)+'\',\'_blank\')" title="ساب"><i class="ti ti-rss"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="showQR(\''+esc(l.vless_link)+'\')" title="QR"><i class="ti ti-qrcode"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="openLinkChart(\''+l.uuid+'\',\''+esc(l.label)+'\')" title="نمودار"><i class="ti ti-chart-line"></i></button><button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink(\''+l.uuid+'\')" title="ویرایش"><i class="ti ti-edit"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="resetUsage(\''+l.uuid+'\')" title="ریست"><i class="ti ti-rotate"></i></button><button class="btn btn-sm btn-d btn-icon" onclick="deleteLink(\''+l.uuid+'\')" title="حذف"><i class="ti ti-trash"></i></button></div></div></div>';}).join('');updateBulkBar();}
function toggleLinkSelect(uuid,el){if(el.checked)selectedLinks.add(uuid);else selectedLinks.delete(uuid);updateBulkBar();}
function toggleSelectAllLinks(el){const list=filteredLinksList();if(el.checked)list.forEach(l=>selectedLinks.add(l.uuid));else list.forEach(l=>selectedLinks.delete(l.uuid));renderLinksGrid();}
function clearLinksSelection(){selectedLinks.clear();renderLinksGrid();}
function updateBulkBar(){const bar=document.getElementById('links-bulkbar');const selall=document.getElementById('links-selall');const n=selectedLinks.size;document.getElementById('links-selcount').textContent=toFa(n);bar.style.display=n>0?'flex':'none';const list=filteredLinksList();selall.checked=list.length>0&&list.every(l=>selectedLinks.has(l.uuid));}
async function bulkLinksAction(action){const uuids=Array.from(selectedLinks);if(!uuids.length)return;if(action==='delete'&&!confirm('حذف '+toFa(uuids.length)+' کانفیگ؟'))return;try{await Promise.all(uuids.map(uuid=>{if(action==='activate')return authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:true})});if(action==='deactivate')return authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:false})});if(action==='reset')return authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(action==='delete')return authF('/api/links/'+uuid,{method:'DELETE'});}));toast('انجام شد ✓','ok');if(action==='delete')selectedLinks.clear();loadLinks();}catch(e){toast('خطا','err')}}
let linkChart=null;
async function openLinkChart(uuid,label){document.getElementById('lc-title').textContent='نمودار مصرف — '+label;openModal('modal-link-chart');try{const r=await authF('/api/links/'+uuid+'/history'),d=await r.json();const labels=d.days.map(x=>x.date.slice(5));const vals=d.days.map(x=>+(x.bytes/1024**2).toFixed(2));const ctx=document.getElementById('lc-canvas');if(linkChart)linkChart.destroy();linkChart=new Chart(ctx,{type:'bar',data:{labels,datasets:[{label:'MB',data:vals,backgroundColor:'rgba(139,92,246,.55)',borderRadius:5,maxBarThickness:22}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false}},y:{beginAtZero:true}}}});}catch(e){toast('خطا','err')}}
async function createLink(){const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';const val=document.getElementById('nl-val').value;const unit=document.getElementById('nl-unit').value;const exp=document.getElementById('nl-exp').value;const note=document.getElementById('nl-note').value.trim();const protocol=document.getElementById('nl-proto').value||'vless-ws';const fingerprint=document.getElementById('nl-fp').value||'chrome';const alpn=document.getElementById('nl-alpn').value.trim();const port=443;const ip_limit=Number(document.getElementById('nl-iplimit').value)||0;const speed_limit_value=Number(document.getElementById('nl-speed').value)||0;const speed_limit_unit=document.getElementById('nl-speed-unit').value;try{const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,protocol,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit})});if(!r.ok)throw new Error();['nl-label','nl-val','nl-exp','nl-note','nl-alpn'].forEach(id=>document.getElementById(id).value='');document.getElementById('nl-iplimit').value='0';document.getElementById('nl-speed').value='0';document.getElementById('nl-alpn-preset').value='';document.getElementById('nl-alpn').style.display='none';toast('ساخته شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}}
function openEditLink(uuid){const l=allLinksList.find(x=>x.uuid===uuid);if(!l)return;document.getElementById('el-uuid').value=uuid;document.getElementById('el-label').value=l.label;document.getElementById('el-note').value=l.note||'';if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}document.getElementById('el-exp').value='';document.getElementById('el-fp').value=l.fingerprint||'chrome';document.getElementById('el-alpn').value=l.alpn||'';document.getElementById('el-port').value=l.port||443;document.getElementById('el-iplimit').value=l.ip_limit||0;if(!l.speed_limit_bytes){document.getElementById('el-speed').value='0';}else{document.getElementById('el-speed').value=(l.speed_limit_bytes*8/1024/1024).toFixed(2);}openModal('modal-edit-link');}
async function saveEditLink(){const uuid=document.getElementById('el-uuid').value;const label=document.getElementById('el-label').value.trim();const note=document.getElementById('el-note').value.trim();const val=document.getElementById('el-val').value;const unit=document.getElementById('el-unit').value;const exp=document.getElementById('el-exp').value;const fingerprint=document.getElementById('el-fp').value||'chrome';const alpn=document.getElementById('el-alpn').value.trim();const port=Number(document.getElementById('el-port').value)||443;const ip_limit=Number(document.getElementById('el-iplimit').value)||0;const speed_limit_value=Number(document.getElementById('el-speed').value)||0;const speed_limit_unit=document.getElementById('el-speed-unit').value;const body={label,note,limit_value:val||0,limit_unit:unit,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit};if(exp&&Number(exp)>0)body.expires_days=Number(exp);try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});if(!r.ok)throw new Error();closeModal('modal-edit-link');toast('ویرایش شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}}
async function toggleActive(uuid,newState){try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال ✓':'غیرفعال','ok');loadLinks();}catch(e){toast('خطا','err')}}
async function resetUsage(uuid){try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('ریست ✓','ok');loadLinks();}catch(e){toast('خطا','err')}}
async function deleteLink(uuid){if(!confirm('حذف؟'))return;try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
let connsExpanded=new Set();
function toggleConnCard(uuid){if(connsExpanded.has(uuid))connsExpanded.delete(uuid);else connsExpanded.add(uuid);renderConnsGrid(window.__lastConfigs||[]);}
function renderConnsGrid(configs){const grid=document.getElementById('conns-grid');grid.innerHTML=configs.map(cfg=>{const open=connsExpanded.has(cfg.uuid);const ipsHtml=(cfg.connections||[]).map(c=>{const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;const dur=secs<60?secs+' ث':secs<3600?Math.floor(secs/60)+' د':Math.floor(secs/3600)+' س';return '<div style="display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;border-radius:10px;background:var(--accent-d);border:1px solid rgba(139,92,246,0.12);margin-top:7px"><div style="display:flex;align-items:center;gap:8px;min-width:0"><i class="ti ti-device-desktop" style="color:var(--t3)"></i><span style="font-family:ui-monospace,monospace;font-size:12px;color:var(--t1)">'+esc(c.ip)+'</span></div><div style="display:flex;align-items:center;gap:12px;font-size:10.5px;color:var(--t3);flex-shrink:0"><span><i class="ti ti-repeat"></i> '+toFa(c.sessions)+' سشن</span><span><i class="ti ti-transfer"></i> '+esc(c.bytes_fmt)+'</span><span><i class="ti ti-clock"></i> '+dur+'</span></div></div>';}).join('')||'<div style="padding:10px;color:var(--t3);font-size:11px">اتصالی نیست</div>';return '<div class="conn-card-v2" style="cursor:pointer" onclick="toggleConnCard(\''+cfg.uuid+'\')"><div class="conn-card-v2-glow"></div><div class="conn-card-v2-top"><div class="conn-avatar"><i class="ti ti-key"></i></div><div class="conn-card-v2-id"><div class="conn-ip-v2">'+esc(cfg.label)+'</div><div class="conn-label-v2">'+toFa(cfg.ip_count)+' آی‌پی · '+toFa(cfg.sessions)+' سشن</div></div><span class="conn-status-pill"><span class="dot dg pulse"></span> زنده</span></div><div class="conn-card-v2-divider"></div><div class="conn-card-v2-body"><div class="conn-proto-row">'+protoBadge(cfg.protocol)+'</div><div class="conn-stat-row"><div class="conn-stat-box"><div class="conn-stat-icon"><i class="ti ti-transfer"></i></div><div><div class="conn-stat-text-label">ترافیک</div><div class="conn-stat-text-val">'+esc(cfg.bytes_fmt)+'</div></div></div><div class="conn-stat-box"><div class="conn-stat-icon time"><i class="ti ti-users"></i></div><div><div class="conn-stat-text-label">آی‌پی</div><div class="conn-stat-text-val">'+toFa(cfg.ip_count)+'</div></div></div></div><div style="text-align:center;font-size:10.5px;color:var(--accent2);margin-top:8px"><i class="ti ti-chevron-'+(open?'up':'down')+'"></i> '+(open?'بستن':'نمایش')+'</div>'+(open?'<div onclick="event.stopPropagation()">'+ipsHtml+'</div>':'')+'</div></div>';}).join('');}
async function loadConns(){try{const r=await authF('/api/connections'),d=await r.json();const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.raw_count+' اتصال';document.getElementById('ch-count').textContent=toFa(d.raw_count);const configs=d.configs||[];window.__lastConfigs=configs;if(!configs.length){grid.innerHTML='';ce.style.display='block';document.getElementById('ch-traffic').textContent='—';document.getElementById('ch-avgdur').textContent='—';document.getElementById('ch-uniq').textContent='—';renderConnFeed([]);return}ce.style.display='none';const totalBytes=configs.reduce((s,c)=>s+(c.bytes||0),0);document.getElementById('ch-traffic').textContent=fmtB(totalBytes);const uniqIps=configs.reduce((s,c)=>s+c.ip_count,0);document.getElementById('ch-uniq').textContent=toFa(uniqIps);const allDurs=[];configs.forEach(c=>(c.connections||[]).forEach(ip=>allDurs.push(ip.connected_at?Math.max(0,Math.floor((Date.now()-new Date(ip.connected_at).getTime())/1000)):0)));const avgSec=allDurs.length?Math.floor(allDurs.reduce((a,b)=>a+b,0)/allDurs.length):0;document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';renderConnsGrid(configs);renderConnFeed(configs);}catch(e){console.error(e)}}
function renderConnFeed(configs){const el=document.getElementById('conn-feed');if(!el)return;if(!configs.length){el.innerHTML='<div style="text-align:center;padding:20px;color:var(--t3);font-size:11px"><i class="ti ti-plug-off" style="font-size:24px;display:block;margin-bottom:8px"></i>اتصالی نیست</div>';return}let items=[];configs.forEach(c=>{(c.connections||[]).forEach(ip=>{items.push({ip:ip.ip,label:c.label,protocol:c.protocol,time:ip.connected_at})})});items.sort((a,b)=>(b.time||'').localeCompare(a.time||''));el.innerHTML=items.slice(0,12).map(it=>{const proto=it.protocol==='xhttp'?'<span class="feed-proto" style="background:var(--purple-bg);color:var(--purple)">XHTTP</span>':'<span class="feed-proto" style="background:var(--blue-bg);color:var(--blue)">VLESS</span>';const timeStr=it.time?new Date(it.time).toLocaleTimeString('fa-IR',{hour:'2-digit',minute:'2-digit'}):'—';return '<div class="feed-item"><div class="feed-dot"></div><span class="feed-ip" title="'+esc(it.ip)+'">'+esc(it.ip)+'</span>'+proto+'<span class="feed-time">'+timeStr+'</span></div>';}).join('');}
let cfgDashSelected=null;
async function loadCfgDash(){try{if(!allLinksList.length)await loadLinks();await loadConns();renderCfgDashList();if(cfgDashSelected&&allLinksList.some(l=>l.uuid===cfgDashSelected))renderCfgDashDetail(cfgDashSelected);}catch(e){console.error(e)}}
function renderCfgDashList(){const wrap=document.getElementById('cfgdash-list'),empty=document.getElementById('cfgdash-empty');document.getElementById('cfgdash-count').textContent=toFa(allLinksList.length);if(!allLinksList.length){wrap.innerHTML='';empty.style.display='block';return}empty.style.display='none';wrap.innerHTML=allLinksList.map(l=>{const allowed=l.active&&!l.expired;const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';return '<div class="cfgdash-item'+(cfgDashSelected===l.uuid?' on':'')+'" onclick="selectCfgDash(\''+l.uuid+'\')"><div class="cfgdash-item-top"><span class="cfg-status-dot '+(allowed?'pulse':'')+'"></span><span class="cfgdash-item-label">'+esc(l.label)+'</span>'+protoBadge(l.protocol)+'</div><div class="ubar"><div class="ubar-f" style="width:'+pct+'%;background:'+bc+'"></div></div><div class="utxt"><span>'+fmtB(l.used_bytes)+'</span><span>'+(l.connected_ips||0)+' آی‌پی</span></div></div>';}).join('');}
function selectCfgDash(uuid){cfgDashSelected=uuid;renderCfgDashList();renderCfgDashDetail(uuid)}
function renderCfgDashDetail(uuid){const box=document.getElementById('cfgdash-detail');const l=allLinksList.find(x=>x.uuid===uuid);if(!l){box.innerHTML='<div class="card"><div class="empty"><p>وجود ندارد</p></div></div>';return}const grp=(window.__lastConfigs||[]).find(c=>c.uuid===uuid);const ips=grp?grp.connections||[]:[];const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';const speedTxt=l.speed_limit_bytes?((l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps'):'نامحدود';box.innerHTML='<div class="card" style="margin-bottom:14px"><div class="card-title"><i class="ti ti-key"></i> '+esc(l.label)+' '+(l.active&&!l.expired?'<span class="badge bg-green" style="margin-right:6px">فعال</span>':'<span class="badge bg-red" style="margin-right:6px">'+(l.expired?'منقضی':'غیرفعال')+'</span>')+'</div><div class="cfgdash-stats"><div class="cfgdash-stat"><div class="cfgdash-stat-l">مصرف</div><div class="cfgdash-stat-v">'+fmtB(l.used_bytes)+'</div><div class="utxt" style="margin-top:6px"><span></span><span>از '+(l.limit_bytes===0?'∞':fmtB(l.limit_bytes))+'</span></div><div class="ubar" style="margin-top:6px"><div class="ubar-f" style="width:'+pct+'%;background:'+bc+'"></div></div></div><div class="cfgdash-stat"><div class="cfgdash-stat-l">سرعت</div><div class="cfgdash-stat-v" style="font-size:14px">'+speedTxt+'</div></div><div class="cfgdash-stat"><div class="cfgdash-stat-l">آی‌پی</div><div class="cfgdash-stat-v">'+toFa(l.connected_ips||0)+(l.ip_limit?(' / '+toFa(l.ip_limit)):' (∞)')+'</div></div><div class="cfgdash-stat"><div class="cfgdash-stat-l">انقضا</div><div class="cfgdash-stat-v" style="font-size:14px">'+expChip(l.expires_at,l.expired)+'</div></div></div></div><div class="card"><div class="card-title"><i class="ti ti-map-pin"></i> آی‌پی‌های متصل <span class="ml-auto badge bg-cyan">'+toFa(ips.length)+'</span></div>'+(ips.length?ips.map(c=>{const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;const dur=secs<60?secs+' ث':secs<3600?Math.floor(secs/60)+' د':Math.floor(secs/3600)+' س';return '<div class="cfgdash-ip-row"><span class="ip"><span class="dot dg pulse" style="width:7px;height:7px;border-radius:50%;background:var(--green);display:inline-block"></span> '+esc(c.ip)+'</span><div class="cfgdash-ip-meta"><span><i class="ti ti-repeat"></i> '+toFa(c.sessions)+' سشن</span><span><i class="ti ti-transfer"></i> '+esc(c.bytes_fmt)+'</span><span><i class="ti ti-clock"></i> '+dur+'</span></div></div>';}).join(''):'<div class="empty"><i class="ti ti-plug-off"></i><p>اتصالی نیست</p></div>')+'</div>';}
async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}
function refreshAll(){fetchStats();loadLinks();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('رفرش شد','ok')}
// Speed Test
async function runSpeedTest(){try{document.getElementById('st-speed').textContent='در حال تست...';document.getElementById('st-latency').textContent='...';const r=await authF('/api/speedtest/run',{method:'POST'});if(!r.ok)throw new Error();toast('تست شروع شد','ok');setTimeout(loadSpeedTest,2000);}catch(e){toast('خطا','err')}}
async function loadSpeedTest(){try{const r=await authF('/api/speedtest');const d=await r.json();document.getElementById('st-speed').textContent=d.speed_mbps||'—';document.getElementById('st-latency').textContent=d.latency_ms?d.latency_ms+'ms':'—';document.getElementById('st-time').textContent=d.last_test?new Date(d.last_test).toLocaleTimeString('fa-IR'):'—';}catch(e){console.error(e)}}

// Xray Update
async function checkXrayUpdate(){document.getElementById('xray-status').textContent='در حال بررسی...';try{const r=await authF('/api/system/xray-update');const d=await r.json();if(d.error){document.getElementById('xray-status').innerHTML='<span style="color:var(--red)">خطا: '+esc(d.error)+'</span>';return}document.getElementById('xray-cur').textContent=d.current_version||'—';document.getElementById('xray-latest').textContent=d.latest_version||'—';document.getElementById('xray-check-time').textContent=new Date().toLocaleTimeString('fa-IR');if(d.update_available){document.getElementById('xray-status').innerHTML='<span style="color:var(--amber)"><i class="ti ti-alert-triangle"></i> آپدیت موجود: '+esc(d.latest_version)+'</span>'}else{document.getElementById('xray-status').innerHTML='<span style="color:var(--green)"><i class="ti ti-circle-check"></i> آخرین نسخه نصب است</span>'}toast('بررسی شد','ok');}catch(e){toast('خطا','err')}}
async function installXrayUpdate(){if(!confirm('بروزرسانی Xray Core؟'))return;document.getElementById('xray-status').textContent='در حال بروزرسانی...';try{const r=await authF('/api/system/xray-update',{method:'POST'});if(!r.ok)throw new Error();toast('بروزرسانی شروع شد','ok');setTimeout(checkXrayUpdate,5000);}catch(e){toast('خطا','err')}}

async function changePw(){const cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;if(!cur||!nw||!cf){toast('پر کنید','err');return}if(nw.length<4){toast('حداقل ۴ کاراکتر','err');return}if(nw!==cf){toast('تکرار اشتباه','err');return}try{const r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});const d=await r.json().catch(()=>({}));if(!r.ok)throw new Error(d.detail||'خطا');toast('رمز تغییر کرد ✓','ok');['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='');}catch(e){toast('✗ '+e.message,'err')}}
function togglePwField(id,btn){const inp=document.getElementById(id);const icon=btn.querySelector('i');const toText=inp.type==='password';inp.type=toText?'text':'password';icon.className='ti '+(toText?'ti-eye-off':'ti-eye');}
function checkPwStrength(val){const segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');const label=document.getElementById('pw-strength-label');const reqLen=document.getElementById('req-len'),reqNum=document.getElementById('req-num'),reqCase=document.getElementById('req-case');const hasLen=val.length>=4,hasNum=/\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;reqLen.classList.toggle('met',hasLen);reqNum.classList.toggle('met',hasNum);reqCase.classList.toggle('met',hasCase);let score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;const colors=['#EF4444','#F59E0B','#3B82F6','#10B981'],labels=['ضعیف','ضعیف','متوسط','قوی'];segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,116,139,.2)'});if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> قدرت رمز';return}label.innerHTML='<i class="ti ti-shield-check" style="color:'+colors[Math.max(0,score-1)]+'"></i> '+labels[Math.max(0,score-1)];}
function initCharts(){
const c1=document.getElementById('ch1').getContext('2d');
ch1=new Chart(c1,{type:'bar',data:{labels:[],datasets:[{label:'MB',data:[],backgroundColor:function(ctx){const g=ctx.chart.ctx.createLinearGradient(0,0,0,280);g.addColorStop(0,'rgba(139,92,246,0.8)');g.addColorStop(1,'rgba(6,182,212,0.2)');return g},borderRadius:6,maxBarThickness:28,borderSkipped:false}]},options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(15,11,26,.96)',borderColor:'rgba(139,92,246,.3)',borderWidth:1,titleColor:'#E8F4FF',bodyColor:'#B0A0C8',padding:11,cornerRadius:10,displayColors:false,titleFont:{family:'Vazirmatn',size:11,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},callbacks:{label:function(v){return v.parsed.y.toFixed(2)+' MB'}}}},scales:{x:{grid:{display:false},border:{display:false},ticks:{color:'#6B5B80',font:{size:9,family:'Vazirmatn'}}},y:{grid:{color:'rgba(139,92,246,.06)'},border:{display:false},ticks:{color:'#6B5B80',font:{size:9,family:'Vazirmatn'},callback:function(v){return v+' MB'}}}}}});
ch2=new Chart(document.getElementById('ch2'),{type:'doughnut',data:{labels:['VLESS/WS','XHTTP Ultra'],datasets:[{data:[55,45],backgroundColor:['#3B82F6','#8B5CF6'],borderColor:'rgba(20,15,35,0.95)',borderWidth:4,hoverOffset:12,borderRadius:6,spacing:3}]},options:{responsive:true,maintainAspectRatio:false,cutout:'72%',plugins:{legend:{position:'bottom',labels:{color:'var(--t2)',font:{size:10,family:'Vazirmatn'},padding:12,usePointStyle:true,pointStyle:'circle'}},tooltip:{backgroundColor:'rgba(15,11,26,.96)',borderColor:'rgba(139,92,246,.3)',borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}},animation:{animateRotate:true,animateScale:true}}});
const c3ctx=document.getElementById('ch3').getContext('2d');const gradFill=c3ctx.createLinearGradient(0,0,0,320);gradFill.addColorStop(0,'rgba(139,92,246,.4)');gradFill.addColorStop(.6,'rgba(6,182,212,.08)');gradFill.addColorStop(1,'rgba(139,92,246,0)');
ch3=new Chart(c3ctx,{type:'line',data:{labels:[],datasets:[{label:'مصرف',data:[],borderColor:'#8B5CF6',backgroundColor:gradFill,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#8B5CF6',pointHoverBorderWidth:3,borderWidth:3,order:2},{label:'میانگین',data:[],borderColor:'#06B6D4',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}]},options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(15,11,26,.97)',borderColor:'rgba(139,92,246,.35)',borderWidth:1,titleColor:'#E8F4FF',bodyColor:'#B0A0C8',padding:13,cornerRadius:12,displayColors:true,boxPadding:4,titleFont:{family:'Vazirmatn',size:11.5,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},callbacks:{label:function(v){return ' '+v.dataset.label+': '+v.parsed.y.toFixed(2)+' MB'}}}},scales:{x:{grid:{display:false},border:{display:false},ticks:{color:'#6B5B80',font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},y:{grid:{color:'rgba(139,92,246,.05)'},border:{display:false},ticks:{color:'#6B5B80',font:{size:9.5,family:'Vazirmatn'},callback:function(v){return v+' MB'}}}}}});}
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log'),p=document.createElement('p');const colors={ok:'#34D399',err:'#F87171',info:'#B0A0C8',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('fa-IR')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','اتصال: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ متصل');ws.onerror=()=>wsLog('err','✗ خطا');ws.onmessage=m=>wsLog('info','دریافت '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','قطع ('+e.code+')')}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}
/* ═══════════════════════════════════════════════════════════════
   PWA - Progressive Web App
   ═══════════════════════════════════════════════════════════════ */
let deferredPrompt=null;
function initPWA(){
  if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js').catch(function(){});}
  window.addEventListener('beforeinstallprompt',function(e){e.preventDefault();deferredPrompt=e;if(!localStorage.getItem('x4g-pwa-dismissed')){document.getElementById('pwa-banner').classList.add('show');}});
  window.addEventListener('appinstalled',function(){deferredPrompt=null;document.getElementById('pwa-banner').classList.remove('show');toast('نصب شد ✓','ok');});
}
function installPWA(){if(!deferredPrompt){toast('از منوی مرورگر نصب کنید','');return;}deferredPrompt.prompt();deferredPrompt.userChoice.then(function(r){if(r.outcome==='accepted')toast('در حال نصب...','ok');deferredPrompt=null;document.getElementById('pwa-banner').classList.remove('show');});}
function dismissPWA(){document.getElementById('pwa-banner').classList.remove('show');localStorage.setItem('x4g-pwa-dismissed','1');}

/* ═══════════════════════════════════════════════════════════════
   NOTIFICATIONS - Real-Time Notifications
   ═══════════════════════════════════════════════════════════════ */
let notifList=[];
let notifWS=null;
let notifSoundEnabled=localStorage.getItem('x4g-notif-sound')!=='off';
let notifSound=null;
function initNotifications(){
  updateNotifSoundIcon();
  loadNotifsFromAPI();
  connectNotifWS();
  setInterval(loadNotifsFromAPI,15000);
}
function updateNotifSoundIcon(){var btn=document.getElementById('notif-sound-btn');if(!btn)return;btn.querySelector('i').className=notifSoundEnabled?'ti ti-volume':'ti ti-volume-off';}
function toggleNotifSound(){notifSoundEnabled=!notifSoundEnabled;localStorage.setItem('x4g-notif-sound',notifSoundEnabled?'on':'off');updateNotifSoundIcon();}
function playNotifSound(){if(!notifSoundEnabled)return;try{if(!notifSound){notifSound=new Audio('data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVgodDbsGczIj2NysijaT0oX53R3LBmMiA3kcnNrWo+L2Kc0d+0ZTIbMJPFy6tpOy9hndHgtmUxGC+RxcuqaTsvYp3R37RlMRktj8TLqmk7L2Kd0d+0ZTEZLY/DyalpOy9indHftGUxGS2Pw8mpaTsvYp3R37RlMRktj8PJqWk7L2Kd0d+0ZTEZLY/DyalpOy9indHftGUxGS2Pw8mpaTsvYp3R37RlMQ==');notifSound.volume=0.3;}notifSound.currentTime=0;notifSound.play().catch(function(){});}catch(e){}}
async function loadNotifsFromAPI(){try{var r=await authF('/api/notifications');if(!r.ok)return;var d=await r.json();var newNotifs=d.notifications||[];if(newNotifs.length>notifList.length){var added=newNotifs.filter(function(n){return !notifList.some(function(m){return m.id===n.id});});added.forEach(function(n){addNotif(n);playNotifSound();});}notifList=newNotifs;updateNotifBadge();renderNotifList();}catch(e){}}
function connectNotifWS(){try{var proto=location.protocol==='https:'?'wss':'ws';notifWS=new WebSocket(proto+'://'+location.host+'/ws/notifications');notifWS.onmessage=function(e){try{var data=JSON.parse(e.data);addNotif(data);playNotifSound();notifList.unshift(data);if(notifList.length>100)notifList.pop();updateNotifBadge();renderNotifList();}catch(err){}};notifWS.onclose=function(){setTimeout(connectNotifWS,5000);};notifWS.onerror=function(){};}catch(e){}}
function addNotif(n){if(!n.id)n.id='n'+Date.now()+'_'+Math.random().toString(36).slice(2,6);if(!n.time)n.time=new Date().toISOString();if(!notifList.some(function(m){return m.id===n.id;})){notifList.unshift(n);if(notifList.length>100)notifList.pop();}updateNotifBadge();renderNotifList();}
function updateNotifBadge(){var badge=document.getElementById('notif-badge');if(!badge)return;var unread=notifList.filter(function(n){return !n.read;}).length;badge.textContent=unread>99?'99+':(unread||'');badge.dataset.count=unread;badge.style.display=unread>0?'flex':'none';}
function renderNotifList(){var el=document.getElementById('notif-list');if(!el)return;if(!notifList.length){el.innerHTML='<div class="notif-empty"><i class="ti ti-bell-off"></i><p>اعلانی نیست</p></div>';return;}var iconMap={connection:{icon:'ti-plug-connected',cls:'conn'},disconnect:{icon:'ti-plug-x',cls:'disc'},expiry:{icon:'ti-alert-triangle',cls:'exp'},error:{icon:'ti-bug',cls:'err'},login:{icon:'ti-login-2',cls:'login'},info:{icon:'ti-info-circle',cls:'info'}};el.innerHTML=notifList.map(function(n){var type=n.type||'info';var ic=iconMap[type]||iconMap.info;var timeStr=n.time?new Date(n.time).toLocaleTimeString('fa-IR',{hour:'2-digit',minute:'2-digit'}):'';var unreadCls=n.read?'':' unread';return '<div class="notif-item'+unreadCls+'" onclick="markNotifRead(\''+n.id+'\')"><div class="notif-icon '+ic.cls+'"><i class="ti '+ic.icon+'"></i></div><div class="notif-body"><div class="notif-msg">'+esc(n.message||n.text||'')+'</div><div class="notif-time"><i class="ti ti-clock"></i> '+timeStr+'</div></div></div>';}).join('');}
function markNotifRead(id){var n=notifList.find(function(x){return x.id===id;});if(n)n.read=true;updateNotifBadge();renderNotifList();}
function clearAllNotifs(){notifList=[];updateNotifBadge();renderNotifList();toast('اعلان‌ها پاک شد','ok');}
function toggleNotifPanel(){var panel=document.getElementById('notif-panel');panel.classList.toggle('open');if(panel.classList.contains('open')){notifList.forEach(function(n){n.read=true;});updateNotifBadge();renderNotifList();}}
document.addEventListener('click',function(e){var panel=document.getElementById('notif-panel');var bell=document.getElementById('notif-bell');if(panel&&panel.classList.contains('open')&&!panel.contains(e.target)&&!bell.contains(e.target)){panel.classList.remove('open');}});

/* ═══════════════════════════════════════════════════════════════
   CUSTOM COLOR THEME
   ═══════════════════════════════════════════════════════════════ */
var themePresets={
  'default':{primary:'#8B5CF6',secondary:'#06B6D4',bg:'#0F0B1A',card:'#140F23'},
  'neon-purple':{primary:'#8B5CF6',secondary:'#06B6D4',bg:'#0F0B1A',card:'#140F23'},
  'ocean-blue':{primary:'#0EA5E9',secondary:'#3B82F6',bg:'#0A1628',card:'#0F2038'},
  'sunset-orange':{primary:'#F97316',secondary:'#EF4444',bg:'#1A0F0A',card:'#231A10'},
  'forest-green':{primary:'#10B981',secondary:'#059669',bg:'#0A1A14',card:'#102820'},
  'rose-pink':{primary:'#EC4899',secondary:'#F43F5E',bg:'#1A0A14',card:'#281020'}
};
function initCustomTheme(){var saved=localStorage.getItem('x4g-custom-theme');if(saved){try{var c=JSON.parse(saved);applyThemeColors(c);setPickerValues(c);highlightPreset(c.preset||'default');}catch(e){}}else{highlightPreset('default');}}
function applyPreset(name){var p=themePresets[name];if(!p)return;p.preset=name;applyThemeColors(p);setPickerValues(p);localStorage.setItem('x4g-custom-theme',JSON.stringify(p));highlightPreset(name);toast('تم اعمال شد ✓','ok');}
function applyThemeColors(c){var r=document.documentElement;r.style.setProperty('--accent',c.primary);r.style.setProperty('--accent2',c.secondary);r.style.setProperty('--accent-d',c.primary+'1a');r.style.setProperty('--cyan',c.secondary);r.style.setProperty('--cyan-d',c.secondary+'1a');r.style.setProperty('--bg',c.bg);r.style.setProperty('--bg2',lighten(c.bg,8));r.style.setProperty('--bg3',lighten(c.bg,15));r.style.setProperty('--card','rgba('+hexToRgb(c.card)+',0.95)');r.style.setProperty('--grad-border','linear-gradient(135deg,'+c.primary+','+c.secondary+')');r.style.setProperty('--card-b',c.primary+'26');r.style.setProperty('--card-bh',c.primary+'66');}
function setPickerValues(c){document.getElementById('tc-primary').value=c.primary;document.getElementById('tc-primary-val').textContent=c.primary;document.getElementById('tc-secondary').value=c.secondary;document.getElementById('tc-secondary-val').textContent=c.secondary;document.getElementById('tc-bg').value=c.bg;document.getElementById('tc-bg-val').textContent=c.bg;document.getElementById('tc-card').value=c.card;document.getElementById('tc-card-val').textContent=c.card;}
function previewCustomColor(){var c=getPickerValues();setPickerValues(c);applyThemeColors(c);}
function getPickerValues(){return{primary:document.getElementById('tc-primary').value,secondary:document.getElementById('tc-secondary').value,bg:document.getElementById('tc-bg').value,card:document.getElementById('tc-card').value};}
function applyCustomTheme(){var c=getPickerValues();c.preset='custom';localStorage.setItem('x4g-custom-theme',JSON.stringify(c));applyThemeColors(c);highlightPreset('custom');toast('رنگ اعمال شد ✓','ok');}
function resetTheme(){document.documentElement.removeAttribute('style');localStorage.removeItem('x4g-custom-theme');setPickerValues(themePresets['default']);highlightPreset('default');toast('بازگشت به پیش‌فرض','ok');}
function highlightPreset(name){document.querySelectorAll('.theme-preset').forEach(function(el){el.classList.toggle('active',el.dataset.preset===name);});}
function hexToRgb(hex){hex=hex.replace('#','');return[parseInt(hex.substring(0,2),16)+','+parseInt(hex.substring(2,4),16)+','+parseInt(hex.substring(4,6),16)];}
function lighten(hex,amt){hex=hex.replace('#','');var r=parseInt(hex.substring(0,2),16),g=parseInt(hex.substring(2,4),16),b=parseInt(hex.substring(4,6),16);r=Math.min(255,r+amt);g=Math.min(255,g+amt);b=Math.min(255,b+amt);return '#'+r.toString(16).padStart(2,'0')+g.toString(16).padStart(2,'0')+b.toString(16).padStart(2,'0');}
document.addEventListener('DOMContentLoaded',async()=>{
function initDailyCharts(){
const el7=document.getElementById('ch-daily7');if(!el7)return;
chDaily7=new Chart(el7.getContext('2d'),{type:'bar',data:{labels:[],datasets:[{label:'MB',data:[],backgroundColor:function(ctx){const g=ctx.chart.ctx.createLinearGradient(0,0,0,250);g.addColorStop(0,'rgba(139,92,246,0.8)');g.addColorStop(1,'rgba(6,182,212,0.2)');return g},borderRadius:6,maxBarThickness:36,borderSkipped:false}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(15,11,26,.96)',borderColor:'rgba(139,92,246,.3)',borderWidth:1,titleColor:'#E8F4FF',bodyColor:'#B0A0C8',padding:11,cornerRadius:10,displayColors:false,callbacks:{label:function(v){return fmtB(v.parsed.y*1024*1024)}}}},scales:{x:{grid:{display:false},border:{display:false},ticks:{color:'#6B5B80',font:{size:9,family:'Vazirmatn'}}},y:{grid:{color:'rgba(139,92,246,.06)'},border:{display:false},ticks:{color:'#6B5B80',font:{size:9,family:'Vazirmatn'},callback:function(v){return v+' MB'}}}}}});
const elP=document.getElementById('ch-proto-report');if(!elP)return;
chProtoReport=new Chart(elP,{type:'doughnut',data:{labels:['VLESS/WS','XHTTP'],datasets:[{data:[1,1],backgroundColor:['#3B82F6','#8B5CF6'],borderColor:'rgba(20,15,35,0.95)',borderWidth:3,hoverOffset:8}]},options:{responsive:true,maintainAspectRatio:false,cutout:'68%',plugins:{legend:{position:'bottom',labels:{color:'var(--t2)',font:{size:9,family:'Vazirmatn'},padding:8,usePointStyle:true,pointStyle:'circle'}},tooltip:{callbacks:{label:function(v){return v.label+': '+fmtB(v.raw)}}}}}});
const elU=document.getElementById('ch-uptime');if(!elU)return;
chUptimeChart=new Chart(elU,{type:'bar',data:{labels:[],datasets:[{label:'Restart #',data:[],backgroundColor:'rgba(6,182,212,0.5)',borderRadius:4,maxBarThickness:16}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false},border:{display:false},ticks:{color:'#6B5B80',font:{size:8,family:'Vazirmatn'},maxRotation:45}},y:{beginAtZero:true,grid:{color:'rgba(139,92,246,.06)'},border:{display:false},ticks:{color:'#6B5B80',font:{size:8,family:'Vazirmatn'}}}}}});}
async function loadTrafficReports(){
try{const r=await authF('/api/reports/traffic');const d=await r.json();
document.getElementById('rpt-today').textContent=d.today_fmt;
document.getElementById('rpt-yesterday').textContent=d.yesterday_fmt;
document.getElementById('rpt-thisweek').textContent=d.this_week_fmt;
document.getElementById('rpt-lastweek').textContent=d.last_week_fmt;
if(chDaily7&&d.last_7_days){const labels=Object.keys(d.last_7_days).sort().map(k=>k.slice(5));const vals=Object.keys(d.last_7_days).sort().map(k=>+(d.last_7_days[k]/1024/1024).toFixed(2));chDaily7.data.labels=labels;chDaily7.data.datasets[0].data=vals;chDaily7.update();}
if(chProtoReport&&d.protocol_breakdown){const pb=d.protocol_breakdown;const labels=Object.keys(pb);const vals=Object.values(pb);if(labels.length){chProtoReport.data.labels=labels;chProtoReport.data.datasets[0].data=vals;chProtoReport.update();}}}catch(e){console.error('traffic reports:',e)}}
async function loadConnectionMap(){
try{const r=await authF('/api/connections/map');const d=await r.json();const svg=document.getElementById('conn-map-svg');const legend=document.getElementById('map-legend');const listEl=document.getElementById('conn-map-list');if(!svg)return;
svg.innerHTML='';
// Draw simplified world outline
svg.innerHTML='<rect width="1000" height="500" fill="rgba(15,11,26,0.3)"/><ellipse cx="500" cy="250" rx="480" ry="230" fill="none" stroke="rgba(139,92,246,0.08)" stroke-width="1"/><ellipse cx="500" cy="250" rx="320" ry="230" fill="none" stroke="rgba(139,92,246,0.06)" stroke-width="1"/><line x1="20" y1="250" x2="980" y2="250" stroke="rgba(139,92,246,0.05)" stroke-width="0.5"/><line x1="500" y1="20" x2="500" y2="480" stroke="rgba(139,92,246,0.05)" stroke-width="0.5"/>';
const locs=d.locations||[];if(!locs.length){legend.innerHTML='اتصالی نیست';listEl.innerHTML='';return;}
let html='';const countryCounts={};
locs.forEach(l=>{if(!l.lat||!l.lon)return;
const x=((l.lon+180)/360)*1000;const y=((90-l.lat)/180)*500;
const r=Math.min(12,Math.max(4,l.count*2));
html+='<circle cx="'+x+'" cy="'+y+'" r="'+r+'" fill="rgba(139,92,246,0.6)" stroke="rgba(6,182,212,0.8)" stroke-width="1.5" opacity="0.85"><title>'+esc(l.ip)+' ('+esc(l.country)+')</title></circle>';
html+='<circle cx="'+x+'" cy="'+y+'" r="'+(r+4)+'" fill="none" stroke="rgba(139,92,246,0.2)" stroke-width="1"><animate attributeName="r" from="'+r+'" to="'+(r+10)+'" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" from="0.4" to="0" dur="2s" repeatCount="indefinite"/></circle>';
countryCounts[l.country]=(countryCounts[l.country]||0)+l.count;});
svg.innerHTML+=html;
legend.innerHTML='<span style="color:var(--accent)">●</span> '+toFa(locs.length)+' آی‌پی از '+toFa(Object.keys(countryCounts).length)+' کشور';
const sortedC=Object.entries(countryCounts).sort((a,b)=>b[1]-a[1]);
listEl.innerHTML=sortedC.map(([c,n])=>'<span style="display:inline-flex;align-items:center;gap:4px;background:var(--accent-d);border:1px solid rgba(139,92,246,0.12);border-radius:8px;padding:4px 10px;margin:3px;font-size:11px"><span style="font-size:13px">'+esc(c)+'</span><span style="color:var(--t3);font-weight:700">'+toFa(n)+'</span></span>').join('');}catch(e){console.error('conn map:',e)}}
async function loadPredictions(){
try{const r=await authF('/api/reports/predict');const d=await r.json();const el=document.getElementById('pred-cards');if(!el)return;const preds=d.predictions||[];
if(!preds.length){el.innerHTML='<div style="padding:10px;color:var(--t3);font-size:12px"><i class="ti ti-link-off"></i> کانفیگی نیست</div>';return;}
el.innerHTML=preds.slice(0,6).map(p=>{let quotaText='∞';let quotaColor='var(--accent)';if(p.days_until_quota!==null){quotaText=toFa(p.days_until_quota)+' روز';if(p.days_until_quota<=3)quotaColor='var(--red)';else if(p.days_until_quota<=7)quotaColor='var(--amber)';}
let expText='∞';let expColor='var(--accent)';if(p.days_until_expiry!==null){expText=toFa(p.days_until_expiry)+' روز';if(p.days_until_expiry<=3)expColor='var(--red)';else if(p.days_until_expiry<=7)expColor='var(--amber)';}
return '<div style="display:flex;align-items:center;justify-content:space-between;padding:9px 12px;border-bottom:1px solid rgba(139,92,246,0.06);font-size:12px"><span style="font-weight:700;color:var(--t1);flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">'+esc(p.label)+'</span><div style="display:flex;gap:12px;flex-shrink:0;margin-left:10px"><span style="font-size:10px;color:'+quotaColor+'"><i class="ti ti-gauge"></i> '+quotaText+'</span><span style="font-size:10px;color:'+expColor+'"><i class="ti ti-calendar"></i> '+expText+'</span></div></div>';}).join('');}catch(e){console.error('predictions:',e)}}
async function loadUptime(){
try{const r=await authF('/api/system/uptime');const d=await r.json();
document.getElementById('up-human').textContent=d.uptime_human;
document.getElementById('up-restarts').textContent=toFa(d.restart_count);
document.getElementById('up-start').textContent=new Date(d.start_time).toLocaleString('fa-IR');
if(chUptimeChart&&d.uptime_history&&d.uptime_history.length){
const labels=d.uptime_history.map(h=>{try{return new Date(h.time).toLocaleDateString('fa-IR',{month:'short',day:'numeric'})}catch(e){return ''}});
const vals=d.uptime_history.map(h=>h.restart_number||1);
chUptimeChart.data.labels=labels;chUptimeChart.data.datasets[0].data=vals;chUptimeChart.update();}}catch(e){console.error('uptime:',e)}}
document.addEventListener('DOMContentLoaded',async()=>{initParticles();await checkAuth();initCharts();initDailyCharts();document.getElementById('set-host').textContent=location.host;fetchStats();loadLinks();loadSpeedTest();checkXrayUpdate();loadTrafficReports();loadConnectionMap();loadPredictions();loadUptime();initNotifications();initPWA();initCustomTheme();setInterval(fetchStats,4000);setInterval(()=>{if(document.getElementById('pg-links').classList.contains('on'))loadLinks();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();if(document.getElementById('pg-cfgdash').classList.contains('on'))loadCfgDash();if(document.getElementById('pg-overview').classList.contains('on')){loadTrafficReports();loadConnectionMap();loadPredictions();loadUptime();}},8000);});
</script>
</body></html>"""



# جایگزینی نهایی لوگو در صفحات استاتیک
LOGIN_HTML = LOGIN_HTML.replace("__LOGO_B64__", LOGO_B64)
DASHBOARD_HTML = DASHBOARD_HTML.replace("__LOGO_B64__", LOGO_B64)


# pages_gold_v3.py - X4G v9.8 Cosmic Flow Design
# Redesigned public page with cosmic/glassmorphism design


def get_public_page_html(uuid_key: str) -> str:
    """صفحه پابلیک ساب — Cosmic Flow Design v3"""
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>X4G · Cosmic Flow</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{
  --bg:#05080F;--bg2:#0A1020;--bg3:#111D35;
  --glass:rgba(10,15,30,0.7);--glass-b:rgba(212,175,55,0.15);
  --mint:#D4AF37;--mint2:#FFD700;--mint-d:rgba(212,175,55,0.08);
  --purple:#7C3AED;--purple-d:rgba(124,58,237,0.1);
  --amber:#F59E0B;--amber-d:rgba(245,158,11,0.1);
  --red:#EF4444;--red-d:rgba(239,68,68,0.1);
  --blue:#3B82F6;--blue-d:rgba(59,130,246,0.1);
  --t1:#FFFFFF;--t2:#B0B0B0;--t3:#475569;
  --radius:20px;--shadow:0 16px 48px rgba(0,0,0,0.5);
  --serif:'Vazirmatn',sans-serif;
}}
[data-theme="light"]{{
  --bg:#F0F4FA;--bg2:#E2EAF6;--bg3:#D4DFF0;
  --glass:rgba(255,255,255,0.8);--glass-b:rgba(0,180,130,0.15);
  --mint:#059669;--mint2:#047857;--mint-d:rgba(5,150,105,0.08);
  --purple:#6D28D9;--purple-d:rgba(109,40,217,0.08);
  --amber:#D97706;--amber-d:rgba(217,119,6,0.08);
  --red:#DC2626;--red-d:rgba(220,38,38,0.08);
  --blue:#2563EB;--blue-d:rgba(37,99,235,0.08);
  --t1:#0F172A;--t2:#475569;--t3:#94A3B8;
  --shadow:0 12px 36px rgba(20,40,90,0.1);
}}
html,body{{min-height:100%;background:var(--bg);font-family:var(--serif);color:var(--t1);font-size:14px;transition:background .4s,color .4s;overflow-x:hidden}}
.nebula{{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}}
.nebula .orb{{position:absolute;border-radius:50%;filter:blur(120px);opacity:.6}}
.nebula .orb-1{{width:500px;height:500px;background:rgba(124,58,237,0.12);top:-150px;right:-120px;animation:nebDrift 18s ease-in-out infinite alternate}}
.nebula .orb-2{{width:400px;height:400px;background:rgba(212,175,55,0.06);bottom:-120px;left:-80px;animation:nebDrift 22s ease-in-out infinite alternate-reverse}}
.nebula .orb-3{{width:300px;height:300px;background:rgba(59,130,246,0.08);top:40%;left:30%;animation:nebDrift 16s ease-in-out infinite alternate}}
@keyframes nebDrift{{0%{{transform:translate(0,0) scale(1)}}100%{{transform:translate(50px,-40px) scale(1.2)}}}}
#particles{{position:fixed;inset:0;z-index:1;pointer-events:none;overflow:hidden}}
.particle{{position:absolute;width:2px;height:2px;background:var(--mint);border-radius:50%;opacity:0;animation:pFloat linear infinite}}
@keyframes pFloat{{0%{{transform:translateY(100vh) scale(0);opacity:0}}10%{{opacity:.5}}90%{{opacity:.5}}100%{{transform:translateY(-10vh) scale(1);opacity:0}}}}
[data-reveal]{{opacity:0;transform:translateY(32px);transition:opacity .65s cubic-bezier(.22,1,.36,1),transform .65s cubic-bezier(.22,1,.36,1)}}
[data-reveal].revealed{{opacity:1;transform:translateY(0)}}
[data-reveal]:nth-child(2){{transition-delay:.08s}}
[data-reveal]:nth-child(3){{transition-delay:.16s}}
[data-reveal]:nth-child(4){{transition-delay:.24s}}
.wrap{{position:relative;z-index:10;max-width:700px;margin:0 auto;padding:0 16px 90px}}
.hero{{text-align:center;padding:36px 0 28px;position:relative}}
.hero-logo{{width:68px;height:68px;border-radius:22px;margin:0 auto 14px;overflow:hidden;border:2px solid var(--glass-b);box-shadow:0 0 50px rgba(212,175,55,0.18),0 0 100px rgba(124,58,237,0.08);animation:heroGlow 3.5s ease-in-out infinite}}
@keyframes heroGlow{{0%,100%{{box-shadow:0 0 50px rgba(212,175,55,0.18),0 0 100px rgba(124,58,237,0.08)}}50%{{box-shadow:0 0 70px rgba(212,175,55,0.28),0 0 130px rgba(124,58,237,0.14)}}}}
.hero-logo img{{width:100%;height:100%;object-fit:cover}}
.hero-title{{font-size:28px;font-weight:800;background:linear-gradient(135deg,var(--mint),var(--purple));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;letter-spacing:-.02em}}
.hero-ver{{font-size:11px;color:var(--t3);margin-top:3px;letter-spacing:.08em}}
.hero-actions{{display:flex;justify-content:center;gap:8px;margin-top:16px}}
.icon-btn{{width:38px;height:38px;border-radius:12px;background:var(--glass);border:1px solid var(--glass-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:17px;cursor:pointer;transition:.2s;backdrop-filter:blur(16px)}}
.icon-btn:hover{{background:var(--mint-d);color:var(--mint);border-color:var(--mint)}}
.sub-card{{background:var(--glass);border:1px solid var(--glass-b);border-radius:var(--radius);padding:24px;margin-bottom:16px;backdrop-filter:blur(24px);position:relative;overflow:hidden}}
.sub-card::before{{content:'';position:absolute;top:0;right:0;width:180px;height:180px;background:radial-gradient(circle,rgba(212,175,55,0.08),transparent 70%);pointer-events:none}}
.sub-eyebrow{{font-size:10px;font-weight:700;color:var(--mint);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.sub-eyebrow i{{font-size:14px}}
.sub-name{{font-size:22px;font-weight:800;color:var(--t1);margin-bottom:6px;letter-spacing:-.02em}}
.sub-desc{{font-size:12px;color:var(--t2);line-height:1.8;margin-bottom:12px}}
.sub-meta{{font-size:10px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:5px}}
.sub-url-box{{background:var(--mint-d);border:1px solid var(--glass-b);border-radius:14px;padding:12px 14px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.sub-url{{font-family:ui-monospace,monospace;font-size:10px;color:var(--mint);word-break:break-all;flex:1;min-width:120px}}
.stats-strip{{display:flex;gap:10px;margin-bottom:20px;overflow-x:auto;scrollbar-width:none;padding:2px 0}}
.stats-strip::-webkit-scrollbar{{display:none}}
.stat-item{{flex:1;min-width:110px;background:var(--glass);border:1px solid var(--glass-b);border-radius:16px;padding:16px 14px;text-align:center;backdrop-filter:blur(20px);position:relative;overflow:hidden;transition:.2s}}
.stat-item:hover{{border-color:var(--mint);transform:translateY(-2px)}}
.stat-item::before{{content:'';position:absolute;inset:0;opacity:.06;pointer-events:none}}
.stat-item:nth-child(1)::before{{background:linear-gradient(135deg,var(--mint),transparent)}}
.stat-item:nth-child(2)::before{{background:linear-gradient(135deg,var(--blue),transparent)}}
.stat-item:nth-child(3)::before{{background:linear-gradient(135deg,var(--purple),transparent)}}
.stat-icon{{font-size:20px;margin-bottom:8px;color:var(--mint);filter:drop-shadow(0 0 8px rgba(212,175,55,0.3))}}
.stat-item:nth-child(2) .stat-icon{{color:var(--blue);filter:drop-shadow(0 0 8px rgba(59,130,246,0.3))}}
.stat-item:nth-child(3) .stat-icon{{color:var(--purple);filter:drop-shadow(0 0 8px rgba(124,58,237,0.3))}}
.stat-num{{font-size:28px;font-weight:700;color:var(--t1);line-height:1;font-variant-numeric:tabular-nums}}
.stat-label{{font-size:9px;color:var(--t3);text-transform:uppercase;letter-spacing:.1em;margin-top:6px;font-weight:600}}
.stat-online{{display:inline-flex;align-items:center;gap:4px;font-size:9px;color:var(--mint2);font-weight:700;margin-top:4px}}
.sec-title{{font-size:11px;font-weight:800;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.1em}}
.sec-title i{{color:var(--mint);font-size:16px}}
.cfg-card{{background:var(--glass);border:1px solid var(--glass-b);border-radius:var(--radius);backdrop-filter:blur(24px);position:relative;overflow:hidden;margin-bottom:14px;transition:all .3s cubic-bezier(.22,1,.36,1);animation:cardBreathe 4s ease-in-out infinite}}
.cfg-card:nth-child(even){{animation-delay:2s}}
@keyframes cardBreathe{{0%,100%{{box-shadow:0 0 20px rgba(212,175,55,0.03)}}50%{{box-shadow:0 0 35px rgba(212,175,55,0.08)}}}}
.cfg-card:hover{{border-color:var(--mint);transform:translateY(-3px);box-shadow:0 20px 50px rgba(0,0,0,0.3),0 0 30px rgba(212,175,55,0.08)}}
.cfg-card.inactive{{opacity:.65;animation:none}}
.cfg-card.inactive:hover{{border-color:var(--red);box-shadow:0 0 20px rgba(239,68,68,0.08)}}
.cfg-watermark{{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:100px;color:var(--mint);opacity:.03;pointer-events:none;z-index:0;filter:blur(2px)}}
.cfg-status-pill{{position:absolute;top:14px;left:14px;display:flex;align-items:center;gap:4px;font-size:9px;font-weight:700;padding:4px 10px;border-radius:20px;z-index:2;backdrop-filter:blur(8px)}}
.cfg-status-pill.ok{{background:rgba(212,175,55,0.15);color:var(--mint);border:1px solid rgba(212,175,55,0.2)}}
.cfg-status-pill.no{{background:var(--red-d);color:var(--red);border:1px solid rgba(239,68,68,0.2)}}
.cfg-card-body{{padding:20px;position:relative;z-index:1}}
.cfg-card-top{{display:flex;align-items:flex-start;gap:14px;margin-bottom:14px}}
.usage-donut{{width:56px;height:56px;border-radius:50%;position:relative;flex-shrink:0;display:flex;align-items:center;justify-content:center}}
.usage-donut svg{{position:absolute;inset:0;width:100%;height:100%;transform:rotate(-90deg)}}
.usage-donut circle{{fill:none;stroke-width:4}}
.usage-donut .ring-bg{{stroke:rgba(212,175,55,0.08)}}
.usage-donut .ring-fg{{stroke-linecap:round;transition:stroke-dashoffset .8s cubic-bezier(.22,1,.36,1)}}
.usage-donut .ring-pct{{font-size:13px;font-weight:800;color:var(--mint);position:relative;z-index:1}}
.cfg-card-info{{flex:1;min-width:0}}
.cfg-label{{font-size:15px;font-weight:700;color:var(--t1);margin-bottom:6px}}
.cfg-badges{{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:8px}}
.proto-chip{{font-size:9px;padding:3px 8px;border-radius:7px;font-weight:800;letter-spacing:.02em}}
.pc-ws{{background:var(--blue-d);color:var(--blue)}}
.pc-xhttp{{background:var(--purple-d);color:var(--purple)}}
.pc-ultra{{background:var(--mint-d);color:var(--mint)}}
.conn-chip{{display:inline-flex;align-items:center;gap:4px;font-size:9px;padding:3px 8px;border-radius:20px;background:var(--mint-d);color:var(--mint);font-weight:700}}
.dot{{width:5px;height:5px;border-radius:50%;background:var(--mint);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.2}}}}
.cfg-usage-text{{font-size:10px;color:var(--t3);display:flex;justify-content:space-between;margin-top:4px}}
.cfg-actions{{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding-top:12px;border-top:1px solid var(--glass-b);margin-top:4px}}
.cfg-actions::-webkit-scrollbar{{display:none}}
.btn{{font-family:inherit;font-size:11px;font-weight:700;border-radius:10px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .18s;white-space:nowrap;flex-shrink:0}}
.btn i{{font-size:13px}}
.btn-mint{{background:linear-gradient(135deg,var(--mint),var(--mint2));color:#05080F;box-shadow:0 3px 14px rgba(212,175,55,0.3)}}
.btn-mint:hover{{box-shadow:0 6px 24px rgba(212,175,55,0.45);transform:translateY(-1px)}}
.btn-glass{{background:var(--glass);color:var(--t2);border:1px solid var(--glass-b);backdrop-filter:blur(8px)}}
.btn-glass:hover{{background:var(--mint-d);color:var(--mint);border-color:var(--mint)}}
.btn-purple{{background:var(--purple-d);color:var(--purple);border:1px solid rgba(124,58,237,0.2)}}
.btn-purple:hover{{background:rgba(124,58,237,0.2)}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px dashed var(--glass-b);border-radius:11px;padding:10px 13px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:11px;font-weight:600;transition:.18s}}
.cfg-link-toggle:hover{{background:var(--mint-d);border-color:var(--mint);color:var(--mint)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .25s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .3s cubic-bezier(.22,1,.36,1)}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,.25);border:1px solid var(--glass-b);border-radius:10px;padding:11px 13px;font-size:9.5px;font-family:ui-monospace,monospace;color:var(--mint);word-break:break-all;line-height:1.7;margin-top:9px;max-height:88px;overflow-y:auto}}
[data-theme="light"] .cfg-vless{{background:rgba(212,175,55,0.04)}}
.fab{{position:fixed;bottom:24px;left:24px;width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,var(--mint),var(--purple));border:none;color:#fff;font-size:22px;cursor:pointer;z-index:100;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 28px rgba(212,175,55,0.35);transition:all .3s cubic-bezier(.22,1,.36,1)}}
.fab:hover{{transform:scale(1.1);box-shadow:0 8px 40px rgba(212,175,55,0.5)}}
.fab:active{{transform:scale(.95)}}
.fab .fab-count{{position:absolute;top:-4px;right:-4px;background:var(--red);color:#fff;font-size:10px;font-weight:800;min-width:20px;height:20px;border-radius:10px;display:flex;align-items:center;justify-content:center;padding:0 5px;box-shadow:0 2px 8px rgba(239,68,68,0.4)}}
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:70vh;padding:20px 0}}
.lock-card{{background:var(--glass);border:1px solid var(--glass-b);border-radius:26px;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow);overflow:hidden;position:relative;backdrop-filter:blur(24px)}}
.lock-banner{{background:linear-gradient(150deg,rgba(212,175,55,0.08),rgba(124,58,237,0.05) 70%);padding:36px 28px 24px;position:relative}}
.lock-shield{{width:60px;height:60px;border-radius:18px;background:var(--mint-d);border:1px solid var(--glass-b);display:flex;align-items:center;justify-content:center;margin:0 auto 16px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-8px;border-radius:22px;border:1px solid var(--glass-b);animation:breathe 2.8s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.5}}50%{{transform:scale(1.1);opacity:0}}}}
.lock-shield i{{font-size:26px;color:var(--mint)}}
.lock-title{{font-size:17px;font-weight:800;margin-bottom:5px;color:var(--t1)}}
.lock-sub{{font-size:11.5px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:22px 28px 28px}}
.lock-field{{position:relative;margin-bottom:12px}}
.lock-inp{{width:100%;padding:13px 44px;border-radius:13px;border:1px solid var(--glass-b);background:rgba(0,0,0,.25);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.14em;transition:.2s}}
[data-theme="light"] .lock-inp{{background:rgba(212,175,55,0.03)}}
.lock-inp:focus{{border-color:var(--mint);box-shadow:0 0 0 3px var(--mint-d)}}
.lock-eye{{position:absolute;left:13px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--mint)}}
.lock-lockicon{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none}}
.lock-err{{color:var(--red);font-size:11px;margin-bottom:10px;min-height:16px;display:flex;align-items:center;justify-content:center;gap:5px}}
.lock-btn{{width:100%;justify-content:center;padding:13px;font-size:13px;border-radius:13px}}
.lock-footer{{padding:12px 28px;border-top:1px solid var(--glass-b);font-size:10px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}}
.toast{{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--glass);border:1px solid var(--glass-b);color:var(--t1);border-radius:14px;padding:10px 22px;font-size:12px;font-weight:600;opacity:0;transition:all .3s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow);white-space:nowrap;backdrop-filter:blur(16px)}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(212,175,55,0.3);background:var(--mint-d);color:var(--mint)}}
.qr-modal{{display:none;position:fixed;inset:0;background:rgba(5,8,15,0.85);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(8px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--glass);border:1px solid var(--glass-b);border-radius:22px;padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow);backdrop-filter:blur(24px)}}
.qr-title{{font-size:13px;font-weight:800;margin-bottom:16px;color:var(--t1)}}
.qr-img{{border-radius:14px;overflow:hidden;margin-bottom:15px}}
.qr-img img{{width:100%;display:block;background:#FFD700;padding:10px;border-radius:14px}}
.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:38px;display:block;margin-bottom:14px}}
.footer{{text-align:center;padding:24px 0 0;font-size:10px;color:var(--t3)}}
.footer a{{color:var(--mint);font-weight:700}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(24px)}}to{{opacity:1;transform:translateY(0)}}}}
@media(max-width:520px){{.wrap{{padding:0 12px 80px}}.hero{{padding:28px 0 22px}}.hero-title{{font-size:24px}}.stat-num{{font-size:24px}}.sub-name{{font-size:19px}}.cfg-card-body{{padding:16px}}.fab{{bottom:20px;left:20px;width:52px;height:52px;font-size:20px}}}}
</style>
</head>
<body>
<div class="nebula"><div class="orb orb-1"></div><div class="orb orb-2"></div><div class="orb orb-3"></div></div>
<div id="particles"></div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-glass" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <header class="hero" data-reveal>
    <div class="hero-logo"><img src="data:image/png;base64,{LOGO_B64}" alt="X4G"></div>
    <div class="hero-title">X4G</div>
    <div class="hero-ver">v9.8 · Cosmic Flow</div>
    <div class="hero-actions">
      <button class="icon-btn" id="theme-toggle" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-sun" id="theme-icon"></i></button>
    </div>
  </header>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
  </div>
  <div class="footer">پشتیبانی: <a href="https://t.me/X4GHUB" target="_blank">@X4GHUB</a> · X4G v9.8</div>
</div>
<button class="fab" id="fab" onclick="copyAllConfigs()" title="کپی همه" style="display:none"><i class="ti ti-clipboard-copy"></i><span class="fab-count" id="fab-count" style="display:none">0</span></button>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';

let isDark=localStorage.getItem('x4g-pub-theme')!=='light';
function applyTheme(dark){{
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  document.getElementById('theme-icon').className='ti '+(dark?'ti-sun':'ti-moon');
}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('x4g-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);

function toast(msg,type=''){{
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}}
function esc(s){{return String(s||'')..pc-xhttp{background:var(--purple-bg);color:var(--purple)}(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}})[c])}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n)..pc-xhttp{background:var(--purple-bg);color:var(--purple)}(/\d/g,d=>'\u06f0\u06f1\u06f2\u06f3\u06f4\u06f5\u06f6\u06f7\u06f8\u06f9'[d])}}
function protoChip(p){{
  if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp"><i class="ti ti-bolt"></i> XHTTP \u00b7 auto</span>';
  return '<span class="proto-chip pc-ws">VLESS \u00b7 WS</span>';
}}

function showQR(label,link){{
  document.getElementById('qr-label').textContent=label;
  document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);
  document.getElementById('qr-modal').classList.add('open');
}}

function toggleLink(i){{
  const wrap=document.getElementById('vw-'+i);
  const btn=document.getElementById('vt-'+i);
  const open=wrap.classList.toggle('open');
  btn.classList.toggle('open',open);
  btn.querySelector('.ltl span').textContent = open ? '\u067e\u0646\u0647\u0627\u0646 \u06a9\u0631\u062f\u0646 \u0644\u06cc\u0646\u06a9' : '\u0646\u0645\u0627\u06cc\u0634 \u0644\u06cc\u0646\u06a9 \u06a9\u0627\u0646\u0641\u06cc\u06af';
}}

async function loadData(pw=''){{
  const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');
  const r=await fetch(url);
  return r.json();
}}

function renderLock(name,errMsg=''){{
  document.getElementById('root').innerHTML=`
    <div class="lock-stage">
      <div class="lock-card">
        <div class="lock-banner">
          <div class="lock-shield"><i class="ti ti-shield-lock"></i></div>
          <div class="lock-title">${{esc(name)}}</div>
          <div class="lock-sub">\u0627\u06cc\u0646 \u06af\u0631\u0648\u0647 \u0628\u0627 \u0631\u0645\u0632 \u0645\u062d\u0627\u0641\u0638\u062a \u0634\u062f\u0647. \u0628\u0631\u0627\u06cc \u062f\u06cc\u062f\u0646 \u06a9\u0627\u0646\u0641\u06cc\u06af\u200c\u0647\u0627 \u0631\u0645\u0632 \u0631\u0648 \u0648\u0627\u0631\u062f \u06a9\u0646\u06cc\u062f.</div>
        </div>
        <div class="lock-form">
          <div class="lock-err" id="lock-err">${{errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : ''}}</div>
          <div class="lock-field">
            <i class="ti ti-lock lock-lockicon"></i>
            <input class="lock-inp" type="password" id="lock-pw" placeholder="\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022" autofocus>
            <button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button>
          </div>
          <button class="btn btn-mint lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> \u0648\u0631\u0648\u062f \u0628\u0647 \u06af\u0631\u0648\u0647</button>
        </div>
        <div class="lock-footer"><i class="ti ti-shield-check"></i> \u0627\u062a\u0635\u0627\u0644 \u0634\u0645\u0627 \u0631\u0645\u0632\u0646\u06af\u0627\u0631\u06cc\u200c\u0634\u062f\u0647 \u0627\u0633\u062a</div>
      </div>
    </div>
  `;
  const inp=document.getElementById('lock-pw');
  inp.addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock()}});
}}

function togglePwVis(){{
  const inp=document.getElementById('lock-pw');
  const icon=document.getElementById('lock-eye-icon');
  const toText = inp.type==='password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti '+(toText ? 'ti-eye-off' : 'ti-eye');
}}

async function submitLock(){{
  const pw=document.getElementById('lock-pw').value;
  const data=await loadData(pw);
  if(data.locked){{renderLock(data.name,'\u0631\u0645\u0632 \u0627\u0634\u062a\u0628\u0627\u0647 \u0627\u0633\u062a');return}}
  savedPw=pw;
  renderContent(data);
}}

function renderContent(d){{
  const activeCount=d.links.filter(l=>l.active).length;
  const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/p/' + UUID_KEY);
  const subUrl = baseSubUrl;

  window._x4gSubUrl  = subUrl;
  window._x4gSubName = d.name;
  window._x4gLinks   = d.links.map(l => ({{
    vless : l.vless_link,
    sub   : l.sub_url,
    label : l.label,
  }}));

  const fab=document.getElementById('fab');
  const fabCount=document.getElementById('fab-count');
  if(activeCount>0){{
    fab.style.display='flex';
    fabCount.textContent=toFa(activeCount);
    fabCount.style.display='flex';
  }}else{{
    fab.style.display='none';
  }}

  document.getElementById('root').innerHTML=`
    <div class="sub-card" data-reveal>
      <div class="sub-eyebrow"><i class="ti ti-folders"></i> \u06af\u0631\u0648\u0647 \u062f\u0633\u062a\u0631\u0633\u06cc</div>
      <div class="sub-name">${{esc(d.name)}}</div>
      ${{d.desc ? `<div class="sub-desc">${{esc(d.desc)}}</div>` : ''}}
      <div class="sub-meta"><i class="ti ti-clock"></i> \u0622\u062e\u0631\u06cc\u0646 \u0628\u0631\u0648\u0632\u0631\u0633\u0627\u0646\u06cc: ${{new Date().toLocaleTimeString('fa-IR')}}</div>
      <div class="sub-url-box">
        <span class="sub-url">${{esc(subUrl)}}</span>
        <button class="btn btn-purple" style="padding:7px 12px;font-size:10px"
          onclick="navigator.clipboard.writeText(window._x4gSubUrl).then(()=>toast('\u0644\u06cc\u0646\u06a9 \u0633\u0627\u0628 \u06a9\u067e\u06cc \u0634\u062f \u2713','ok'))">
          <i class="ti ti-copy"></i> \u06a9\u067e\u06cc \u0644\u06cc\u0646\u06a9 \u0633\u0627\u0628
        </button>
        <button class="btn btn-glass" style="padding:7px 12px;font-size:10px"
          onclick="showQR(window._x4gSubName + ' \u2014 \u06a9\u0644 \u06af\u0631\u0648\u0647', window._x4gSubUrl)">
          <i class="ti ti-qrcode"></i> QR \u06a9\u0644
        </button>
      </div>
    </div>

    <div class="stats-strip" data-reveal>
      <div class="stat-item">
        <div class="stat-icon"><i class="ti ti-link"></i></div>
        <div class="stat-num" data-count="${{activeCount}}">${{toFa(activeCount)}}</div>
        <div class="stat-label">\u06a9\u0627\u0646\u0641\u06cc\u06af \u0641\u0639\u0627\u0644</div>
      </div>
      <div class="stat-item">
        <div class="stat-icon"><i class="ti ti-trending-up"></i></div>
        <div class="stat-num" data-count="${{d.active_connections}}">${{toFa(d.active_connections)}}</div>
        <div class="stat-label">\u0627\u062a\u0635\u0627\u0644 \u0632\u0646\u062f\u0647</div>
        <div class="stat-online"><span class="dot"></span> \u0622\u0646\u0644\u0627\u06cc\u0646</div>
      </div>
      <div class="stat-item">
        <div class="stat-icon"><i class="ti ti-database"></i></div>
        <div class="stat-num" style="font-size:18px">${{esc(d.total_used_fmt)}}</div>
        <div class="stat-label">\u06a9\u0644 \u0645\u0635\u0631\u0641</div>
      </div>
    </div>

    <div class="sec-title" data-reveal><i class="ti ti-link"></i> \u06a9\u0627\u0646\u0641\u06cc\u06af\u200c\u0647\u0627 (${{toFa(d.links.length)}} \u0639\u062f\u062f)</div>
    <div class="cfg-grid">
      ${{d.links.map((l, i) => {{
        const pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
        const bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--mint)';
        const lim = l.limit_bytes === 0 ? '\u221e' : fmtB(l.limit_bytes);
        const circumference = 2 * Math.PI * 22;
        const dashoffset = circumference - (pct / 100) * circumference;
        const wmIcon = (l.protocol && l.protocol.startsWith('xhttp')) ? 'ti-bolt' : 'ti-world';
        return `
          <div class="cfg-card${{l.active ? '' : ' inactive'}}" data-reveal>
            <i class="ti ${{wmIcon}} cfg-watermark"></i>
            <span class="cfg-status-pill ${{l.active ? 'ok' : 'no'}}">${{l.active ? '<i class="ti ti-circle-check"></i> \u0641\u0639\u0627\u0644' : '<i class="ti ti-circle-x"></i> \u063a\u06cc\u0631\u0641\u0639\u0627\u0644'}}</span>
            <div class="cfg-card-body">
              <div class="cfg-card-top">
                <div class="usage-donut">
                  <svg viewBox="0 0 50 50">
                    <circle class="ring-bg" cx="25" cy="25" r="22"/>
                    <circle class="ring-fg" cx="25" cy="25" r="22" stroke="${{bc}}" stroke-dasharray="${{circumference}}" stroke-dashoffset="${{dashoffset}}"/>
                  </svg>
                  <span class="ring-pct" style="color:${{bc}}">${{pct > 0 ? Math.round(pct)+'%' : '\u221e'}}</span>
                </div>
                <div class="cfg-card-info">
                  <div class="cfg-label">${{esc(l.label)}}</div>
                  <div class="cfg-badges">
                    ${{protoChip(l.protocol)}}
                    ${{l.connections > 0 ? `<span class="conn-chip"><span class="dot"></span> ${{toFa(l.connections)}} \u0627\u062a\u0635\u0627\u0644</span>` : ''}}
                  </div>
                  <div class="cfg-usage-text"><span>${{esc(l.used_fmt)}} \u0645\u0635\u0631\u0641</span><span>\u0633\u0647\u0645\u06cc\u0647: ${{lim}}</span></div>
                </div>
              </div>
              <div class="cfg-actions">
                <button class="btn btn-mint"
                  onclick="navigator.clipboard.writeText(window._x4gLinks[${{i}}].vless).then(()=>toast('\u0644\u06cc\u0646\u06a9 \u06a9\u067e\u06cc \u0634\u062f \u2713','ok'))">
                  <i class="ti ti-copy"></i> \u06a9\u067e\u06cc \u0644\u06cc\u0646\u06a9
                </button>
                <button class="btn btn-glass"
                  onclick="showQR(window._x4gLinks[${{i}}].label, window._x4gLinks[${{i}}].vless)">
                  <i class="ti ti-qrcode"></i> QR
                </button>
                <button class="btn btn-glass cfg-link-toggle" id="vt-${{i}}" onclick="toggleLink(${{i}})" style="border:none">
                  <span class="ltl"><i class="ti ti-eye"></i> <span>\u0646\u0645\u0627\u06cc\u0634 \u0644\u06cc\u0646\u06a9</span></span>
                  <i class="ti ti-chevron-down"></i>
                </button>
              </div>
              <div class="cfg-vless-wrap" id="vw-${{i}}">
                <div class="cfg-vless-inner">
                  <div class="cfg-vless">${{esc(l.vless_link)}}</div>
                </div>
              </div>
            </div>
          </div>
        `;
      }}).join('')}}
    </div>
  `;

  initReveal();
  animateCounters();
  setTimeout(() => autoRefresh(), 30000);
}}

function copyAllConfigs(){{
  const links=window._x4gLinks||[];
  if(!links.length){{toast('\u06a9\u0627\u0646\u0641\u06cc\u06af\u06cc \u0628\u0631\u0627\u06cc \u06a9\u067e\u06cc \u0646\u0633\u062a','');return}}
  const text=links.map(l=>l.vless).join('\\n');
  navigator.clipboard.writeText(text).then(()=>toast('\u0647\u0645\u0647\u200c\u06cc '+toFa(links.length)+' \u06a9\u0627\u0646\u0641\u06cc\u06af \u06a9\u067e\u06cc \u0634\u062f \u2713','ok'));
}}

async function autoRefresh(){{
  try{{
    const data = await loadData(savedPw);
    if (!data.locked) renderContent(data);
  }} catch(e) {{}}
}}

function createParticles(){{
  const c=document.getElementById('particles');
  if(!c)return;
  for(let i=0;i<28;i++){{
    const p=document.createElement('div');
    p.className='particle';
    p.style.left=Math.random()*100+'%';
    p.style.animationDuration=(10+Math.random()*18)+'s';
    p.style.animationDelay=Math.random()*12+'s';
    const sz=1.5+Math.random()*3;
    p.style.width=sz+'px';p.style.height=sz+'px';
    if(Math.random()>.6)p.style.background='var(--purple)';
    if(Math.random()>.85)p.style.background='var(--blue)';
    c.appendChild(p);
  }}
}}

let revealObs;
function initReveal(){{
  if(!revealObs){{
    revealObs=new IntersectionObserver((entries)=>{{
      entries.forEach(e=>{{
        if(e.isIntersecting){{
          e.target.classList.add('revealed');
          revealObs.unobserve(e.target);
        }}
      }});
    }},{{threshold:0.12}});
  }}
  document.querySelectorAll('[data-reveal]:not(.revealed)').forEach(el=>revealObs.observe(el));
}}

function animateCounters(){{
  document.querySelectorAll('.stat-num[data-count]').forEach(el=>{{
    const target=parseInt(el.dataset.count);
    if(isNaN(target)||target===0)return;
    let current=0;
    const step=Math.max(1,Math.ceil(target/30));
    const timer=setInterval(()=>{{
      current+=step;
      if(current>=target){{current=target;clearInterval(timer)}}
      el.textContent=toFa(current);
    }},30);
  }});
}}

async function init(){{
  createParticles();
  initReveal();
  try{{
    const data = await loadData();
    if (data.locked) {{ renderLock(data.name); return; }}
    renderContent(data);
  }} catch(e) {{
    document.getElementById('root').innerHTML =
      '<div class="empty-state" style="color:var(--red)"><i class="ti ti-alert-circle"></i>\u062e\u0637\u0627 \u062f\u0631 \u0628\u0627\u0631\u06af\u0630\u0627\u0631\u06cc</div>';
  }}
}}

init();
</script>
</body>
</html>"""
