# pages.py  -  SPIDER PANEL v1.0 RTL Persian
# Contains: LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · SPIDER PANEL</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#F8F9FA;--card-bg:#FFFFFF;--text:#1E272E;--text-dim:#636E72;--accent:#2B66FF;--accent-red:#FF3B65;--border:#E2E8F0;--radius:20px}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px;transition:background .4s}
.bg-layer{position:fixed;inset:0;z-index:0;pointer-events:none}
.bg-layer svg{position:absolute}
.bg-layer svg.tl{top:-80px;right:-60px;opacity:.03;width:380px;height:380px}
.bg-layer svg.br{bottom:-80px;left:-60px;opacity:.03;width:340px;height:340px}
.wrap{position:relative;z-index:10;width:100%;max-width:440px}
.card{background:var(--card-bg);border:1px solid var(--border);border-radius:var(--radius);padding:42px 38px 38px;box-shadow:0 8px 40px rgba(0,0,0,0.08),0 0 0 1px rgba(0,0,0,0.02);transition:all .3s}
.card:hover{box-shadow:0 12px 48px rgba(0,0,0,0.12)}
.spider-logo{display:flex;align-items:center;justify-content:center;margin-bottom:4px}
.spider-svg{width:56px;height:56px}
.brand-row{text-align:center;margin-bottom:8px}
.brand-name{font-size:26px;font-weight:800;letter-spacing:-.02em;background:linear-gradient(135deg,#2B66FF,#FF3B65);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.separator{width:50px;height:3px;background:linear-gradient(135deg,#2B66FF,#FF3B65);border-radius:3px;margin:22px auto}
.welcome{font-size:17px;font-weight:700;color:var(--text);margin-bottom:6px;text-align:center}
.subtitle{font-size:12px;color:var(--text-dim);margin-bottom:26px;text-align:center;line-height:1.6}
.hint-box{display:flex;align-items:center;gap:10px;background:rgba(43,102,255,0.05);border:1px solid rgba(43,102,255,0.12);border-radius:12px;padding:10px 14px;margin-bottom:20px}
.hint-label{font-size:11px;color:var(--text-dim);flex:1}
.hint-val{font-family:'Vazirmatn',monospace;font-size:14px;font-weight:700;color:var(--accent);background:rgba(43,102,255,0.08);border:1px solid rgba(43,102,255,0.18);padding:4px 12px;border-radius:8px;cursor:pointer;transition:.15s;direction:ltr}
.hint-val:hover{background:rgba(43,102,255,0.15)}
.field{margin-bottom:18px}
.field label{display:block;font-size:11px;font-weight:600;color:var(--text-dim);margin-bottom:7px}
.inp-wrap{position:relative}
input[type=password]{width:100%;padding:14px 44px 14px 44px;border-radius:14px;border:1.5px solid var(--border);background:#fff;color:var(--text);font-family:inherit;font-size:14px;outline:none;transition:.2s;direction:ltr;text-align:left}
input[type=password]:focus{border-color:rgba(43,102,255,0.5);box-shadow:0 0 0 4px rgba(43,102,255,0.06)}
input[type=password]::placeholder{color:var(--text-dim)}
.ic{position:absolute;top:50%;transform:translateY(-50%);color:var(--text-dim);font-size:18px;pointer-events:none;transition:.2s}
.ic.ilic{right:14px}
.ic.iric{left:14px}
.eye-btn{position:absolute;left:14px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--text-dim);cursor:pointer;font-size:18px;padding:4px;display:flex;z-index:2;transition:.15s}
.eye-btn:hover{color:var(--accent-red)}
input:focus~.ic{color:var(--accent)}
.err{display:none;background:rgba(220,38,38,0.06);border:1px solid rgba(220,38,38,0.15);border-radius:12px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:#EF4444;align-items:center;gap:8px}
.err.show{display:flex}
.row-flex{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;font-size:12px}
.remember{display:flex;align-items:center;gap:6px;color:var(--text-dim);cursor:pointer}
.remember input{accent-color:var(--accent);width:15px;height:15px}
.forgot{color:var(--accent-red);text-decoration:none;font-weight:600;transition:.15s}
.forgot:hover{text-decoration:underline}
.btn{width:100%;padding:14px;border-radius:14px;border:none;cursor:pointer;background:linear-gradient(135deg,#2B66FF,#FF3B65);color:#fff;font-family:inherit;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 4px 24px rgba(43,102,255,0.3);transition:.25s;position:relative;overflow:hidden}
.btn::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(255,255,255,0.12),transparent);opacity:0;transition:.25s}
.btn:hover{box-shadow:0 6px 32px rgba(43,102,255,0.45);transform:translateY(-1px)}
.btn:hover::before{opacity:1}
.btn:active{transform:translateY(0) scale(.98)}
.btn:disabled{opacity:.5;cursor:not-allowed;transform:none}
.theme-switch{position:absolute;top:16px;left:16px;background:rgba(43,102,255,0.06);border:1px solid var(--border);color:var(--text-dim);width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:20;transition:.15s;font-size:16px}
.theme-switch:hover{background:rgba(43,102,255,0.12);color:var(--accent)}
.footer{margin-top:22px;padding-top:18px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11px;color:var(--text-dim)}
.footer a{color:var(--accent);font-weight:600;text-decoration:none;display:flex;align-items:center;gap:4px;transition:.15s}
.footer a:hover{color:var(--accent-red)}
@keyframes spin{to{transform:rotate(360deg)}}
@media(max-width:480px){.card{padding:32px 24px 28px;border-radius:16px}.brand-name{font-size:22px}}
</style>
</head>
<body>
<div class="bg-layer">
  <svg class="tl" viewBox="0 0 400 400" fill="none">
    <line x1="200" y1="0" x2="200" y2="400" stroke="#636E72" stroke-width="0.4"/>
    <line x1="0" y1="200" x2="400" y2="200" stroke="#636E72" stroke-width="0.4"/>
    <line x1="59" y1="0" x2="341" y2="400" stroke="#636E72" stroke-width="0.3"/>
    <line x1="341" y1="0" x2="59" y2="400" stroke="#636E72" stroke-width="0.3"/>
    <circle cx="200" cy="200" r="60" stroke="#636E72" stroke-width="0.4"/>
    <circle cx="200" cy="200" r="120" stroke="#636E72" stroke-width="0.3"/>
    <circle cx="200" cy="200" r="180" stroke="#636E72" stroke-width="0.2"/>
    <path d="M140 110L155 165L210 175L155 185L140 240L125 185L70 175L125 165Z" stroke="#636E72" stroke-width="0.5"/>
  </svg>
  <svg class="br" viewBox="0 0 400 400" fill="none">
    <line x1="200" y1="0" x2="200" y2="400" stroke="#636E72" stroke-width="0.4"/>
    <line x1="0" y1="200" x2="400" y2="200" stroke="#636E72" stroke-width="0.4"/>
    <line x1="59" y1="0" x2="341" y2="400" stroke="#636E72" stroke-width="0.3"/>
    <line x1="341" y1="0" x2="59" y2="400" stroke="#636E72" stroke-width="0.3"/>
    <circle cx="200" cy="200" r="80" stroke="#636E72" stroke-width="0.4"/>
    <circle cx="200" cy="200" r="150" stroke="#636E72" stroke-width="0.3"/>
    <path d="M140 110L155 165L210 175L155 185L140 240L125 185L70 175L125 165Z" stroke="#636E72" stroke-width="0.5"/>
  </svg>
</div>
<button class="theme-switch" id="theme-btn" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-moon" id="theme-icon"></i></button>
<div class="wrap">
  <div class="card">
    <div class="spider-logo">
      <svg class="spider-svg" viewBox="0 0 64 64" fill="none">
        <defs>
          <linearGradient id="spiderRed" x1="0" y1="0" x2="64" y2="64"><stop offset="0%" stop-color="#FF3B65"/><stop offset="35%" stop-color="#FF3B65"/><stop offset="65%" stop-color="#2B66FF"/><stop offset="100%" stop-color="#2B66FF"/></linearGradient>
          <filter id="gloss"><feGaussianBlur in="SourceAlpha" stdDeviation="1"/><feOffset dx="0" dy="0"/><feComponentTransfer><feFuncA type="linear" slope="0.3"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
        </defs>
        <circle cx="32" cy="32" r="30" stroke="url(#spiderRed)" stroke-width="2" fill="rgba(255,59,101,0.05)"/>
        <ellipse cx="32" cy="30" rx="14" ry="8" fill="url(#spiderRed)" opacity="0.15"/>
        <path d="M32 8L33 26L51 27L33 28L32 48L31 28L13 27L31 26Z" fill="url(#spiderRed)" opacity="0.95" filter="url(#gloss)"/>
        <circle cx="32" cy="27" r="5" fill="url(#spiderRed)"/>
        <path d="M20 16L26 24" stroke="url(#spiderRed)" stroke-width="2" stroke-linecap="round"/>
        <path d="M44 16L38 24" stroke="url(#spiderRed)" stroke-width="2" stroke-linecap="round"/>
        <path d="M20 38L26 30" stroke="url(#spiderRed)" stroke-width="2" stroke-linecap="round"/>
        <path d="M44 38L38 30" stroke="url(#spiderRed)" stroke-width="2" stroke-linecap="round"/>
        <path d="M32 4L32 8" stroke="url(#spiderRed)" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </div>
    <div class="brand-row"><div class="brand-name">SPIDER PANEL</div></div>
    <div class="separator"></div>
    <h1 class="welcome">ورود به حساب کاربری</h1>
    <p class="subtitle">برای دسترسی به پنل مدیریت رمز عبور خود را وارد کنید</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="hint-box">
      <span class="hint-label">رمز عبور پیش‌فرض</span>
      <span class="hint-val" onclick="document.getElementById('pw').value='123456';document.getElementById('pw').focus()">123456</span>
    </div>
    <form id="form">
      <div class="field">
        <label>رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="رمز عبور خود را وارد کنید" autofocus required>
          <i class="ti ti-lock ic ilic"></i>
          <button type="button" class="eye-btn" onclick="togglePw()"><i class="ti ti-eye" id="eye-icon"></i></button>
        </div>
      </div>
      <div class="row-flex">
        <label class="remember"><input type="checkbox"> مرا به خاطر بسپار</label>
        <a href="#" class="forgot">فراموشی رمز عبور</a>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود</button>
    </form>
    <div class="footer"><a href="https://t.me/CodeBoxo" target="_blank"><i class="ti ti-brand-telegram"></i>@CodeBoxo</a></div>
  </div>
</div>
<script>
function togglePw(){var i=document.getElementById('pw');var btn=document.getElementById('eye-icon');var toText=i.type==='password';i.type=toText?'text':'password';btn.className='ti '+(toText?'ti-eye-off':'ti-eye');}
var isDark=false;
function applyTheme(dark){document.documentElement.setAttribute('data-theme',dark?'dark':'light');var icon=document.getElementById('theme-icon');icon.className='ti '+(dark?'ti-sun':'ti-moon');}
function toggleTheme(){isDark=!isDark;localStorage.setItem('sp-theme',isDark?'dark':'light');applyTheme(isDark);}
applyTheme(isDark);
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  var btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  try{
    var r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){var d=await r.json().catch(function(){return{};});throw new Error(d.detail||'خطا');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود';
  }
});
</script>
</body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SPIDER PANEL · مدیریت</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0D1117;--bg2:#161B22;--bg3:#21262D;
  --card:rgba(22,27,34,0.8);--card-b:rgba(255,255,255,0.08);--card-bh:rgba(255,255,255,0.14);
  --accent:#2B66FF;--accent2:#6C5CE7;--accent-d:rgba(43,102,255,0.1);
  --green:#00B894;--green-bg:rgba(0,184,148,0.1);--green-t:#00B894;
  --red:#FF4757;--red-bg:rgba(255,71,87,0.1);--red-t:#FF4757;
  --amber:#FDCB6E;--amber-bg:rgba(253,203,110,0.1);--amber-t:#FDCB6E;
  --purple:#6C5CE7;--purple-bg:rgba(108,92,231,0.1);--purple-t:#A29BFE;
  --t1:#E6EDF3;--t2:#8B949E;--t3:#484F58;
  --sidebar-w:260px;--radius:20px;
  --shadow:0 4px 30px rgba(0,0,0,0.3);
  --gradient:linear-gradient(135deg,#2B66FF,#FF3B65);
  --font:'Vazirmatn',sans-serif;
}
[data-theme="light"]{
  --bg:#F8F9FA;--bg2:#F1F5F9;--bg3:#E2E8F0;
  --card:rgba(255,255,255,0.85);--card-b:rgba(0,0,0,0.08);--card-bh:rgba(43,102,255,0.2);
  --t1:#1E272E;--t2:#636E72;--t3:#B2BEC3;
  --green:#00B894;--green-bg:rgba(0,184,148,0.08);--green-t:#00856A;
  --red:#FF4757;--red-bg:rgba(255,71,87,0.08);--red-t:#D63031;
  --amber:#FDCB6E;--amber-bg:rgba(253,203,110,0.15);--amber-t:#B8860B;
  --purple-t:#5B21B6;
}
html,body{height:100%}
body{font-family:var(--font);background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:13px;transition:background .35s,color .35s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}

/* Sidebar - RTL: right side */
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--card);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);transition:transform .3s cubic-bezier(.4,0,.2,1),background .35s,border-color .35s}
.sidebar::before{content:'';position:absolute;inset:0;background:rgba(255,255,255,0.01);pointer-events:none}
.logo{padding:22px 20px 18px;border-bottom:1px solid var(--card-b);display:flex;align-items:center;gap:12px}
.logo-svg{width:40px;height:40px;flex-shrink:0}
.logo-text{min-width:0}
.logo-name{font-size:15px;font-weight:800;letter-spacing:-.01em;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.logo-sub{font-size:9px;color:var(--t3);font-weight:500;margin-top:1px}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:10px;font-size:16px;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.sb-close:hover{background:rgba(255,71,87,0.1);color:var(--red-t)}
.nav-wrap{flex:1;overflow-y:auto;padding:8px 0}
.nav-sec{padding:16px 20px 6px;font-size:9.5px;letter-spacing:.12em;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:10px;padding:11px 16px;margin:2px 10px;color:var(--t2);font-size:12.5px;font-weight:500;cursor:pointer;border-radius:14px;transition:all .18s;position:relative}
.nav-it i{font-size:17px;width:20px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t1)}
.nav-it.on{background:var(--accent-d);color:var(--t1);font-weight:600}
.nav-it.on::before{content:'';position:absolute;right:0;top:50%;transform:translateY(-50%);width:3px;height:24px;border-radius:3px 0 0 3px;background:var(--gradient)}
.nav-badge{margin-right:auto;background:var(--accent-d);color:var(--accent);font-size:10px;padding:2px 8px;border-radius:20px;font-weight:700}
.sb-foot{padding:14px 16px;border-top:1px solid var(--card-b);display:flex;flex-direction:column;gap:7px}
.sb-foot .user-chip{display:flex;align-items:center;gap:8px;padding:10px 12px;background:var(--accent-d);border-radius:14px;margin-bottom:4px}
.sb-foot .user-avatar{width:32px;height:32px;border-radius:10px;background:var(--gradient);display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px;flex-shrink:0}
.sb-foot .user-name{font-size:12px;font-weight:600;color:var(--t1)}
.sb-foot .user-role{font-size:9.5px;color:var(--t3)}
.tg-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#0098e6,#0077bb);color:#fff;border-radius:12px;padding:10px;font-size:12px;font-weight:600;font-family:inherit;border:none;cursor:pointer;width:100%;transition:.15s}
.tg-btn:hover{filter:brightness(1.1)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:12px;padding:9px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.15s}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:12px;padding:9px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(255,71,87,0.2);cursor:pointer;width:100%;transition:.15s}
.logout-btn:hover{background:rgba(255,71,87,0.2)}

/* Mobile */
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:54px;background:var(--card);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 16px;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.mob-top .ml{display:flex;align-items:center;gap:10px}
.mob-logo-svg{width:30px;height:30px}
.mob-title{font-size:14px;font-weight:800;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.mob-right{display:flex;gap:7px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:36px;height:36px;border-radius:12px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.menu-btn:hover,.theme-mob:hover{color:var(--accent)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}

/* Content */
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .3s;position:relative;z-index:1}
.pg{display:none;animation:pgIn .3s ease}
.pg.on{display:block}
@keyframes pgIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* Topbar */
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:24px;flex-wrap:wrap;gap:12px}
.tb-left{min-width:0}
.tb-title{font-size:20px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:10px;letter-spacing:-.02em}
.tb-title i{color:var(--accent);font-size:22px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}

/* Badges */
.badge{font-size:10px;padding:5px 12px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:var(--purple-t)}
.dot{width:7px;height:7px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}

/* Metrics */
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:20px 20px 18px;transition:all .25s;position:relative;overflow:hidden;cursor:default;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.metric::before{content:'';position:absolute;top:0;right:0;left:0;height:3px;background:var(--gradient);opacity:0;transition:.25s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:var(--shadow)}
.metric:hover::before{opacity:1}
.metric.suc::before{background:var(--green)}
.metric.dan::before{background:var(--red)}
.m-icon{width:38px;height:38px;border-radius:12px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:var(--accent);font-size:18px}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10.5px;color:var(--t3);margin-bottom:5px;font-weight:600}
.m-val{font-size:28px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:13px;font-weight:500;color:var(--t3)}
.m-sub{font-size:10.5px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:4px}

/* Quick Actions */
.quick-actions{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px}
.qa-btn{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:18px 14px;display:flex;flex-direction:column;align-items:center;gap:8px;cursor:pointer;transition:all .2s;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);font-family:inherit;color:var(--t2)}
.qa-btn:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow);color:var(--accent)}
.qa-btn i{font-size:22px;color:var(--accent)}
.qa-btn span{font-size:11px;font-weight:600;text-align:center}

/* Glass Card */
.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:20px 22px;transition:border-color .25s,background .35s,transform .25s;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.card:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.card-title{font-size:13px;font-weight:700;color:var(--t1);margin-bottom:16px;display:flex;align-items:center;gap:8px}
.card-title i{font-size:17px;color:var(--accent)}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:18px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:14px;margin-bottom:18px}
.mb16{margin-bottom:16px}

/* VLESS Box */
.vless-box{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px;margin-bottom:20px;position:relative;overflow:hidden;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.vless-box::before{content:'';position:absolute;top:-50px;left:-50px;width:180px;height:180px;background:radial-gradient(circle,rgba(43,102,255,0.08),transparent 70%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px;position:relative;z-index:1}
.vl-title{color:var(--t2);font-size:12px;display:flex;align-items:center;gap:7px;font-weight:700}
.vl-title i{color:var(--accent);font-size:16px}
.vl-code{background:rgba(0,0,0,0.15);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px;font-size:11px;font-family:'SF Mono','Fira Code',ui-monospace,monospace;color:var(--accent);word-break:break-all;line-height:1.8;position:relative;z-index:1;direction:ltr;text-align:left}
.vl-actions{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap;position:relative;z-index:1}

/* Buttons */
.btn{font-family:inherit;font-size:12px;font-weight:600;border-radius:14px;padding:9px 16px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border:none;transition:all .18s;white-space:nowrap}
.btn i{font-size:14px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{background:var(--gradient);color:#fff;box-shadow:0 3px 14px rgba(43,102,255,0.3)}
.btn-p:hover{box-shadow:0 5px 20px rgba(43,102,255,0.45);transform:translateY(-1px)}
.btn-o{background:transparent;border:1.5px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:var(--card-bh)}
.btn-g{background:var(--accent-d);color:var(--accent);border:1px solid rgba(43,102,255,0.12)}
.btn-g:hover{background:rgba(43,102,255,0.18)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(255,71,87,0.15)}
.btn-d:hover{background:rgba(255,71,87,0.2)}
.btn-pur{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(108,92,231,0.15)}
.btn-pur:hover{background:rgba(108,92,231,0.2)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(253,203,110,0.15)}
.btn-amber:hover{background:rgba(253,203,110,0.2)}
.btn-sm{padding:6px 10px;font-size:10.5px;border-radius:10px}
.btn-icon{width:32px;height:32px;padding:0;justify-content:center;border-radius:10px}

/* Server Info Panel */
.server-panel{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px 22px;margin-bottom:16px;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.server-panel:hover{border-color:var(--card-bh);box-shadow:var(--shadow)}
.server-row{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.server-row:last-child{margin-bottom:0}
.server-info-label{font-size:11px;font-weight:600;color:var(--t2);display:flex;align-items:center;gap:8px;min-width:70px}
.server-info-label i{font-size:15px;color:var(--accent)}
.server-info-val{font-size:11px;font-weight:700;color:var(--t1);width:50px;text-align:left}
.server-bar-wrap{flex:1;margin:0 12px}
.server-bar{height:8px;border-radius:4px;background:rgba(255,255,255,0.06);overflow:hidden}
.server-bar-f{height:100%;border-radius:4px;transition:width .6s ease}
.server-bar-f.cpu{background:linear-gradient(90deg,#2B66FF,#6C5CE7)}
.server-bar-f.ram{background:linear-gradient(90deg,#6C5CE7,#A29BFE)}
.server-bar-f.disk{background:linear-gradient(90deg,#2B66FF,#FF3B65)}
.server-bar-f.net{background:linear-gradient(90deg,#00B894,#2B66FF)}

/* Data Table */
.data-table{width:100%;border-collapse:separate;border-spacing:0;background:var(--card);border:1px solid var(--card-b);border-radius:16px;overflow:hidden;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.data-table th{background:rgba(255,255,255,0.03);font-size:10.5px;font-weight:700;color:var(--t3);padding:14px 16px;text-align:right;border-bottom:1px solid var(--card-b)}
.data-table td{padding:14px 16px;border-bottom:1px solid var(--card-b);font-size:12px;color:var(--t1)}
.data-table tr:last-child td{border-bottom:none}
.data-table tr:hover td{background:rgba(255,255,255,0.02)}
.pagination{display:flex;align-items:center;justify-content:center;gap:6px;margin-top:16px}
.pg-btn{width:34px;height:34px;border-radius:8px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;cursor:pointer;transition:.15s;font-family:inherit}
.pg-btn:hover{background:var(--accent-d);color:var(--accent)}
.pg-btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}

/* Status rows */
.sr{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.04);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:7px}
.sr-k i{font-size:14px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}

/* Charts */
.ch{position:relative;height:240px}
.ch-lg{position:relative;height:340px}
.ch-sm{position:relative;height:190px}

/* Chip badges */
.exp-chip{font-size:9.5px;padding:4px 10px;border-radius:8px;font-weight:700;display:inline-flex;align-items:center;gap:4px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent)}

/* Toggle */
.tog{width:38px;height:22px;border-radius:22px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:16px;height:16px;border-radius:50%;background:#fff;left:3px;top:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on{background:var(--green)}
.tog.on::after{left:19px}

/* Forms */
.form-row{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:4px}
.fg label{font-size:10.5px;color:var(--t3);font-weight:700}
.fi,.fs{padding:10px 13px;border-radius:12px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.15);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s;min-width:100px}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:rgba(43,102,255,0.45);box-shadow:0 0 0 3px rgba(43,102,255,0.08)}
.fs option{background:var(--bg2)}
.cl{background:var(--accent-d);border:1px solid rgba(43,102,255,0.12);border-radius:12px;padding:12px 14px;font-size:11.5px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.7;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(253,203,110,0.15);color:var(--amber-t)}
.cl.amber i{color:var(--amber)}

/* Create Panel */
.create-panel{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;margin-bottom:18px;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);position:relative}
.cp-head{display:flex;align-items:center;gap:14px;padding:24px 26px 20px;position:relative;z-index:1}
.cp-head-icon{width:48px;height:48px;border-radius:16px;background:var(--gradient);display:flex;align-items:center;justify-content:center;color:#fff;font-size:21px;flex-shrink:0;box-shadow:0 6px 18px rgba(43,102,255,0.3)}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:15px;font-weight:800;color:var(--t1)}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:3px}
.cp-body{padding:4px 26px 24px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:16px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,0.1);border:1px solid var(--card-b);border-radius:16px;padding:16px 18px}
.cp-block-label{font-size:10.5px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;margin-bottom:12px}
.cp-block-label i{color:var(--accent);font-size:15px}
.cp-input-full{width:100%;padding:11px 14px;border-radius:13px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.12);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
.cp-input-full:focus{border-color:rgba(43,102,255,0.5);box-shadow:0 0 0 3px rgba(43,102,255,0.1)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:10px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
.chip{font-size:10.5px;font-weight:700;padding:6px 13px;border-radius:10px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;white-space:nowrap}
.chip:hover{background:rgba(43,102,255,0.18);color:var(--accent)}
.chip.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 12px rgba(43,102,255,0.35)}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.proto-card{border:1.5px solid var(--card-b);border-radius:16px;padding:15px 13px;cursor:pointer;transition:.2s;text-align:center;position:relative;background:rgba(0,0,0,0.08)}
.proto-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(43,102,255,0.08)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-check{position:absolute;top:8px;left:8px;width:18px;height:18px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.22s}
.proto-card-icon{width:36px;height:36px;border-radius:12px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:17px;margin:0 auto 9px}
.proto-card.active .proto-card-icon{background:var(--accent);color:#fff}
.proto-card-title{font-size:11.5px;font-weight:800;color:var(--t1)}
.proto-card-desc{font-size:9.5px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:14px;padding-top:18px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:9px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:16px;flex-shrink:0}
.cp-submit-btn{background:var(--gradient);color:#fff;border:none;border-radius:16px;padding:14px 28px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 22px rgba(43,102,255,0.3);transition:.2s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(43,102,255,0.45)}
.cp-submit-btn:active{transform:translateY(0) scale(.98)}

/* Inbound Config Modal (X-UI inspired) */
.inbound-modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(8px);padding:20px}
.inbound-modal.open{display:flex}
.inbound-card{background:rgba(22,27,34,0.96);border:1px solid rgba(255,255,255,0.1);border-radius:24px;max-width:900px;width:100%;max-height:90vh;overflow:hidden;display:flex;position:relative;box-shadow:0 24px 80px rgba(0,0,0,0.5);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.inbound-banner{width:280px;flex-shrink:0;background:linear-gradient(180deg,rgba(22,27,34,1) 0%,rgba(10,15,25,1) 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px 24px;position:relative;overflow:hidden;border-left:1px solid rgba(255,255,255,0.06)}
.inbound-banner::before{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,0.03) 1px,transparent 1px);background-size:20px 20px}
.inbound-banner::after{content:'';position:absolute;top:-80px;right:-30px;width:200px;height:200px;background:radial-gradient(circle,rgba(43,102,255,0.15),transparent 70%)}
.inbound-spider{position:relative;z-index:1}
.inbound-spider svg{width:100px;height:100px;filter:drop-shadow(0 0 30px rgba(255,59,101,0.4)) drop-shadow(0 0 50px rgba(43,102,255,0.3))}
.inbound-banner-text{position:relative;z-index:1;margin-top:24px;text-align:center;font-size:15px;font-weight:700;color:rgba(255,255,255,0.8)}
.inbound-form{flex:1;overflow-y:auto;padding:28px 30px}
.inbound-section{margin-bottom:22px}
.inbound-section-title{font-size:11px;font-weight:800;color:var(--accent);margin-bottom:12px;display:flex;align-items:center;gap:7px}
.inbound-section-title i{font-size:14px}
.inbound-field{margin-bottom:12px}
.inbound-field label{display:block;font-size:10.5px;font-weight:700;color:var(--t3);margin-bottom:5px}
.inbound-field.flex-row{display:flex;gap:10px}
.inbound-field.flex-row>div{flex:1}
.inbound-input-wrap{position:relative}
.inbound-input-wrap>i{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none;z-index:1}
.inbound-input{width:100%;padding:10px 36px 10px 14px;border-radius:12px;border:1.5px solid rgba(255,255,255,0.08);background:rgba(0,0,0,0.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
.inbound-input::placeholder{color:var(--t3)}
.inbound-input:focus{border-color:rgba(43,102,255,0.5);box-shadow:0 0 0 3px rgba(43,102,255,0.08)}
select.inbound-input{appearance:none;cursor:pointer}
.inbound-select-wrap{position:relative}
.inbound-select-wrap .sel-arr{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:12px;pointer-events:none}
/* sub-fields for transport */
.transport-sub{background:rgba(0,0,0,0.15);border:1px solid rgba(255,255,255,0.05);border-radius:14px;padding:14px 16px;margin-top:10px}
.transport-sub.hidden{display:none}
/* security toggles */
.sec-toggles{display:flex;gap:8px;margin-bottom:14px}
.sec-tog{flex:1;padding:10px 14px;border-radius:12px;border:1.5px solid rgba(255,255,255,0.08);background:rgba(0,0,0,0.15);color:var(--t2);font-family:inherit;font-size:11px;font-weight:700;cursor:pointer;transition:.18s;text-align:center}
.sec-tog:hover{border-color:rgba(43,102,255,0.3);color:var(--t1)}
.sec-tog.active{background:var(--accent-d);border-color:var(--accent);color:var(--accent)}
.sec-tog.active.tls{background:rgba(108,92,231,0.15);border-color:var(--purple);color:var(--purple)}
.sec-tog.active.reality{background:rgba(255,59,101,0.12);border-color:#FF3B65;color:#FF3B65}
.sec-panel{background:rgba(0,0,0,0.12);border:1px solid rgba(255,255,255,0.05);border-radius:14px;padding:14px 16px;margin-top:10px}
.sec-panel.hidden{display:none}
/* footer */
.inbound-footer{display:flex;gap:10px;margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,0.06)}
.inbound-cancel{flex:1;padding:12px;border-radius:14px;border:1.5px solid rgba(255,255,255,0.1);background:transparent;color:var(--t2);font-family:inherit;font-size:13px;font-weight:700;cursor:pointer;transition:.15s}
.inbound-cancel:hover{background:rgba(255,255,255,0.04);color:var(--t1)}
.inbound-submit{flex:2;padding:12px;border-radius:14px;border:none;background:var(--gradient);color:#fff;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;transition:.2s;display:flex;align-items:center;justify-content:center;gap:6px;box-shadow:0 4px 16px rgba(43,102,255,0.25)}
.inbound-submit:hover{transform:translateY(-1px);box-shadow:0 6px 24px rgba(43,102,255,0.4)}
@media(max-width:760px){.inbound-card{flex-direction:column;max-height:95vh}.inbound-banner{width:100%;flex-direction:row;padding:20px 24px;gap:16px}.inbound-banner svg{width:56px;height:56px}.inbound-banner-text{font-size:13px;margin-top:0}}

/* Password panel */
.pw-panel{background:var(--card);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;position:relative;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.pw-hero{display:flex;align-items:center;gap:16px;padding:24px 26px 20px;position:relative;z-index:1}
.pw-hero-icon{width:52px;height:52px;border-radius:16px;background:linear-gradient(135deg,#6C5CE7,#FF3B65);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(108,92,231,0.35)}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:15px;font-weight:800;color:var(--t1)}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:4px 26px 24px;position:relative;z-index:1}
.pw-field{position:relative;margin-bottom:14px}
.pw-field label{display:block;font-size:10.5px;font-weight:700;color:var(--t2);margin-bottom:7px}
.pw-input{width:100%;padding:12px 44px 12px 15px;border-radius:14px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.1);color:var(--t1);font-family:inherit;font-size:13px;outline:none;transition:.18s}
.pw-input:focus{border-color:rgba(108,92,231,0.5);box-shadow:0 0 0 3px rgba(108,92,231,0.1)}
.pw-eye{position:absolute;left:13px;top:36px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.pw-eye:hover{color:var(--purple)}
.pw-strength{height:5px;border-radius:3px;background:var(--accent-d);margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:rgba(100,116,139,0.2);transition:.25s}
.pw-strength-label{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:7px;margin-top:12px;margin-bottom:18px}
.pw-req{font-size:9.5px;padding:4px 10px;border-radius:8px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.18s}
.pw-req.met{background:var(--green-bg);color:var(--green-t)}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,#6C5CE7,#FF3B65);color:#fff;border:none;border-radius:16px;padding:13px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(108,92,231,0.3);transition:.2s}
.pw-submit:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(108,92,231,0.45)}
.pw-submit:active{transform:translateY(0) scale(.98)}

/* Sub groups */
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:18px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:12px 16px 12px 42px;border-radius:15px;border:1.5px solid var(--card-b);background:var(--card);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s;backdrop-filter:blur(12px)}
.subs-search input:focus{border-color:rgba(108,92,231,0.5);box-shadow:0 0 0 3px rgba(108,92,231,0.08)}
.subs-search i{position:absolute;left:15px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:16px}
.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:18px;margin-bottom:20px}
.sub-card{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;transition:all .3s cubic-bezier(.4,0,.2,1);position:relative;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.sub-card:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:0 16px 40px rgba(0,0,0,0.2)}
.sub-card-top{background:linear-gradient(155deg,rgba(108,92,231,0.06) 0%,transparent 65%);padding:22px 22px 18px;position:relative}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:14px;position:relative;z-index:1}
.sub-card-icon{width:50px;height:50px;border-radius:16px;background:linear-gradient(135deg,#6C5CE7,#FF3B65);display:flex;align-items:center;justify-content:center;color:#fff;font-size:21px;flex-shrink:0;box-shadow:0 6px 18px rgba(108,92,231,0.3)}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:15px;font-weight:800;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:28px;height:28px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:13px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}
.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative;z-index:1;margin-top:18px;background:rgba(0,0,0,0.08);border:1px solid var(--card-b);border-radius:16px;overflow:hidden}
.sub-card-stat{padding:12px 8px;text-align:center;border-left:1px solid var(--card-b)}
.sub-card-stat:last-child{border-left:none}
.sub-card-stat-val{font-size:16px;font-weight:800;color:var(--t1);line-height:1.2}
.sub-card-stat-label{font-size:9px;color:var(--t3);font-weight:700;margin-top:4px}
.sub-card-url-row{margin:16px 22px 0;background:rgba(108,92,231,0.06);border:1px dashed rgba(108,92,231,0.2);border-radius:14px;padding:10px 13px;display:flex;align-items:center;gap:8px;direction:ltr}
.sub-card-url-text{font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:10px;color:var(--purple);flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-align:left}
.sub-card-url-copy{background:none;border:none;color:var(--purple);cursor:pointer;font-size:13px;padding:3px;display:flex;flex-shrink:0;transition:.15s}
.sub-card-url-copy:hover{color:var(--purple-t);transform:scale(1.1)}
.sub-card-bottom{padding:16px 22px 20px;display:flex;gap:8px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}
.subs-empty-v2{text-align:center;padding:80px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:22px;grid-column:1/-1}
.subs-empty-v2-icon{width:70px;height:70px;border-radius:20px;background:var(--purple-bg);display:flex;align-items:center;justify-content:center;font-size:30px;color:var(--purple);margin:0 auto 18px}
.subs-empty-v2-title{font-size:14px;font-weight:700;color:var(--t2);margin-bottom:6px}
.subs-empty-v2-sub{font-size:11px;color:var(--t3)}

/* Config cards */
.cfg-grid{display:flex;flex-direction:column;gap:11px}
.spbar{height:5px;border-radius:3px;background:rgba(255,255,255,0.06);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:var(--gradient);transition:width 1s}
.cfg-card{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:0;transition:all .25s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 6px 28px rgba(0,0,0,0.15)}
.cfg-card.is-off{opacity:.55}
.cfg-card.is-exp{opacity:.75}
.cfg-row{display:flex;align-items:center;gap:18px;padding:16px 20px}
.cfg-status-dot{width:10px;height:10px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 4px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 4px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 4px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:130px;flex-shrink:0}
.cfg-label{font-size:13px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:8px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:9.5px;color:var(--accent);background:var(--accent-d);padding:3px 8px;border-radius:6px;cursor:pointer;transition:.15s;direction:ltr}
.cfg-uuid-mini:hover{background:rgba(43,102,255,0.2)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:6px;border-radius:4px;background:rgba(255,255,255,0.06);overflow:hidden}
.ubar-f{height:100%;border-radius:4px;transition:width .4s ease}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.proto-chip{font-size:9.5px;padding:4px 9px;border-radius:8px;font-weight:700;white-space:nowrap}
.pc-ws{background:var(--accent-d);color:var(--accent)}
.pc-xhttp{background:var(--purple-bg);color:var(--purple-t)}
.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:var(--purple);font-size:11px}

@media(max-width:880px){.cfg-row{flex-wrap:wrap}.cfg-divider-v{display:none}.cfg-usage-col{min-width:100%;order:5}}
@media(max-width:768px){.cfg-grid{display:grid;grid-template-columns:1fr;gap:14px}.cfg-card{border-radius:18px}.cfg-row{flex-direction:column;align-items:stretch;gap:14px;padding:18px}.cfg-identity{min-width:0;flex:1}.cfg-usage-col{min-width:0}.cfg-exp-col{min-width:0}.cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}.cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;margin-top:2px;width:100%}}

/* Connections */
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.conn-hero-tile{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:18px 20px;position:relative;overflow:hidden;transition:.25s;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.conn-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;right:0;left:0;height:3px;background:var(--gradient)}
.conn-hero-icon{width:36px;height:36px;border-radius:12px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:16px;margin-bottom:12px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-d);color:var(--accent)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{font-size:10px;color:var(--t3);font-weight:700;margin-bottom:4px}
.conn-hero-val{font-size:24px;font-weight:800;color:var(--t1);line-height:1}
.conn-hero-unit{font-size:11px;color:var(--t3);font-weight:500}
.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:16px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px}
.conn-toolbar-title i{color:var(--green);font-size:16px}
.conn-live-badge{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--green-t);background:var(--green-bg);padding:6px 13px;border-radius:20px;border:1px solid rgba(0,184,148,0.15)}
.conn-live-dot{width:7px;height:7px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite}
.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}
.conn-card-v2{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;transition:all .3s cubic-bezier(.4,0,.2,1);position:relative;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.conn-card-v2:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 36px rgba(0,0,0,0.2)}
.conn-card-v2-glow{position:absolute;top:-40px;left:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(0,184,148,0.08),transparent 70%);pointer-events:none}
.conn-card-v2-top{display:flex;align-items:center;gap:14px;padding:18px 20px 15px;position:relative;z-index:1}
.conn-avatar{width:46px;height:46px;border-radius:16px;background:linear-gradient(135deg,#00B894,#0D9668);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;position:relative;box-shadow:0 4px 16px rgba(0,184,148,0.25)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:19px;border:1.5px solid var(--green);opacity:.4;animation:breathe2 2.4s ease-in-out infinite}
@keyframes breathe2{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.12);opacity:0}}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px;direction:ltr}
.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex;transition:.15s}
.conn-ip-copy:hover{color:var(--accent)}
.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:9.5px;font-weight:800;padding:5px 10px;border-radius:20px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;gap:5px;white-space:nowrap;flex-shrink:0}
.conn-card-v2-divider{height:1px;background:linear-gradient(90deg,transparent,var(--card-b) 15%,var(--card-b) 85%,transparent);margin:0 20px}
.conn-card-v2-body{padding:15px 20px 18px}
.conn-proto-row{margin-bottom:14px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin-bottom:14px}
.conn-stat-box{display:flex;align-items:center;gap:9px}
.conn-stat-icon{width:28px;height:28px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0}
.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-text-label{font-size:9px;color:var(--t3);font-weight:700}
.conn-stat-text-val{font-size:12px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-duration-track{height:6px;border-radius:4px;background:rgba(255,255,255,0.06);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,#00B894,#3FD79C);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);width:40%;animation:shimmer 1.8s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}
.conn-empty-v2{text-align:center;padding:80px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:22px}
.conn-empty-v2-icon{width:70px;height:70px;border-radius:20px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:30px;color:var(--t3);margin:0 auto 18px}
.conn-empty-v2-title{font-size:14px;font-weight:700;color:var(--t2);margin-bottom:6px}
.conn-empty-v2-sub{font-size:11px;color:var(--t3)}

/* Logs */
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:13px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.04);position:relative}
.log-item:last-child{border-bottom:none}
.log-ic{width:32px;height:32px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.log-ic.err{background:var(--red-bg);color:var(--red-t)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-ic.info{background:var(--accent-d);color:var(--accent)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:9px;padding:2px 8px;border-radius:10px;background:var(--accent-d);color:var(--accent);font-weight:700}
.erow{padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.04)}
.erow:last-child{border-bottom:none}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px;display:flex;align-items:center;gap:5px}
.emsg{color:var(--red-t);font-family:'SF Mono','Fira Code',ui-monospace,monospace;background:var(--red-bg);padding:7px 10px;border-radius:8px;word-break:break-all;font-size:10.5px;direction:ltr;text-align:left}

/* Empty state */
.empty{text-align:center;padding:60px 20px;color:var(--t3)}
.empty i{font-size:42px;opacity:.3;margin-bottom:14px;display:block}
.empty p{font-size:13px;margin-top:4px}

/* Modal v2 */
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(6px)}
.modal-bg.open{display:flex}
.modal-v2{background:var(--card);border:1px solid var(--card-b);border-radius:24px;padding:0;max-width:460px;width:calc(100% - 32px);max-height:92vh;overflow-y:auto;position:relative;animation:modalIn .25s ease;box-shadow:0 24px 70px rgba(0,0,0,0.3);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px)}
@keyframes modalIn{from{opacity:0;transform:translateY(10px) scale(.97)}to{opacity:1;transform:none}}
.modal-v2-head{background:linear-gradient(155deg,rgba(108,92,231,0.08) 0%,transparent 65%);padding:20px 24px 16px;position:relative;overflow:hidden}
.modal-v2-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:32px;height:32px;border-radius:11px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:.15s}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(255,71,87,0.25)}
.modal-v2-icon{width:46px;height:46px;border-radius:16px;background:linear-gradient(135deg,#6C5CE7,#FF3B65);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;margin-bottom:12px;position:relative;z-index:1;box-shadow:0 8px 20px rgba(108,92,231,0.35)}
.modal-v2-title{font-size:16px;font-weight:800;color:var(--t1);position:relative;z-index:1}
.modal-v2-sub{font-size:11px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:18px 24px 22px;border-top:1px solid var(--card-b)}
.modal-v2-field{margin-bottom:12px}
.modal-v2-field label{display:flex;align-items:center;gap:6px;font-size:10px;font-weight:800;color:var(--t2);margin-bottom:6px}
.modal-v2-field label i{color:var(--purple);font-size:14px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none;transition:.15s;z-index:1}
.modal-v2-input{width:100%;padding:10px 40px 10px 14px;border-radius:14px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.1);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-input:focus{border-color:rgba(108,92,231,0.55);box-shadow:0 0 0 3px rgba(108,92,231,0.12)}
.modal-v2-input:focus~i{color:var(--purple)}
.modal-v2-hint{background:rgba(43,102,255,0.06);border:1px solid rgba(43,102,255,0.12);border-radius:13px;padding:10px 13px;font-size:10.5px;color:var(--t2);display:flex;gap:7px;align-items:flex-start;line-height:1.6;margin-top:3px}
.modal-v2-hint i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:9px;margin-top:16px}
.modal-v2-btn-cancel{flex:.75;justify-content:center;padding:11px;border-radius:14px;background:transparent;border:1.5px solid var(--card-b);color:var(--t2);font-family:inherit;font-size:12.5px;font-weight:700;cursor:pointer;transition:.15s;display:flex;align-items:center}
.modal-v2-btn-cancel:hover{background:var(--accent-d);color:var(--t1)}
.modal-v2-btn-submit{flex:1;justify-content:center;padding:11px;border-radius:14px;background:linear-gradient(135deg,#6C5CE7,#FF3B65);color:#fff;border:none;font-family:inherit;font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;box-shadow:0 6px 20px rgba(108,92,231,0.35);transition:.2s}
.modal-v2-btn-submit:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(108,92,231,0.5)}
.modal-v2-btn-submit:active{transform:translateY(0) scale(.98)}

/* Links modal */
.lmodal-head{background:linear-gradient(155deg,rgba(43,102,255,0.08) 0%,transparent 70%);padding:24px 26px 20px;position:relative;border-bottom:1px solid var(--card-b)}
.lmodal-icon-row{display:flex;align-items:center;gap:14px;position:relative;z-index:1}
.lmodal-icon{width:48px;height:48px;border-radius:16px;background:var(--gradient);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 18px rgba(43,102,255,0.3)}
.lmodal-title-v2{font-size:15px;font-weight:800;color:var(--t1)}
.lmodal-sub-v2{font-size:10.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:16px;position:relative}
.lmodal-search input{width:100%;padding:11px 14px 11px 40px;border-radius:14px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.1);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.18s}
.lmodal-search input:focus{border-color:rgba(43,102,255,0.5);box-shadow:0 0 0 3px rgba(43,102,255,0.08)}
.lmodal-search i{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:12px;position:relative;z-index:1}
.lmodal-qbtn{font-size:10.5px;font-weight:700;padding:6px 12px;border-radius:10px;background:var(--accent-d);color:var(--accent);border:1px solid var(--card-b);cursor:pointer;transition:.15s;font-family:inherit}
.lmodal-qbtn:hover{background:rgba(43,102,255,0.2)}
.lmodal-count{margin-right:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}
.lmodal-list{padding:12px 16px;max-height:380px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:16px;cursor:pointer;transition:.15s;margin-bottom:4px;border:1px solid transparent}
.lrow-v2:hover{background:var(--accent-d)}
.lrow-v2.checked{background:rgba(43,102,255,0.08);border-color:rgba(43,102,255,0.2)}
.lrow-v2-check{width:22px;height:22px;border-radius:8px;border:2px solid var(--card-b);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s;background:rgba(0,0,0,0.15)}
.lrow-v2.checked .lrow-v2-check{background:var(--accent);border-color:var(--accent)}
.lrow-v2-check i{font-size:13px;color:#fff;opacity:0;transform:scale(.5);transition:.15s}
.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}
.lrow-v2-avatar{width:36px;height:36px;border-radius:12px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.lrow-v2.checked .lrow-v2-avatar{background:var(--accent);color:#fff}
.lrow-v2-info{flex:1;min-width:0}
.lrow-v2-name{font-size:13px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-v2-meta{font-size:10px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.lrow-v2-status{font-size:9.5px;font-weight:800;padding:4px 10px;border-radius:20px;flex-shrink:0;white-space:nowrap}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}
.lrow-v2-status.off{background:var(--red-bg);color:var(--red-t)}
.lmodal-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:18px 26px;border-top:1px solid var(--card-b)}
.lmodal-footer-info{font-size:10.5px;color:var(--t3);display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--accent)}
.lmodal-footer-btns{display:flex;gap:8px}

/* Modal (legacy) */
.modal{background:var(--card);border:1px solid var(--card-b);border-radius:24px;padding:30px 28px;max-width:540px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:modalIn .25s ease;backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px)}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:32px;height:32px;border-radius:10px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none}
.modal-close:hover{background:var(--red-bg);color:var(--red-t)}
.modal-title{font-size:17px;font-weight:700;color:var(--t1);margin-bottom:20px;display:flex;align-items:center;gap:9px}
.modal-title i{color:var(--accent)}
.lrow{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid rgba(255,255,255,0.04)}
.lrow:last-child{border-bottom:none}
.lrow-check{width:16px;height:16px;border-radius:4px;cursor:pointer;accent-color:var(--accent)}
.lrow-label{flex:1;font-size:12px;color:var(--t1)}
.lrow-badge{font-size:9px;padding:2px 7px;border-radius:5px;background:var(--green-bg);color:var(--green-t);font-weight:700}

/* Toast */
.toast{position:fixed;bottom:24px;right:50%;transform:translateX(50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:14px;padding:12px 22px;font-size:12.5px;font-weight:600;opacity:0;transition:all .3s cubic-bezier(.4,0,.2,1);z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:0 8px 30px rgba(0,0,0,0.2);white-space:nowrap;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.toast.show{opacity:1;transform:translateX(50%) translateY(0)}
.toast.ok{border-color:rgba(0,184,148,0.3);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(255,71,87,0.3);background:var(--red-bg);color:var(--red-t)}

/* Dashboard footer */
.dash-footer{border-top:1px solid var(--card-b);margin-top:16px;padding-top:16px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10.5px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent);display:flex;align-items:center;gap:6px;font-weight:600}
.df-link:hover{color:var(--accent2)}

/* Traffic page */
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:14px;margin-bottom:20px}
.traf-main-stat{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px 26px;position:relative;overflow:hidden;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.traf-main-label{font-size:11px;color:var(--t3);font-weight:700;display:flex;align-items:center;gap:7px;margin-bottom:12px;position:relative;z-index:1}
.traf-main-val{font-size:36px;font-weight:800;color:var(--t1);line-height:1;display:flex;align-items:baseline;gap:6px;position:relative;z-index:1}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 11px;border-radius:20px;margin-top:14px;position:relative;z-index:1}
.traf-trend.up{background:var(--green-bg);color:var(--green-t)}
.traf-trend.down{background:var(--red-bg);color:var(--red-t)}
.traf-mini{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:20px;display:flex;flex-direction:column;justify-content:space-between;transition:.25s;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.traf-mini:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px}
.traf-mini-icon{width:34px;height:34px;border-radius:12px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}
.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-label{font-size:10px;color:var(--t3);font-weight:700}
.traf-mini-val{font-size:22px;font-weight:800;color:var(--t1)}
.traf-mini-sub{font-size:10px;color:var(--t3);margin-top:4px}
.traf-chart-card{background:var(--card);border:1px solid var(--card-b);border-radius:24px;padding:24px 26px 20px;margin-bottom:18px;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:19px}
.traf-chart-sub{font-size:11px;color:var(--t3);margin-top:4px}
.traf-legend{display:flex;gap:16px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:11px;color:var(--t2);font-weight:600}
.traf-legend-dot{width:9px;height:9px;border-radius:3px}
.traf-range-tabs{display:flex;gap:4px;background:var(--accent-d);padding:3px;border-radius:12px;border:1px solid var(--card-b)}
.traf-range-tab{padding:7px 14px;border-radius:10px;font-size:11px;font-weight:700;color:var(--t3);cursor:pointer;transition:.15s;border:none;background:transparent;font-family:inherit}
.traf-range-tab.on{background:var(--accent);color:#fff;box-shadow:0 2px 8px rgba(43,102,255,0.3)}
.traf-chart-body{height:340px;margin-top:16px;position:relative}

/* Subscriptions */
.sub-box{background:rgba(108,92,231,0.06);border:1px solid rgba(108,92,231,0.18);border-radius:14px;padding:16px 18px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:12px}
.sub-url{font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:11px;color:var(--purple);word-break:break-all;flex:1;direction:ltr;text-align:left}

/* Server panel v2 */
.srv-panel{background:var(--card);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;position:relative;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.srv-hero{display:flex;align-items:center;gap:16px;padding:24px 26px;position:relative;z-index:1;border-bottom:1px solid var(--card-b)}
.srv-hero-icon{width:52px;height:52px;border-radius:16px;background:var(--gradient);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(43,102,255,0.3)}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:15px;font-weight:800;color:var(--t1);word-break:break-all;direction:ltr;text-align:left}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:22px 24px;position:relative;z-index:1}
.srv-tile{display:flex;align-items:center;gap:12px;background:rgba(0,0,0,0.08);border:1px solid var(--card-b);border-radius:16px;padding:14px 16px;transition:.18s}
.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.srv-tile-icon{width:38px;height:38px;border-radius:12px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;margin-bottom:3px}
.srv-tile-val{font-size:12.5px;font-weight:700;color:var(--t1);word-break:break-word}

@media(max-width:900px){.traf-hero{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.traf-hero{grid-template-columns:1fr}.traf-chart-body{height:280px}.quick-actions{grid-template-columns:1fr 1fr}}
@media(max-width:760px){.conn-hero{grid-template-columns:1fr 1fr}.inbound-card{flex-direction:column}.inbound-banner{width:100%;flex-direction:row;padding:20px 24px;gap:16px}.inbound-banner svg{width:56px;height:56px}}
@media(max-width:560px){.srv-tiles{grid-template-columns:1fr}}
@media(max-width:500px){.sub-grid{grid-template-columns:1fr}.sub-card-stats{grid-template-columns:repeat(3,1fr)}.conn-grid-v2{grid-template-columns:1fr}}
@media(max-width:1050px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.4)}
  .sb-close{display:flex}
  .main{margin-right:0;padding-top:72px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
  .cp-row{grid-template-columns:1fr}
  .proto-cards{grid-template-columns:1fr}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:64px 14px 50px}
  .sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}
}
</style>
</head>
<body>
<div class="toast" id="toast"></div>

<!-- Inbound Config Modal (X-UI inspired) -->
<div class="inbound-modal" id="inbound-modal">
  <div class="inbound-card">
    <div class="inbound-banner">
      <div class="inbound-spider">
        <svg viewBox="0 0 100 100" fill="none">
          <defs>
            <radialGradient id="ibGlow" cx="50%" cy="50%"><stop offset="0%" stop-color="#FF3B65" stop-opacity="0.3"/><stop offset="100%" stop-color="transparent"/></radialGradient>
            <linearGradient id="ibGrad" x1="0" y1="0" x2="100" y2="100"><stop offset="0%" stop-color="#2B66FF"/><stop offset="100%" stop-color="#FF3B65"/></linearGradient>
          </defs>
          <circle cx="50" cy="50" r="48" fill="rgba(22,27,34,0.5)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
          <circle cx="50" cy="50" r="35" fill="url(#ibGlow)"/>
          <path d="M50 10L52 40L82 42L52 44L50 80L48 44L18 42L48 40Z" fill="url(#ibGrad)" opacity="0.95"/>
          <circle cx="50" cy="42" r="6" fill="url(#ibGrad)"/>
          <path d="M30 24L36 34" stroke="url(#ibGrad)" stroke-width="2"/>
          <path d="M70 24L64 34" stroke="url(#ibGrad)" stroke-width="2"/>
          <path d="M30 60L36 50" stroke="url(#ibGrad)" stroke-width="2"/>
          <path d="M70 60L64 50" stroke="url(#ibGrad)" stroke-width="2"/>
        </svg>
      </div>
      <div class="inbound-banner-text">اتصال امن و سریع</div>
    </div>
    <div class="inbound-form">
      <button class="modal-v2-close" onclick="closeInboundModal()"><i class="ti ti-x"></i></button>

      <!-- Core Settings -->
      <div class="inbound-section">
        <div class="inbound-section-title"><i class="ti ti-settings"></i> تنظیمات اصلی</div>

        <div class="inbound-field">
          <label>پروتکل</label>
          <div class="inbound-select-wrap">
            <select class="inbound-input" id="ib-protocol" onchange="onProtocolChange()">
              <option value="vless">VLESS</option>
              <option value="vmess">VMESS</option>
              <option value="trojan">Trojan</option>
              <option value="shadowsocks">Shadowsocks</option>
            </select>
            <i class="ti ti-chevron-down sel-arr"></i>
          </div>
        </div>

        <div class="inbound-field">
          <label>پورت</label>
          <div class="inbound-input-wrap">
            <i class="ti ti-hash"></i>
            <input class="inbound-input" id="ib-port" type="number" placeholder="مثال: 443">
          </div>
        </div>

        <div class="inbound-field flex-row">
          <div>
            <label>حجم کل (گیگابایت)</label>
            <div class="inbound-select-wrap">
              <select class="inbound-input" id="ib-traffic">
                <option value="0">نامحدود</option>
                <option value="5">۵ گیگابایت</option>
                <option value="10">۱۰ گیگابایت</option>
                <option value="20">۲۰ گیگابایت</option>
                <option value="50">۵۰ گیگابایت</option>
                <option value="100">۱۰۰ گیگابایت</option>
                <option value="500">۵۰۰ گیگابایت</option>
              </select>
              <i class="ti ti-chevron-down sel-arr"></i>
            </div>
          </div>
          <div>
            <label>تاریخ انقضا</label>
            <div class="inbound-input-wrap">
              <i class="ti ti-calendar"></i>
              <input class="inbound-input" id="ib-expire" type="date">
            </div>
          </div>
        </div>

        <div class="inbound-field">
          <label>محدودیت IP کلاینت</label>
          <div class="inbound-input-wrap">
            <i class="ti ti-users"></i>
            <input class="inbound-input" id="ib-iplimit" type="number" placeholder="۰ = نامحدود" value="0">
          </div>
        </div>
      </div>

      <!-- Transport -->
      <div class="inbound-section">
        <div class="inbound-section-title"><i class="ti ti-network"></i> ترنسمیشن</div>

        <div class="inbound-field">
          <label>نوع شبکه</label>
          <div class="inbound-select-wrap">
            <select class="inbound-input" id="ib-network" onchange="onNetworkChange()">
              <option value="tcp">TCP</option>
              <option value="http">HTTP</option>
              <option value="ws">WebSocket (WS)</option>
              <option value="grpc">gRPC</option>
              <option value="quic">QUIC</option>
              <option value="xhttp">XHTTP</option>
            </select>
            <i class="ti ti-chevron-down sel-arr"></i>
          </div>
        </div>

        <!-- WS sub-fields -->
        <div class="transport-sub" id="ts-ws">
          <div class="inbound-field"><label>مسیر (Path)</label><input class="inbound-input" id="ib-ws-path" placeholder="/"></div>
          <div class="inbound-field"><label>Host Header</label><input class="inbound-input" id="ib-ws-host" placeholder=""></div>
        </div>

        <!-- gRPC sub-fields -->
        <div class="transport-sub hidden" id="ts-grpc">
          <div class="inbound-field"><label>نام سرویس</label><input class="inbound-input" id="ib-grpc-service" placeholder="GunService"></div>
        </div>

        <!-- XHTTP sub-fields -->
        <div class="transport-sub hidden" id="ts-xhttp">
          <div class="inbound-field"><label>حالت (Mode)</label>
            <div class="inbound-select-wrap">
              <select class="inbound-input" id="ib-xhttp-mode">
                <option value="packet-up">packet-up</option>
                <option value="stream-up">stream-up</option>
                <option value="stream-one">stream-one</option>
              </select>
              <i class="ti ti-chevron-down sel-arr"></i>
            </div>
          </div>
          <div class="inbound-field"><label>مسیر (Path)</label><input class="inbound-input" id="ib-xhttp-path" placeholder="/"></div>
        </div>

        <!-- TCP sub-fields -->
        <div class="transport-sub hidden" id="ts-tcp">
          <div class="inbound-field"><label>نوع Header</label><input class="inbound-input" id="ib-tcp-header" placeholder="none"></div>
          <div class="inbound-field"><label>مسیر (Path)</label><input class="inbound-input" id="ib-tcp-path" placeholder="/"></div>
        </div>
      </div>

      <!-- Security -->
      <div class="inbound-section">
        <div class="inbound-section-title"><i class="ti ti-shield-lock"></i> امنیت</div>

        <div class="sec-toggles">
          <button class="sec-tog active" onclick="setSecurity('none',this)">بدون رمزنگاری</button>
          <button class="sec-tog tls" onclick="setSecurity('tls',this)">TLS</button>
          <button class="sec-tog reality" onclick="setSecurity('reality',this)">REALITY</button>
        </div>

        <!-- TLS Panel -->
        <div class="sec-panel hidden" id="sec-tls">
          <div class="inbound-field"><label>دامنه</label><input class="inbound-input" id="ib-tls-domain" placeholder="example.com"></div>
          <div class="inbound-field"><label>مسیر Cert عمومی</label><input class="inbound-input" id="ib-tls-cert" placeholder="/etc/cert.pem"></div>
          <div class="inbound-field"><label>کلید خصوصی</label><input class="inbound-input" id="ib-tls-key" placeholder="/etc/key.pem"></div>
          <div class="inbound-field"><label>ALPN</label><input class="inbound-input" id="ib-tls-alpn" placeholder="h2,http/1.1"></div>
        </div>

        <!-- REALITY Panel -->
        <div class="sec-panel hidden" id="sec-reality">
          <div class="inbound-field"><label>مقصد (Dest)</label><div class="inbound-input-wrap"><i class="ti ti-target"></i><input class="inbound-input" id="ib-real-dest" placeholder="yahoo.com:443"></div></div>
          <div class="inbound-field"><label>Server Names (SNI)</label><input class="inbound-input" id="ib-real-sni" placeholder="yahoo.com,www.yahoo.com"></div>
          <div class="inbound-field"><label>کلید خصوصی</label><input class="inbound-input" id="ib-real-privkey" placeholder=""></div>
          <div class="inbound-field"><label>کلید عمومی</label><input class="inbound-input" id="ib-real-pubkey" placeholder=""></div>
          <div class="inbound-field"><label>Short IDs (hex)</label><input class="inbound-input" id="ib-real-shortids" placeholder="6ba85179e30d4fc2"></div>
          <div class="inbound-field"><label>Flow</label><div class="inbound-select-wrap"><select class="inbound-input" id="ib-real-flow"><option value="xtls-rprx-vision">xtls-rprx-vision</option></select><i class="ti ti-chevron-down sel-arr"></i></div></div>
        </div>
      </div>

      <!-- Footer -->
      <div class="inbound-footer">
        <button class="inbound-cancel" onclick="closeInboundModal()">انصراف</button>
        <button class="inbound-submit" onclick="submitInbound()"><i class="ti ti-link-plus"></i> ایجاد کانفیگ</button>
      </div>
    </div>
  </div>
</div>

<!-- Links Modal -->
<div class="modal-bg" id="modal-links">
  <div class="modal-v2" style="max-width:520px">
    <div class="lmodal-head">
      <button class="modal-v2-close" onclick="closeModal('modal-links')"><i class="ti ti-x"></i></button>
      <div class="lmodal-icon-row">
        <div class="lmodal-icon"><i class="ti ti-link-plus"></i></div>
        <div>
          <div class="lmodal-title-v2">مدیریت کانفیگ‌های <span id="modal-sub-name" style="color:var(--accent)">—</span></div>
          <div class="lmodal-sub-v2">انتخاب کانفیگ‌های این گروه</div>
        </div>
      </div>
      <div class="lmodal-search">
        <i class="ti ti-search"></i>
        <input type="text" id="lmodal-search-inp" placeholder="جستجوی کانفیگ..." oninput="filterLmodal(this.value)">
      </div>
      <div class="lmodal-quickbar">
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> انتخاب همه</button>
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> حذف انتخاب</button>
        <span class="lmodal-count" id="lmodal-count">۰ انتخاب شده</span>
      </div>
    </div>
    <div class="lmodal-list" id="modal-links-body">در حال بارگذاری...</div>
    <div class="lmodal-footer">
      <div class="lmodal-footer-info"><i class="ti ti-info-circle"></i> تغییرات بلافاصله اعمال می‌شود</div>
      <div class="lmodal-footer-btns">
        <button class="btn btn-o" onclick="closeModal('modal-links')">انصراف</button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> ذخیره</button>
      </div>
    </div>
  </div>
</div>

<!-- Create Sub Modal -->
<div class="modal-bg" id="modal-create-sub">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-folder-plus"></i></div>
      <div class="modal-v2-title">ایجاد گروه جدید</div>
      <div class="modal-v2-sub">ایجاد صفحه عمومی مجزا برای مدیریت کانفیگ‌ها</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> نام گروه</label>
        <input class="modal-v2-input" id="ns-name" placeholder="مثال: کانال تلگرام">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> توضیحات (اختیاری)</label>
        <input class="modal-v2-input" id="ns-desc" placeholder="توضیح کوتاه">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-lock"></i> رمز عبور صفحه عمومی (اختیاری)</label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="خالی = بدون رمز عبور">
      </div>
      <div class="cl" style="margin-top:16px"><i class="ti ti-info-circle"></i><span>صفحه عمومی از طریق یک لینک یکتا در اینترنت قابل دسترسی خواهد بود.</span></div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-sub')" style="flex:.6">انصراف</button>
        <button class="btn btn-pur" onclick="createSub()"><i class="ti ti-folder-plus"></i> ایجاد گروه</button>
      </div>
    </div>
  </div>
</div>

<!-- Edit Link Modal -->
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> ویرایش کانفیگ</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:14px"><label>برچسب</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:14px">
      <div class="fg" style="flex:1"><label>حجم (۰ = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:14px"><label>انقضا (روز از الان، ۰ = بدون تغییر)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:18px"><label>یادداشت</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>برای حفظ تاریخ انقضای فعلی، مقدار ۰ را وارد کنید.</span></div>
    <div style="margin-top:18px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">انصراف</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> ذخیره تغییرات</button>
    </div>
  </div>
</div>

<!-- Mobile Topbar -->
<div class="mob-top">
  <div class="ml">
    <svg class="mob-logo-svg" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="16" stroke="url(#mobGrad)" stroke-width="1.2"/><defs><linearGradient id="mobGrad" x1="0" y1="0" x2="36" y2="36"><stop stop-color="#2B66FF"/><stop offset="0.5" stop-color="#6C5CE7"/><stop offset="1" stop-color="#FF3B65"/></linearGradient></defs><path d="M18 5L20 16L31 18L20 20L18 31L16 20L5 18L16 16Z" fill="url(#mobGrad)" opacity="0.9"/></svg>
    <span class="mob-title">SPIDER PANEL</span>
  </div>
  <div class="mob-right">
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>

<div class="overlay" id="overlay"></div>

<!-- Sidebar - RTL: right side -->
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <svg class="logo-svg" viewBox="0 0 48 48" fill="none">
      <circle cx="24" cy="24" r="22" stroke="url(#sbGrad)" stroke-width="1.5"/>
      <defs><linearGradient id="sbGrad" x1="0" y1="0" x2="48" y2="48"><stop stop-color="#2B66FF"/><stop offset="0.5" stop-color="#6C5CE7"/><stop offset="1" stop-color="#FF3B65"/></linearGradient></defs>
      <path d="M24 6L26 22L42 24L26 26L24 42L22 26L6 24L22 22Z" fill="url(#sbGrad)" opacity="0.9"/>
      <circle cx="24" cy="24" r="3.5" fill="url(#sbGrad)"/>
      <path d="M17 14L21 20" stroke="url(#sbGrad)" stroke-width="1.2"/>
      <path d="M31 14L27 20" stroke="url(#sbGrad)" stroke-width="1.2"/>
      <path d="M17 34L21 28" stroke="url(#sbGrad)" stroke-width="1.2"/>
      <path d="M31 34L27 28" stroke="url(#sbGrad)" stroke-width="1.2"/>
    </svg>
    <div class="logo-text"><div class="logo-name">SPIDER PANEL</div><div class="logo-sub">مدیریت شبکه سازمانی</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">پنل</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">۰</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> گروه‌ها <span class="nav-badge" id="subs-nb">۰</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> اشتراک‌ها</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="nav-badge" id="conns-nb">۰</span></div>
    <div class="nav-sec">سیستم</div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> گزارش فعالیت</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> خطاها</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> تست WebSocket</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
  </div>
  <div class="sb-foot">
    <div class="user-chip">
      <div class="user-avatar"><i class="ti ti-user"></i></div>
      <div><div class="user-name">Admin</div><div class="user-role">مدیر سیستم</div></div>
    </div>
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-icon"></i> <span id="theme-label">حالت روشن</span></button>
    <a class="tg-btn" href="https://t.me/CodeBoxo" target="_blank" rel="noopener"><i class="ti ti-brand-telegram"></i> @CodeBoxo</a>
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>

<!-- Main Content -->
<main class="main">

<!-- Overview / Dashboard -->
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div class="tb-left"><div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="tb-sub" id="last-upd">در حال بارگذاری...</div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot dg pulse"></span> آنلاین</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> بروزرسانی</button>
    </div>
  </div>
  <div class="metrics">
    <div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">اتصالات فعال</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span class="dot dg pulse"></span> WebSocket / XHTTP زنده</div></div>
    <div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label">ترافیک کل</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">از زمان راه‌اندازی</div></div>
    <div class="metric suc"><div class="m-icon suc"><i class="ti ti-link"></i></div><div class="m-label">کانفیگ‌های فعال</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">از کل</div></div>
    <div class="metric pur"><div class="m-icon pur"><i class="ti ti-folders"></i></div><div class="m-label">گروه‌ها</div><div class="m-val" id="m-subs">—</div><div class="m-sub">فعال</div></div>
  </div>

  <!-- Quick Actions -->
  <div class="quick-actions">
    <button class="qa-btn" onclick="openInboundModal()"><i class="ti ti-square-rounded-plus"></i><span>ساخت کانفیگ جدید</span></button>
    <button class="qa-btn" onclick="navTo('subgroups')"><i class="ti ti-folders"></i><span>مدیریت گروه‌ها</span></button>
    <button class="qa-btn" onclick="navTo('traffic')"><i class="ti ti-chart-area"></i><span>مشاهده ترافیک</span></button>
    <button class="qa-btn" onclick="navTo('settings')"><i class="ti ti-settings"></i><span>تنظیمات سرور</span></button>
  </div>

  <div class="vless-box">
    <div class="vl-header">
      <div class="vl-title"><i class="ti ti-link"></i> کانفیگ پیش‌فرض (نامحدود)</div>
      <span class="badge bg-blue"><span class="dot db"></span> TLS 443 · WS</span>
    </div>
    <div class="vl-code" id="vless-main">در حال بارگذاری...</div>
    <div class="vl-actions">
      <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> کپی</button>
      <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> کانفیگ‌های محدود</button>
      <button class="btn btn-pur" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> گروه‌ها</button>
    </div>
  </div>

  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> ترافیک ساعتی (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-donut"></i> توزیع</div><div class="ch-sm"><canvas id="ch2"></canvas></div></div>
  </div>

  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-activity"></i> وضعیت سرویس‌ها</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> احراز هویت UUID</span><span class="sr-v" style="color:var(--green-t)">● فعال · Strict</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> تونل VLESS / WS</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● فعال · ۳ حالت</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-folders"></i> گروه‌ها</span><span class="sr-v" style="color:var(--green-t)">● فعال v9</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> API اشتراک</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptime-inline">—</span></div>
      <div class="sr" style="flex-direction:column;align-items:flex-start;gap:6px">
        <div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> بار نسبی</span><span class="sr-v" id="bw-pct">—%</span></div>
        <div class="spbar" style="width:100%"><div class="spfill" id="bw-bar" style="width:0%"></div></div>
      </div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="ml-auto badge bg-blue" id="lsummary-badge">۰</span></div>
      <div id="lsummary">—</div>
    </div>
  </div>

  <!-- Server Information Panel -->
  <div class="server-panel">
    <div class="card-title"><i class="ti ti-server-2"></i> اطلاعات سرور</div>
    <div class="server-row">
      <span class="server-info-label"><i class="ti ti-cpu"></i> CPU</span>
      <div class="server-bar-wrap"><div class="server-bar"><div class="server-bar-f cpu" style="width:32%"></div></div></div>
      <span class="server-info-val">۳۲٪</span>
    </div>
    <div class="server-row">
      <span class="server-info-label"><i class="ti ti-memory"></i> RAM</span>
      <div class="server-bar-wrap"><div class="server-bar"><div class="server-bar-f ram" style="width:46%"></div></div></div>
      <span class="server-info-val">۴۶٪</span>
    </div>
    <div class="server-row">
      <span class="server-info-label"><i class="ti ti-database"></i> دیسک</span>
      <div class="server-bar-wrap"><div class="server-bar"><div class="server-bar-f disk" style="width:61%"></div></div></div>
      <span class="server-info-val">۶۱٪</span>
    </div>
    <div class="server-row">
      <span class="server-info-label"><i class="ti ti-network"></i> شبکه</span>
      <div class="server-bar-wrap"><div class="server-bar"><div class="server-bar-f net" style="width:42%"></div></div></div>
      <span class="server-info-val">۱۴۶ Mbps</span>
    </div>
  </div>

  <!-- Active Users Table -->
  <div class="card" style="margin-top:16px">
    <div class="card-title"><i class="ti ti-users"></i> کاربران / کانفیگ‌های فعال</div>
    <div style="overflow-x:auto">
      <table class="data-table">
        <thead><tr><th>نام کاربری</th><th>مصرف کل</th><th>انقضا</th><th>پروتکل</th><th>پورت</th><th>عملیات</th></tr></thead>
        <tbody><tr><td>user_1</td><td>۲.۴۵ GB</td><td>۳۰ روز</td><td>VLESS</td><td>۴۴۳</td><td><button class="btn btn-sm btn-g">ویرایش</button> <button class="btn btn-sm btn-d">حذف</button> <button class="btn btn-sm btn-pur">کپی لینک</button></td></tr><tr><td>user_2</td><td>۸۵۰ MB</td><td>۱۴ روز</td><td>VMESS</td><td>۴۴۳</td><td><button class="btn btn-sm btn-g">ویرایش</button> <button class="btn btn-sm btn-d">حذف</button> <button class="btn btn-sm btn-pur">کپی لینک</button></td></tr><tr><td>user_3</td><td>۱۲.۸ GB</td><td>منقضی</td><td>Trojan</td><td>۴۴۳</td><td><button class="btn btn-sm btn-g">ویرایش</button> <button class="btn btn-sm btn-d">حذف</button> <button class="btn btn-sm btn-pur">کپی لینک</button></td></tr></tbody>
      </table>
    </div>
    <div class="pagination"><button class="pg-btn active">۱</button><button class="pg-btn">۲</button><button class="pg-btn">۳</button><button class="pg-btn">...</button><button class="pg-btn">۱۲</button></div>
  </div>

  <div class="dash-footer">
    <span class="df-text">SPIDER PANEL v1.0 · Railway · ۲۰۲۵</span>
    <a class="df-link" href="https://t.me/CodeBoxo" target="_blank"><i class="ti ti-brand-telegram"></i> t.me/CodeBoxo</a>
  </div>
</section>

<!-- Configs -->
<section class="pg" id="pg-links">
  <div class="topbar">
    <div class="tb-left"><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ایجاد و مدیریت کانفیگ‌ها با حجم، انقضا و گروه‌بندی</div></div>
    <div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">۰ کانفیگ</span><button class="btn btn-p btn-sm" onclick="openInboundModal()"><i class="ti ti-plus"></i> کانفیگ جدید</button></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">ایجاد کانفیگ جدید</div>
        <div class="cp-head-sub">UUID تصادفی · انتخاب حجم، انقضا و پروتکل</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> مشخصات کانفیگ</div>
          <input class="cp-input-full" id="nl-label" placeholder="مثال: کاربر علی">
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-note" placeholder="یادداشت (اختیاری)">
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> گروه و انقضا</div>
          <select class="cp-input-full fs" id="nl-sub"><option value="">— بدون گروه —</option></select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="انقضا (روز) · ۰ = نامحدود">
          </div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">نامحدود</span>
            <span class="chip" onclick="setExpiry(7,this)">۷ روز</span>
            <span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span>
            <span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> حجم ترافیک</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="۰ = نامحدود">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">۱ GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">۵ GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">۱۰ GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">۵۰ GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> پروتکل انتقال</div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WebSocket</option>
          <option value="xhttp-packet-up">XHTTP Ultra · packet-up</option>
          <option value="xhttp-stream-up">XHTTP Ultra · stream-up</option>
        </select>
        <div class="proto-cards">
          <div class="proto-card active" data-val="vless-ws" onclick="selectProto('vless-ws',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-link"></i></div>
            <div class="proto-card-title">VLESS / WS</div>
            <div class="proto-card-desc">پایدار و عمومی</div>
          </div>
          <div class="proto-card" data-val="xhttp-packet-up" onclick="selectProto('xhttp-packet-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-bolt"></i></div>
            <div class="proto-card-title">XHTTP · packet-up</div>
            <div class="proto-card-desc">سازگار با CDN</div>
          </div>
          <div class="proto-card" data-val="xhttp-stream-up" onclick="selectProto('xhttp-stream-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-rocket"></i></div>
            <div class="proto-card-title">XHTTP · stream-up</div>
            <div class="proto-card-desc">تاخیر کمتر</div>
          </div>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID به صورت تصادفی تولید می‌شود · فقط UUIDهای ثبت شده می‌توانند متصل شوند · پروتکل پس از ایجاد قابل تغییر نیست.</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> ایجاد کانفیگ</button>
      </div>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>

<!-- Sub Groups -->
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div class="tb-left"><div class="tb-title"><i class="ti ti-folders"></i> گروه‌ها</div><div class="tb-sub">هر گروه صفحه عمومی مجزا با کانفیگ‌های اختصاصی دارد</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">۰ گروه</span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> گروه جدید</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="جستجوی گروه..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">برای سازماندهی کانفیگ‌ها یک گروه ایجاد کنید</div></div>
  </div>
</section>

<!-- Subscriptions -->
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-rss"></i> اشتراک‌ها</div><div class="tb-sub">لینک‌های اشتراک برای اپلیکیشن‌های V2Ray</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-rss"></i> اشتراک‌های انفرادی</div>
      <p style="font-size:12px;color:var(--t3);line-height:1.8;margin-bottom:14px">هر کانفیگ لینک اشتراک اختصاصی خود را دارد. روی آیکون <i class="ti ti-rss"></i> کارت کانفیگ کلیک کنید.</p>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-database"></i> اشتراک کامل (مدیر)</div>
      <p style="font-size:12px;color:var(--t3);line-height:1.8;margin-bottom:4px">شامل تمام کانفیگ‌های فعال.</p>
      <div class="sub-box"><span class="sub-url" id="sub-all-url">در حال بارگذاری...</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
      <div class="cl amber" style="margin-top:13px"><i class="ti ti-alert-triangle"></i><span>این آدرس فقط در مرورگری که وارد پنل شده کار می‌کند (نیاز به کوکی نشست دارد).</span></div>
    </div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-folders"></i> لینک‌های اشتراک گروه‌ها</div>
    <div id="sub-groups-list">در حال بارگذاری...</div>
  </div>
</section>

<!-- Traffic -->
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div class="tb-left"><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل و مانیتورینگ مصرف پهنای باند</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> بروزرسانی</button></div>
  </div>
  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> ترافیک کل</div>
      <div class="traf-main-val" id="t-traffic">—<span class="m-unit">MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">میانگین ساعتی</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">مگابایت در ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">اوج مصرف</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">بالاترین ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">کمترین مصرف</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">مگابایت در ساعت</div></div>
    </div>
  </div>
  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> روند ترافیک</div>
        <div class="traf-chart-sub">مگابایت در ساعت</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> مصرف</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> میانگین</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>

<!-- Connections -->
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div class="tb-left"><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده IP و ترافیک هر اتصال</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> بروزرسانی</button></div>
  </div>
  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="conn-hero-label">اتصالات زنده</div>
      <div class="conn-hero-val" id="ch-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-transfer"></i></div>
      <div class="conn-hero-label">ترافیک لحظه‌ای کل</div>
      <div class="conn-hero-val" id="ch-traffic">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-clock"></i></div>
      <div class="conn-hero-label">میانگین زمان اتصال</div>
      <div class="conn-hero-val" id="ch-avgdur">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div>
      <div class="conn-hero-label">IPهای یکتا</div>
      <div class="conn-hero-val" id="ch-uniq">—</div>
    </div>
  </div>
  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> لیست اتصالات</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> بروزرسانی خودکار هر ۵ ثانیه</div>
  </div>
  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">اتصال فعالی وجود ندارد</div>
    <div class="conn-empty-v2-sub">کلاینت‌های متصل شده اینجا نمایش داده می‌شوند</div>
  </div>
</section>

<!-- Security -->
<section class="pg" id="pg-security">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-shield-lock"></i> امنیت</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-lock"></i> رمزنگاری</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● فعال (۴۴۳)</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> اثر انگشت</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> پروتکل‌ها</span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> هش رمز عبور</span><span class="sr-v">SHA-256 + Salt</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> نشست</span><span class="sr-v">HttpOnly · ۷ روز</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-shield-check"></i> کنترل دسترسی</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> احراز هویت UUID</span><span class="sr-v" style="color:var(--green-t)">● فعال v9</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> فعال/غیرفعال کردن کانفیگ</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> سهمیه ترافیک</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> تاریخ انقضا</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> رمز عبور صفحه گروه</span><span class="sr-v" style="color:var(--green-t)">● اختیاری · SHA-256</span></div>
    </div>
  </div>
</section>

<!-- Logs -->
<section class="pg" id="pg-logs">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-history"></i> گزارش فعالیت</div><div class="tb-sub">تاریخچه کامل رویدادها</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>هنوز فعالیتی ثبت نشده</p></div></div>
</section>

<!-- Errors -->
<section class="pg" id="pg-errors">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-alert-triangle"></i> خطاها</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> گزارش خطا</div><div id="errs-full">—</div></div>
</section>

<!-- WebSocket Test -->
<section class="pg" id="pg-testws">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-wifi"></i> تست WebSocket</div></div></div>
  <div class="card" style="max-width:700px">
    <div class="cl amber" style="margin-top:0;margin-bottom:14px"><i class="ti ti-alert-triangle"></i><span>فقط UUIDهای ثبت شده و فعال می‌توانند متصل شوند (این تست فقط VLESS/WS را بررسی می‌کند؛ XHTTP باید از کلاینت تست شود).</span></div>
    <div class="form-row" style="margin-bottom:14px">
      <div class="fg" style="flex:1"><label>UUID (باید در کانفیگ‌ها موجود باشد)</label><input class="fi" id="ws-uuid" placeholder="UUID یک کانفیگ فعال" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> اتصال</button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> قطع</button>
    </div>
    <div class="form-row" style="margin-bottom:14px">
      <input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> ارسال</button>
    </div>
    <div style="background:rgba(0,0,0,0.08);border:1.5px solid var(--card-b);border-radius:14px;padding:16px;height:260px;overflow-y:auto;font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:11px;line-height:2" id="ws-log">
      <p style="color:var(--t3)">منتظر اتصال...</p>
    </div>
  </div>
</section>

<!-- Settings -->
<section class="pg" id="pg-settings">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div></div></div>
  <div class="g2">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> آنلاین · Railway</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پورت</div><div class="srv-tile-val">۴۴۳ (TLS)</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">نسخه</div><div class="srv-tile-val">v1.0</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label">فریمورک</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پلتفرم</div><div class="srv-tile-val">Railway</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">ذخیره‌سازی</div><div class="srv-tile-val">فایل JSON (/data)</div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">تغییر رمز عبور</div>
          <div class="pw-hero-sub">یک رمز عبور قوی انتخاب کرده و آن را در جای امن نگهداری کنید</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field">
          <label>رمز عبور فعلی</label>
          <input class="pw-input" type="password" id="cp-cur" placeholder="رمز عبور فعلی را وارد کنید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field" style="margin-bottom:6px">
          <label>رمز عبور جدید</label>
          <input class="pw-input" type="password" id="cp-new" placeholder="حداقل ۴ کاراکتر" oninput="checkPwStrength(this.value)">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-strength" id="pw-strength-bar">
          <div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div>
        </div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> قدرت رمز عبور</div>
        <div class="pw-reqs">
          <span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> حداقل ۴ کاراکتر</span>
          <span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> شامل عدد</span>
          <span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> حروف بزرگ و کوچک</span>
        </div>
        <div class="pw-field" style="margin-bottom:20px">
          <label>تکرار رمز عبور جدید</label>
          <input class="pw-input" type="password" id="cp-cf" placeholder="رمز عبور جدید را تکرار کنید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
        </div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> ذخیره رمز عبور جدید</button>
      </div>
    </div>
  </div>
</section>
</main>

<script>
var isDark=true;
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  var icon=document.getElementById('theme-icon'),label=document.getElementById('theme-label');
  icon.className='ti '+(dark?'ti-moon':'ti-sun');
  label.textContent=dark?'حالت روشن':'حالت تاریک';
  var mobI=document.getElementById('theme-mob-icon');if(mobI)mobI.className='ti '+(dark?'ti-moon':'ti-sun');
}
function toggleTheme(){isDark=!isDark;localStorage.setItem('sp-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
function toast(msg,type){
  type=type||'';
  var t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(function(){t.classList.remove('show');},2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1048576)return (b/1024).toFixed(1)+' KB';if(b<1073741824)return (b/1048576).toFixed(2)+' MB';return (b/1073741824).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,function(d){return '۰۱۲۳۴۵۶۷۸۹'[d];})}
function esc(s){return String(s||'').replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];})}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/864e5)}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی شده</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
  var d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی شده</span>';
  if(d<=3)return '<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> '+d+' روز باقی‌مانده</span>';
  return '<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> '+d+' روز باقی‌مانده</span>';
}
function protoBadge(p){
  var m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp-packet-up':['XHTTP · packet-up','pc-xhttp'],'xhttp-stream-up':['XHTTP · stream-up','pc-xhttp'],'xhttp-stream-one':['XHTTP ULTRA','pc-ultra']};
  var v=m[p]||m['vless-ws'];
  return '<span class="proto-chip '+v[1]+'">'+v[0]+'</span>';
}

async function checkAuth(){try{var r=await fetch('/api/me');var d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts){
  opts=opts||{};
  var r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}
function setQuota(val,unit,el){
  document.getElementById('nl-val').value = val===0?'':val;
  document.getElementById('nl-unit').value = unit;
  document.querySelectorAll('#quota-chips .chip').forEach(function(c){c.classList.remove('active');});
  el.classList.add('active');
}
function setExpiry(days,el){
  document.getElementById('nl-exp').value = days===0?'':days;
  document.querySelectorAll('#exp-chips .chip').forEach(function(c){c.classList.remove('active');});
  el.classList.add('active');
}
function selectProto(val,el){
  document.getElementById('nl-proto').value = val;
  document.querySelectorAll('.proto-card').forEach(function(c){c.classList.remove('active');});
  el.classList.add('active');
}
var sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){
  document.querySelectorAll('.nav-it').forEach(function(n){n.classList.toggle('on',n.dataset.pg===name);});
  document.querySelectorAll('.pg').forEach(function(p){p.classList.toggle('on',p.id==='pg-'+name);});
  var loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity};
  if(loaders[name])loaders[name]();
  closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(function(el){el.addEventListener('click',function(){navTo(el.dataset.pg);});});
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}

/* Inbound Modal Functions */
function openInboundModal(){document.getElementById('inbound-modal').classList.add('open');onNetworkChange();}
function closeInboundModal(){document.getElementById('inbound-modal').classList.remove('open')}
function onProtocolChange(){
  var proto=document.getElementById('ib-protocol').value;
}
function onNetworkChange(){
  var net=document.getElementById('ib-network').value;
  ['ts-ws','ts-grpc','ts-xhttp','ts-tcp'].forEach(function(id){document.getElementById(id).classList.add('hidden');});
  if(net==='ws')document.getElementById('ts-ws').classList.remove('hidden');
  else if(net==='grpc')document.getElementById('ts-grpc').classList.remove('hidden');
  else if(net==='xhttp')document.getElementById('ts-xhttp').classList.remove('hidden');
  else if(net==='tcp')document.getElementById('ts-tcp').classList.remove('hidden');
}
var currentSecurity='none';
function setSecurity(type,btn){
  currentSecurity=type;
  document.querySelectorAll('.sec-tog').forEach(function(b){b.classList.remove('active');});
  btn.classList.add('active');
  document.getElementById('sec-tls').classList.toggle('hidden',type!=='tls');
  document.getElementById('sec-reality').classList.toggle('hidden',type!=='reality');
}
async function submitInbound(){
  var protocol=document.getElementById('ib-protocol').value;
  var port=document.getElementById('ib-port').value||'443';
  var traffic=document.getElementById('ib-traffic').value;
  var expire=document.getElementById('ib-expire').value;
  var iplimit=document.getElementById('ib-iplimit').value||'0';
  var network=document.getElementById('ib-network').value;

  var body={label:'New Config',limit_value:traffic||0,limit_unit:'GB',note:'',protocol:'vless-ws'};
  if(expire){
    var days=Math.ceil((new Date(expire)-Date.now())/864e5);
    if(days>0)body.expires_days=days;
  }
  if(network==='xhttp'){
    var mode=document.getElementById('ib-xhttp-mode').value;
    body.protocol='xhttp-'+mode;
  }
  try{
    var r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error('failed');
    closeInboundModal();
    toast('کانفیگ با موفقیت ایجاد شد','ok');loadLinks();
  }catch(e){toast('خطا در ایجاد کانفیگ','err')}
}

var prevTraf=0,ch1,ch2,ch3,currentSubId;
async function fetchStats(){
  try{
    var r=await authF('/stats'),d=await r.json();
    document.getElementById('m-conns').textContent=d.active_connections;
    document.getElementById('conns-nb').textContent=d.active_connections;
    document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    document.getElementById('m-alinks').textContent=d.active_links||'—';
    document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';
    document.getElementById('m-subs').textContent=d.subs_count||'—';
    document.getElementById('errs-badge').textContent=d.total_errors+' خطا';
    document.getElementById('uptime-inline').textContent=d.uptime;
    document.getElementById('uptime-badge').textContent='Railway · '+d.uptime;
    document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('en-US');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' اتصال';
    document.getElementById('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    var delta=d.total_traffic_mb-prevTraf,pct=Math.min(100,Math.round((delta/50)*100));
    document.getElementById('bw-pct').textContent=pct+'%';
    document.getElementById('bw-bar').style.width=pct+'%';
    prevTraf=d.total_traffic_mb;
    if(d.hourly){
      var labels=Object.keys(d.hourly).sort(),vals=labels.map(function(k){return +(d.hourly[k]/1048576).toFixed(2);});
      [ch1,ch3].forEach(function(c){if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update();});
      if(vals.length){var avg=vals.reduce(function(a,b){return a+b;},0)/vals.length,peak=Math.max.apply(null,vals);document.getElementById('t-avg').innerHTML=avg.toFixed(2)+'<span class="m-unit">MB</span>';document.getElementById('t-peak').innerHTML=peak.toFixed(2)+'<span class="m-unit">MB</span>';}
    }
    renderErrs(d.recent_errors||[]);
  }catch(e){console.error(e)}
}
function renderErrs(errs){
  var el=document.getElementById('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:12px;font-size:12.5px;display:flex;align-items:center;gap:6px"><i class="ti ti-circle-check"></i> خطایی وجود ندارد</div>';return}
  el.innerHTML=errs.slice().reverse().map(function(e){return '<div class="erow"><div class="etime"><i class="ti ti-clock"></i>'+new Date(e.time).toLocaleString('en-US')+'</div><div class="emsg">'+esc(e.error)+(e.url?' &mdash; '+esc(e.url):'')+'</div></div>';}).join('');
}
async function loadActivity(){
  try{
    var r=await authF('/api/activity'),d=await r.json();
    var logs=(d.logs||[]).slice().reverse();
    var el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');
    if(!logs.length){el.innerHTML='';em.style.display='block';return}
    em.style.display='none';
    var icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
    var kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};
    el.innerHTML=logs.map(function(l){
      return '<div class="log-item"><div class="log-ic '+l.level+'"><i class="ti '+(icMap[l.level]||'ti-info-circle')+'"></i></div><div class="log-body"><div class="log-msg">'+esc(l.message)+'</div><div class="log-time"><i class="ti ti-clock"></i> '+new Date(l.time).toLocaleString('en-US')+' <span class="log-kind">'+(kindFa[l.kind]||l.kind)+'</span></div></div></div>';
    }).join('');
  }catch(e){console.error(e)}
}
var allSubsList=[],allLinksList=[];
async function loadLinks(){
  try{
    var res=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    var links=(await res[0].json()).links||[];
    var subs=(await res[1].json()).subs||[];
    allSubsList=subs;allLinksList=links;
    var nlSub=document.getElementById('nl-sub');
    nlSub.innerHTML='<option value="">&mdash; بدون گروه &mdash;</option>'+subs.map(function(s){return '<option value="'+esc(s.sub_id)+'">'+esc(s.name)+'</option>';}).join('');
    document.getElementById('links-nb').textContent=links.length;
    document.getElementById('links-pg-cnt').textContent=links.length+' کانفیگ';
    document.getElementById('lsummary-badge').textContent=links.length;
    var grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!links.length){grid.innerHTML='';empty.style.display='block';document.getElementById('lsummary').innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>بدون کانفیگ</p></div>';return}
    empty.style.display='none';
    var subMap={};subs.forEach(function(s){subMap[s.sub_id]=s.name;});
    grid.innerHTML=links.map(function(l){
  var lim=l.limit_bytes===0?'&infin;':fmtB(l.limit_bytes);
  var pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
  var bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
  var allowed=l.active&&!l.expired;
  var cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
  return '<div class="cfg-card '+cardCls+'"><div class="cfg-row"><span class="cfg-status-dot '+(allowed?'pulse':'')+'"></span><div class="cfg-identity"><div class="cfg-label">'+esc(l.label)+'</div><div class="cfg-sub-meta"><span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText(\''+l.uuid+'\').then(function(){toast(\'UUID کپی شد\',\'ok\');})" title="'+l.uuid+'"><i class="ti ti-fingerprint"></i> '+l.uuid.slice(0,10)+'&hellip;</span><span>'+new Date(l.created_at).toLocaleDateString('en-US')+'</span></div></div><div class="cfg-divider-v"></div><div class="cfg-usage-col"><div class="ubar"><div class="ubar-f" style="width:'+pct+'%;background:'+bc+'"></div></div><div class="utxt"><span>'+fmtB(l.used_bytes)+'</span><span>از '+lim+'</span></div></div><div class="cfg-divider-v"></div><div class="cfg-exp-col">'+expChip(l.expires_at,l.expired)+'</div><div class="cfg-divider-v"></div><div class="cfg-badges-col">'+protoBadge(l.protocol)+(l.sub_id&&allSubsList.find(function(s){return s.sub_id===l.sub_id;})?'<span class="cfg-sub-tag"><i class="ti ti-folder"></i> '+esc(allSubsList.find(function(s){return s.sub_id===l.sub_id;}).name)+'</span>':'')+'</div><div class="cfg-divider-v"></div><div class="cfg-actions"><button class="tog'+(allowed?' on':'')+'" onclick="toggleActive(\''+l.uuid+'\','+(!l.active)+')" title="فعال/غیرفعال"></button><button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText(\''+esc(l.vless_link)+'\').then(function(){toast(\'لینک کپی شد\',\'ok\');})" title="کپی لینک"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText(\''+esc(l.sub_url)+'\').then(function(){toast(\'لینک اشتراک کپی شد\',\'ok\');})" title="لینک اشتراک"><i class="ti ti-rss"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="showQR(\''+esc(l.vless_link)+'\')" title="QR"><i class="ti ti-qrcode"></i></button><button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink(\''+l.uuid+'\')" title="ویرایش"><i class="ti ti-edit"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="resetUsage(\''+l.uuid+'\')" title="بازنشانی مصرف"><i class="ti ti-rotate"></i></button><button class="btn btn-sm btn-d btn-icon" onclick="deleteLink(\''+l.uuid+'\')" title="حذف"><i class="ti ti-trash"></i></button></div></div></div>';
}).join('');
    document.getElementById('lsummary').innerHTML=links.slice(0,6).map(function(l){return '<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti '+(l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x')+'" style="color:'+(l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)')+'"></i>'+esc(l.label)+'</span><span class="sr-v" style="font-size:10px">'+fmtB(l.used_bytes)+' / '+(l.limit_bytes===0?'&infin;':fmtB(l.limit_bytes))+'</span></div>';}).join('');
  }catch(e){console.error(e)}
}
async function createLink(){
  var label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';
  var val=document.getElementById('nl-val').value;
  var unit=document.getElementById('nl-unit').value;
  var exp=document.getElementById('nl-exp').value;
  var note=document.getElementById('nl-note').value.trim();
  var sub_id=document.getElementById('nl-sub').value||null;
  var protocol=document.getElementById('nl-proto').value||'vless-ws';
  try{
    var r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label:label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note:note,sub_id:sub_id,protocol:protocol})});
    if(!r.ok)throw new Error('failed');
    ['nl-label','nl-val','nl-exp','nl-note'].forEach(function(id){document.getElementById(id).value='';});
    toast('کانفیگ ایجاد شد','ok');loadLinks();
  }catch(e){toast('خطا در ایجاد کانفیگ','err')}
}
function openEditLink(uuid){
  var l=allLinksList.find(function(x){return x.uuid===uuid;});
  if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label;
  document.getElementById('el-note').value=l.note||'';
  if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
  else{document.getElementById('el-val').value=(l.limit_bytes/1048576).toFixed(0);document.getElementById('el-unit').value='MB';}
  document.getElementById('el-exp').value='';
  openModal('modal-edit-link');
}
async function saveEditLink(){
  var uuid=document.getElementById('el-uuid').value;
  var label=document.getElementById('el-label').value.trim();
  var note=document.getElementById('el-note').value.trim();
  var val=document.getElementById('el-val').value;
  var unit=document.getElementById('el-unit').value;
  var exp=document.getElementById('el-exp').value;
  var body={label:label,note:note,limit_value:val||0,limit_unit:unit};
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    var r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('کانفیگ بروزرسانی شد','ok');loadLinks();
  }catch(e){toast('خطا در بروزرسانی','err')}
}
async function toggleActive(uuid,newState){
  try{var r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function resetUsage(uuid){
  try{var r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف بازنشانی شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function deleteLink(uuid){
  if(!confirm('این کانفیگ حذف شود؟'))return;
  try{var r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
var allSubsRaw=[];
async function loadSubs(){
  try{
    var r=await authF('/api/subs'),d=await r.json();
    var subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-nb').textContent=subs.length;
    document.getElementById('subs-pg-cnt').textContent=subs.length+' گروه';
    renderSubsGrid(subs);
  }catch(e){console.error(e)}
}
function renderSubsGrid(subs){
  var grid=document.getElementById('subs-grid');
  if(!subs.length){
    grid.innerHTML='<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">برای سازماندهی کانفیگ‌ها یک گروه ایجاد کنید</div></div>';
    return;
  }
  grid.innerHTML=subs.map(function(s){
    return '<div class="sub-card"><div class="sub-card-top"><div class="sub-card-head-v2"><div class="sub-card-icon"><i class="ti ti-folder"></i></div><div class="sub-card-titles"><div class="sub-card-name-v2">'+esc(s.name)+'</div>'+(s.desc?'<div class="sub-card-desc-v2">'+esc(s.desc)+'</div>':'<div class="sub-card-desc-v2" style="opacity:.5">بدون توضیح</div>')+'</div><div class="sub-card-lock-badge '+(s.has_password?'locked':'open')+'" title="'+(s.has_password?'محافظت شده با رمز':'عمومی')+'"><i class="ti '+(s.has_password?'ti-lock':'ti-lock-open')+'"></i></div></div><div class="sub-card-stats"><div class="sub-card-stat"><div class="sub-card-stat-val">'+s.links_count+'</div><div class="sub-card-stat-label">کانفیگ</div></div><div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">'+s.active_count+'</div><div class="sub-card-stat-label">فعال</div></div><div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">'+esc(s.total_used_fmt)+'</div><div class="sub-card-stat-label">مصرف</div></div></div></div><div class="sub-card-url-row"><span class="sub-card-url-text">'+esc(s.public_url)+'</span><button class="sub-card-url-copy" onclick="navigator.clipboard.writeText(\''+esc(s.public_url)+'\').then(function(){toast(\'لینک عمومی کپی شد\',\'ok\');})" title="کپی"><i class="ti ti-copy"></i></button><button class="sub-card-url-copy" onclick="window.open(\''+esc(s.public_url)+'\',\'_blank\')" title="باز کردن"><i class="ti ti-external-link"></i></button></div><div class="sub-card-bottom"><button class="btn btn-sm btn-g" onclick="openSubLinks(\''+esc(s.sub_id)+'\',\''+esc(s.name)+'\')"><i class="ti ti-link-plus"></i> کانفیگ‌ها</button><button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText(\''+esc(s.sub_url)+'\').then(function(){toast(\'لینک اشتراک کپی شد\',\'ok\');})"><i class="ti ti-rss"></i> اشتراک</button><button class="btn btn-sm btn-g btn-icon" onclick="showQR(\''+esc(s.sub_url)+'\')" title="QR"><i class="ti ti-qrcode"></i></button><button class="btn btn-sm btn-d btn-icon" onclick="deleteSub(\''+esc(s.sub_id)+'\')" title="حذف"><i class="ti ti-trash"></i></button></div></div>';
  }).join('');
}
function filterSubs(q){
  q=q.trim().toLowerCase();
  if(!q){renderSubsGrid(allSubsRaw);return}
  renderSubsGrid(allSubsRaw.filter(function(s){return s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q);}));
}
async function createSub(){
  var name=document.getElementById('ns-name').value.trim()||'گروه جدید';
  var desc=document.getElementById('ns-desc').value.trim();
  var pw=document.getElementById('ns-pw').value;
  try{
    var r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:name,desc:desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(function(id){document.getElementById(id).value='';});
    closeModal('modal-create-sub');
    toast('گروه ایجاد شد','ok');loadSubs();
  }catch(e){toast('خطا در ایجاد گروه','err')}
}
async function deleteSub(sub_id){
  if(!confirm('این گروه حذف شود؟ کانفیگ‌ها حذف نمی‌شوند.'))return;
  try{var r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('گروه حذف شد','ok');loadSubs();loadLinks();}catch(e){toast('خطا','err')}
}
var lmodalLinks=[],lmodalInSub=new Set();
async function openSubLinks(sub_id,name){
  currentSubId=sub_id;
  document.getElementById('modal-sub-name').textContent=name;
  document.getElementById('modal-links-body').innerHTML='<div style="color:var(--t3);font-size:12px;padding:24px;text-align:center"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite;font-size:22px"></i></div>';
  document.getElementById('lmodal-search-inp').value='';
  openModal('modal-links');
  try{
    var res=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    var links=(await res[0].json()).links||[];
    var subs=(await res[1].json()).subs||[];
    var thisSub=subs.find(function(s){return s.sub_id===sub_id;});
    lmodalInSub=new Set(thisSub?thisSub.link_ids:[]);
    lmodalLinks=links;
    renderLmodalList(links);
  }catch(e){toast('خطا در بارگذاری','err')}
}
function renderLmodalList(links){
  var body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div class="empty" style="padding:36px"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>';updateLmodalCount();return}
  body.innerHTML=links.map(function(l){
    var checked=lmodalInSub.has(l.uuid);
    var on=l.active&&!l.expired;
    return '<div class="lrow-v2 '+(checked?'checked':'')+'" data-uuid="'+l.uuid+'" data-name="'+esc(l.label).toLowerCase()+'" onclick="toggleLrow(\''+l.uuid+'\',this)"><div class="lrow-v2-check"><i class="ti ti-check"></i></div><div class="lrow-v2-avatar"><i class="ti ti-key"></i></div><div class="lrow-v2-info"><div class="lrow-v2-name">'+esc(l.label)+'</div><div class="lrow-v2-meta"><i class="ti ti-database" style="font-size:10px"></i> '+fmtB(l.used_bytes)+'</div></div><span class="lrow-v2-status '+(on?'on':'off')+'">'+(on?'فعال':'غیرفعال')+'</span></div>';
  }).join('');
  updateLmodalCount();
}
function toggleLrow(uuid,el){
  if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid);el.classList.remove('checked')}
  else{lmodalInSub.add(uuid);el.classList.add('checked')}
  updateLmodalCount();
}
function lmodalSelectAll(state){
  lmodalLinks.forEach(function(l){if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid);});
  renderLmodalList(lmodalLinks);
}
function updateLmodalCount(){
  var el=document.getElementById('lmodal-count');
  if(el)el.textContent=lmodalInSub.size+' انتخاب شده';
}
function filterLmodal(q){
  q=q.trim().toLowerCase();
  document.querySelectorAll('#modal-links-body .lrow-v2').forEach(function(row){
    row.style.display = !q || row.dataset.name.includes(q) ? '' : 'none';
  });
}
async function saveSubLinks(){
  if(!currentSubId)return;
  var link_ids=Array.from(lmodalInSub);
  try{
    var r=await authF('/api/subs/'+currentSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids:link_ids})});
    if(!r.ok)throw new Error();
    await Promise.all(lmodalLinks.map(function(l){
      return authF('/api/links/'+l.uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({sub_id:lmodalInSub.has(l.uuid)?currentSubId:null})});
    }));
    closeModal('modal-links');
    toast('کانفیگ‌های گروه ذخیره شد','ok');
    loadSubs();loadLinks();
  }catch(e){toast('خطا در ذخیره‌سازی','err')}
}
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  try{
    var r=await authF('/api/subs'),d=await r.json();
    var subs=d.subs||[];
    var el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>هنوز گروهی وجود ندارد</p></div>';return}
    el.innerHTML=subs.map(function(s){
      return '<div style="padding:15px 17px;background:var(--accent-d);border:1px solid var(--card-b);border-radius:16px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap"><div><div style="font-weight:700;font-size:13.5px;margin-bottom:3px">'+esc(s.name)+'</div><div style="font-family:\'SF Mono\',\'Fira Code\',ui-monospace,monospace;font-size:10.5px;color:var(--purple);direction:ltr;text-align:left">'+esc(s.sub_url)+'</div><div style="font-size:10px;color:var(--t3);margin-top:3px">'+s.links_count+' کانفیگ &middot; '+esc(s.total_used_fmt)+' مصرف'+(s.has_password?' &middot; &#128274; رمز عبور':'' )+'</div></div><div style="display:flex;gap:6px;flex-wrap:wrap"><button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText(\''+esc(s.sub_url)+'\').then(function(){toast(\'کپی شد\',\'ok\');})"><i class="ti ti-copy"></i> اشتراک</button><button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText(\''+esc(s.public_url)+'\').then(function(){toast(\'کپی شد\',\'ok\');})"><i class="ti ti-globe"></i> عمومی</button><button class="btn btn-sm btn-g" onclick="showQR(\''+esc(s.sub_url)+'\')"><i class="ti ti-qrcode"></i></button></div></div>';
    }).join('');
  }catch(e){}
}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(function(){toast('کپی شد','ok');})}
function parseBytesFmt(s){
  if(!s)return 0;
  var m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);
  if(!m)return 0;
  var n=parseFloat(m[1]),u=m[2].toUpperCase();
  var mult={B:1,KB:1024,MB:1048576,GB:1073741824,TB:1099511627776};
  return n*(mult[u]||1);
}
async function loadConns(){
  try{
    var r=await authF('/api/connections'),d=await r.json();
    var grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.count+' اتصال';
    document.getElementById('ch-count').textContent=d.count;
    var conns=d.connections||[];
    if(!d.count){
      grid.innerHTML='';ce.style.display='block';
      document.getElementById('ch-traffic').textContent='—';
      document.getElementById('ch-avgdur').textContent='—';
      document.getElementById('ch-uniq').textContent='—';
      return;
    }
    ce.style.display='none';
    var totalBytes=conns.reduce(function(s,c){return s+parseBytesFmt(c.bytes_fmt);},0);
    document.getElementById('ch-traffic').textContent=fmtB(totalBytes);
    var uniqIps=new Set(conns.map(function(c){return c.ip;})).size;
    document.getElementById('ch-uniq').textContent=uniqIps;
    var durs=conns.map(function(c){return c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;});
    var avgSec=durs.length?Math.floor(durs.reduce(function(a,b){return a+b;},0)/durs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ثانیه':avgSec<3600?Math.floor(avgSec/60)+' دقیقه':Math.floor(avgSec/3600)+' ساعت';
    var maxDur=Math.max.apply(null,durs.concat([1]));
    grid.innerHTML=conns.map(function(c){
      var secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      var dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';
      var durPct=Math.min(100,Math.round((secs/maxDur)*100));
      var protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');
      return '<div class="conn-card-v2"><div class="conn-card-v2-glow"></div><div class="conn-card-v2-top"><div class="conn-avatar"><i class="ti ti-device-desktop"></i></div><div class="conn-card-v2-id"><div class="conn-ip-v2">'+esc(c.ip)+'<button class="conn-ip-copy" onclick="navigator.clipboard.writeText(\''+esc(c.ip)+'\').then(function(){toast(\'IP کپی شد\',\'ok\');})" title="کپی IP"><i class="ti ti-copy"></i></button></div><div class="conn-label-v2">'+esc(c.label)+'</div></div><span class="conn-status-pill"><span class="dot dg pulse"></span> زنده</span></div><div class="conn-card-v2-divider"></div><div class="conn-card-v2-body"><div class="conn-proto-row">'+protoBadge(protoVal)+'</div><div class="conn-stat-row"><div class="conn-stat-box"><div class="conn-stat-icon"><i class="ti ti-transfer"></i></div><div><div class="conn-stat-text-label">ترافیک</div><div class="conn-stat-text-val">'+esc(c.bytes_fmt)+'</div></div></div><div class="conn-stat-box"><div class="conn-stat-icon time"><i class="ti ti-clock"></i></div><div><div class="conn-stat-text-label">مدت زمان</div><div class="conn-stat-text-val">'+dur+'</div></div></div></div><div class="conn-duration-track"><div class="conn-duration-fill" style="width:'+durPct+'%"></div></div></div></div>';
    }).join('');
  }catch(e){console.error(e)}
}
async function loadErrs(){try{var r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}
async function fetchDefaultVless(){
  try{var r=await authF('/api/links'),d=await r.json();var links=d.links||[];var def=links.find(function(l){return l.limit_bytes===0&&l.active&&!l.expired;})||links.find(function(l){return l.active&&!l.expired;})||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'هنوز کانفیگی وجود ندارد';}catch(e){}
}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(function(){toast('کپی شد','ok');})}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('بروزرسانی شد','ok')}
async function changePw(){
  var cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;
  if(!cur||!nw||!cf){toast('تمام فیلدها را پر کنید','err');return}
  if(nw.length<4){toast('حداقل ۴ کاراکتر','err');return}
  if(nw!==cf){toast('رمز عبور مطابقت ندارد','err');return}
  try{
    var r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});
    var d=await r.json().catch(function(){return{};});
    if(!r.ok)throw new Error(d.detail||'خطا');
    toast('رمز عبور تغییر کرد','ok');
    ['cp-cur','cp-new','cp-cf'].forEach(function(id){document.getElementById(id).value='';});
  }catch(e){toast('✗ '+e.message,'err')}
}
function togglePwField(id,btn){
  var inp=document.getElementById(id);
  var icon=btn.querySelector('i');
  var toText=inp.type==='password';
  inp.type=toText?'text':'password';
  icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}
function checkPwStrength(val){
  var segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');
  var label=document.getElementById('pw-strength-label');
  var reqLen=document.getElementById('req-len'),reqNum=document.getElementById('req-num'),reqCase=document.getElementById('req-case');
  var hasLen=val.length>=4,hasNum=/\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;
  reqLen.classList.toggle('met',hasLen);
  reqNum.classList.toggle('met',hasNum);
  reqCase.classList.toggle('met',hasCase);
  var score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;
  var colors=['#FF4757','#FDCB6E','#2B66FF','#00B894'],labels=['بسیار ضعیف','ضعیف','متوسط','قوی'];
  segs.forEach(function(s,i){s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,116,139,.2)';});
  if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> قدرت رمز عبور';return}
  label.innerHTML='<i class="ti ti-shield-check" style="color:'+colors[Math.max(0,score-1)]+'"></i> '+labels[Math.max(0,score-1)];
}
function makeGradient(ctx,color1,color2){
  var g=ctx.createLinearGradient(0,0,0,260);
  g.addColorStop(0,color1);g.addColorStop(1,color2);
  return g;
}
function initCharts(){
  var c1ctx=document.getElementById('ch1').getContext('2d');
  var grad1=makeGradient(c1ctx,'rgba(43,102,255,.35)','rgba(43,102,255,0)');
  var opts={
    responsive:true,maintainAspectRatio:false,
    interaction:{mode:'index',intersect:false},
    plugins:{
      legend:{display:false},
      tooltip:{
        backgroundColor:'rgba(13,17,23,.97)',borderColor:'rgba(43,102,255,.3)',borderWidth:1,
        titleColor:'#E6EDF3',bodyColor:'#8B949E',padding:12,cornerRadius:12,displayColors:false,
        titleFont:{family:'Vazirmatn',size:11,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
        callbacks:{label:function(v){return v.parsed.y.toFixed(2)+' MB';}}
      }
    },
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:'#484F58',font:{size:9,family:'Vazirmatn'}}},
      y:{grid:{color:'rgba(255,255,255,.04)'},border:{display:false},ticks:{color:'#484F58',font:{size:9,family:'Vazirmatn'},callback:function(v){return v+' MB';}}}
    },
    elements:{line:{capBezierPoints:true}}
  };
  var ds1={label:'MB',data:[],borderColor:'#2B66FF',backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:'#2B66FF',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5};
  ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[ds1]},options:opts});

  function makeGradientV2(ctx,c1,c2,c3){
    var g=ctx.createLinearGradient(0,0,0,340);
    g.addColorStop(0,c1);g.addColorStop(.6,c2);g.addColorStop(1,c3);
    return g;
  }
  var c3ctx=document.getElementById('ch3').getContext('2d');
  var gradFill3=makeGradientV2(c3ctx,'rgba(43,102,255,.4)','rgba(43,102,255,.06)','rgba(43,102,255,0)');
  ch3=new Chart(document.getElementById('ch3'),{
    type:'line',
    data:{labels:[],datasets:[
      {label:'مصرف',data:[],borderColor:'#2B66FF',backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#2B66FF',pointHoverBorderWidth:3,borderWidth:3,order:2},
      {label:'میانگین',data:[],borderColor:'#FDCB6E',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}
    ]},
    options:{
      responsive:true,maintainAspectRatio:false,
      interaction:{mode:'index',intersect:false},
      plugins:{
        legend:{display:false},
        tooltip:{
          backgroundColor:'rgba(13,17,23,.97)',borderColor:'rgba(43,102,255,.35)',borderWidth:1,
          titleColor:'#E6EDF3',bodyColor:'#8B949E',padding:14,cornerRadius:12,displayColors:true,boxPadding:4,
          titleFont:{family:'Vazirmatn',size:12,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
          callbacks:{label:function(v){return ' '+v.dataset.label+': '+v.parsed.y.toFixed(2)+' MB';}}
        }
      },
      scales:{
        x:{grid:{display:false},border:{display:false},ticks:{color:'#484F58',font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},
        y:{grid:{color:'rgba(255,255,255,.04)'},border:{display:false},ticks:{color:'#484F58',font:{size:9.5,family:'Vazirmatn'},callback:function(v){return v+' MB';}}}
      }
    }
  });

  var cardBg='rgba(22,27,34,0.8)';
  ch2=new Chart(document.getElementById('ch2'),{
    type:'doughnut',
    data:{labels:['VLESS/WS','XHTTP Ultra','HTTP Proxy'],datasets:[{
      data:[55,35,10],
      backgroundColor:['#2B66FF','#00B894','#6C5CE7'],
      borderColor:cardBg,
      borderWidth:4,hoverOffset:12,borderRadius:7,spacing:4
    }]},
    options:{
      responsive:true,maintainAspectRatio:false,cutout:'70%',
      plugins:{
        legend:{position:'bottom',labels:{color:var(--t2)',font:{size:10,family:'Vazirmatn'},padding:14,usePointStyle:true,pointStyle:'circle'}},
        tooltip:{backgroundColor:'rgba(13,17,23,.97)',borderColor:'rgba(43,102,255,.3)',borderWidth:1,padding:11,cornerRadius:11,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}
      }
    }
  });
}
var ws;
function wsLog(c,m){var l=document.getElementById('ws-log'),p=document.createElement('p');var colors={ok:'#4ADE80',err:'#FCA5A5',info:'#94A3B8',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('en-US')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){var u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','err');return}var url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','در حال اتصال: '+url);ws=new WebSocket(url);ws.onopen=function(){wsLog('ok','✓ متصل شد - UUID معتبر');};ws.onerror=function(){wsLog('err','✗ خطا - UUID نامعتبر یا غیرفعال');};ws.onmessage=function(m){wsLog('info','دریافت '+ (m.data.size||m.data.length)+' بایت');};ws.onclose=function(e){wsLog('err','قطع شد ('+e.code+')'+(e.code===1008?' - دسترسی ممنوع':''));}}
function wsSend(){var m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}
document.addEventListener('DOMContentLoaded',async function(){
  await checkAuth();
  initCharts();
  document.getElementById('set-host').textContent=location.host;
  if(document.getElementById('sub-all-url'))document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  fetchStats();fetchDefaultVless();loadLinks();loadSubs();
  setInterval(fetchStats,4000);
  setInterval(function(){
    if(document.getElementById('pg-links').classList.contains('on'))loadLinks();
    if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();
    if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();
    if(document.getElementById('pg-connections').classList.contains('on'))loadConns();
    if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();
  },5000);
});
</script>
</body></html>"""


def get_public_page_html(uuid_key: str) -> str:
    """Public sub page — SPIDER PANEL RTL Persian"""
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>SPIDER PANEL · اشتراک</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{
  --bg:#F8F9FA;--bg2:#F1F5F9;--bg3:#E2E8F0;
  --card:rgba(255,255,255,0.85);--card-b:rgba(0,0,0,0.06);--card-bh:rgba(43,102,255,0.18);
  --accent:#2B66FF;--accent2:#6C5CE7;--accent-d:rgba(43,102,255,0.06);
  --green:#00B894;--green-bg:rgba(0,184,148,0.08);--green-t:#00856A;
  --red:#FF4757;--red-bg:rgba(255,71,87,0.08);--red-t:#D63031;
  --amber:#FDCB6E;--amber-bg:rgba(253,203,110,0.12);--amber-t:#B8860B;
  --purple:#6C5CE7;--purple-bg:rgba(108,92,231,0.08);--purple-t:#5B21B6;
  --t1:#1E272E;--t2:#636E72;--t3:#B2BEC3;
  --radius:24px;--shadow:0 4px 30px rgba(0,0,0,0.06);
  --font:'Vazirmatn',sans-serif;
  --gradient:linear-gradient(135deg,#2B66FF,#FF3B65);
}}
[data-theme="dark"]{{
  --bg:#0D1117;--bg2:#161B22;--bg3:#21262D;
  --card:rgba(22,27,34,0.8);--card-b:rgba(255,255,255,0.06);--card-bh:rgba(255,255,255,0.14);
  --accent:#2B66FF;--accent2:#A29BFE;
  --green:#00B894;--green-bg:rgba(0,184,148,0.1);--green-t:#00B894;
  --red:#FF4757;--red-bg:rgba(255,71,87,0.1);--red-t:#FF4757;
  --amber:#FDCB6E;--amber-bg:rgba(253,203,110,0.1);--amber-t:#FDCB6E;
  --purple:#6C5CE7;--purple-bg:rgba(108,92,231,0.1);--purple-t:#A29BFE;
  --t1:#E6EDF3;--t2:#8B949E;--t3:#484F58;
  --shadow:0 4px 30px rgba(0,0,0,0.3);
}}
html,body{{min-height:100%;background:var(--bg);font-family:var(--font);color:var(--t1);font-size:14px;transition:background .35s,color .35s}}
.bg-layer{{position:fixed;inset:0;z-index:0;pointer-events:none}}
.bg-layer svg{{position:absolute}}
.bg-layer svg.tl{{top:-70px;right:-50px;opacity:.025;width:320px;height:320px}}
.bg-layer svg.br{{bottom:-70px;left:-50px;opacity:.025;width:300px;height:300px}}
.wrap{{position:relative;z-index:10;max-width:880px;margin:0 auto;padding:28px 18px 70px}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:28px;gap:10px}}
.brand{{display:flex;align-items:center;gap:12px;min-width:0}}
.brand-svg{{width:42px;height:42px;flex-shrink:0}}
.brand-name{{font-size:16px;font-weight:800;letter-spacing:-.01em;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.brand-sub{{font-size:10px;color:var(--t3);font-weight:500}}
.top-actions{{display:flex;align-items:center;gap:7px;flex-shrink:0}}
.icon-btn{{width:38px;height:38px;border-radius:13px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:17px;cursor:pointer;transition:.18s;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}}
.icon-btn:hover{{background:var(--accent-d);color:var(--accent);border-color:var(--card-bh)}}
.status-pill{{display:inline-flex;align-items:center;gap:6px;padding:6px 14px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-size:11px;font-weight:700}}
.status-pill i{{font-size:13px}}
.sub-info{{background:var(--card);border:1px solid var(--card-b);border-radius:24px;padding:28px;margin-bottom:18px;position:relative;overflow:hidden;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}}
.sub-name{{font-size:24px;font-weight:800;color:var(--t1);margin-bottom:8px}}
.sub-desc{{font-size:13px;color:var(--t2);line-height:1.8;margin-bottom:16px}}
.sub-detail-table{{width:100%;margin-bottom:20px}}
.sub-detail-row{{display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--card-b);font-size:13px}}
.sub-detail-row:last-child{{border-bottom:none}}
.sub-detail-key{{color:var(--t3);font-weight:500;display:flex;align-items:center;gap:6px}}
.sub-detail-key i{{font-size:14px;color:var(--accent)}}
.sub-detail-val{{color:var(--t1);font-weight:700}}
.sub-detail-val.active{{color:var(--green-t);display:flex;align-items:center;gap:4px}}
/* Usage progress */
.usage-bar-section{{background:rgba(0,0,0,0.03);border-radius:16px;padding:18px 20px;margin-bottom:20px}}
[data-theme="dark"] .usage-bar-section{{background:rgba(255,255,255,0.04)}}
.usage-header{{display:flex;justify-content:space-between;margin-bottom:10px;font-size:12px;color:var(--t2);font-weight:600}}
.usage-bar{{height:10px;border-radius:6px;background:rgba(0,0,0,0.06);overflow:hidden;position:relative}}
[data-theme="dark"] .usage-bar{{background:rgba(255,255,255,0.06)}}
.usage-fill{{height:100%;border-radius:6px;background:linear-gradient(90deg,#2B66FF,#FF3B65);transition:width .6s ease}}
.usage-label{{text-align:center;margin-top:8px;font-size:11px;color:var(--t3)}}
/* Action buttons */
.action-buttons{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px}}
.action-btn{{padding:16px 20px;border-radius:16px;border:none;font-family:inherit;font-size:13px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;transition:.2s;color:#fff}}
.action-btn.config{{background:linear-gradient(135deg,#6C5CE7,#2B66FF);box-shadow:0 4px 16px rgba(108,92,231,0.3)}}
.action-btn.config:hover{{transform:translateY(-2px);box-shadow:0 8px 24px rgba(108,92,231,0.4)}}
.action-btn.sub{{background:linear-gradient(135deg,#FF3B65,#FF6B81);box-shadow:0 4px 16px rgba(255,59,101,0.3)}}
.action-btn.sub:hover{{transform:translateY(-2px);box-shadow:0 8px 24px rgba(255,59,101,0.4)}}
/* QR section */
.qr-section{{text-align:center;padding:24px;background:var(--card);border:1px solid var(--card-b);border-radius:20px;margin-bottom:20px;position:relative;overflow:hidden;backdrop-filter:blur(12px)}}
.qr-center{{position:relative;display:inline-block;padding:16px;background:#fff;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,0.12)}}
.qr-center img{{width:160px;height:160px;display:block}}
.qr-spider{{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);opacity:.12}}
.qr-spider svg{{width:60px;height:60px}}
.qr-instructions{{display:flex;justify-content:center;gap:48px;margin-top:18px;font-size:11px;color:var(--t3)}}
.qr-instructions div{{display:flex;align-items:center;gap:5px;font-weight:600}}
.qr-instructions i{{font-size:14px;color:var(--accent)}}
/* App cards */
.app-rec-section{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:20px}}
.app-card{{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:18px 20px;display:flex;align-items:center;gap:14px;transition:.2s;backdrop-filter:blur(12px)}}
.app-card:hover{{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}}
.app-icon{{width:44px;height:44px;border-radius:14px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0}}
.app-info{{flex:1}}
.app-name{{font-size:13px;font-weight:700;color:var(--t1);margin-bottom:3px}}
.app-desc{{font-size:10.5px;color:var(--t3);line-height:1.5}}
/* Config list */
.cfg-title{{font-size:13px;font-weight:800;color:var(--t2);margin-bottom:14px;display:flex;align-items:center;gap:7px}}
.cfg-title i{{color:var(--accent);font-size:16px}}
.cfg-grid{{display:grid;gap:14px}}
.cfg-card{{background:var(--card);border:1px solid var(--card-b);border-radius:20px;transition:all .25s;position:relative;overflow:hidden;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}}
.cfg-card:hover{{border-color:var(--card-bh);box-shadow:var(--shadow)}}
.cfg-top{{padding:20px 22px 18px;position:relative}}
.cfg-top::after{{content:'';position:absolute;top:0;right:0;width:4px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-top::after{{background:var(--red)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:14px;flex-wrap:wrap}}
.cfg-label{{font-size:15px;font-weight:700;color:var(--t1)}}
.cfg-badges{{display:flex;gap:6px;flex-wrap:wrap;margin-top:7px}}
.proto-chip{{font-size:9.5px;padding:4px 9px;border-radius:8px;font-weight:800}}
.pc-ws{{background:var(--accent-d);color:var(--accent)}}
.pc-xhttp{{background:var(--purple-bg);color:var(--purple-t)}}
.pc-ultra{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status{{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;padding:5px 12px;border-radius:20px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red-t)}}
.cfg-usage{{margin-bottom:4px}}
.ubar{{height:7px;border-radius:5px;background:rgba(0,0,0,0.06);overflow:hidden;margin-bottom:6px}}
[data-theme="dark"] .ubar{{background:rgba(255,255,255,0.06)}}
.ubar-f{{height:100%;border-radius:5px;transition:width .5s ease}}
.utxt{{font-size:10.5px;color:var(--t3);display:flex;justify-content:space-between}}
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 22px}}
.cfg-bottom{{padding:18px 22px 20px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1.5px dashed var(--card-b);border-radius:14px;padding:11px 15px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:12px;font-weight:600;transition:.15s}}
.cfg-link-toggle:hover{{background:var(--accent-d);border-color:var(--card-bh);color:var(--accent)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,0.03);border:1px solid var(--card-b);border-radius:12px;padding:12px 15px;font-size:10px;font-family:'SF Mono','Fira Code',ui-monospace,monospace;color:var(--accent);word-break:break-all;line-height:1.8;margin-top:10px;max-height:100px;overflow-y:auto;direction:ltr;text-align:left}}
[data-theme="dark"] .cfg-vless{{background:rgba(0,0,0,0.2)}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap;margin-top:12px}}
.btn{{font-family:inherit;font-size:12px;font-weight:700;border-radius:14px;padding:9px 17px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border:none;transition:all .18s;white-space:nowrap}}
.btn i{{font-size:14px}}
.btn-p{{background:var(--accent);color:#fff;box-shadow:0 3px 14px rgba(43,102,255,0.3)}}
.btn-p:hover{{box-shadow:0 5px 20px rgba(43,102,255,0.4);transform:translateY(-1px)}}
.btn-g{{background:var(--accent-d);color:var(--accent);border:1px solid rgba(43,102,255,0.12)}}
.btn-g:hover{{background:rgba(43,102,255,0.15)}}
.conn-chip{{display:inline-flex;align-items:center;gap:5px;font-size:9.5px;padding:4px 9px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-weight:700}}
.dot{{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
/* Lock stage */
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:75vh;padding:20px 0}}
.lock-card{{background:var(--card);border:1px solid var(--card-b);border-radius:24px;padding:0;text-align:center;max-width:400px;width:100%;overflow:hidden;position:relative;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}}
.lock-banner{{background:linear-gradient(150deg,rgba(43,102,255,0.06),rgba(108,92,231,0.03) 70%);padding:44px 32px 30px;position:relative}}
.lock-shield{{width:70px;height:70px;border-radius:20px;background:var(--accent-d);border:1px solid var(--card-bh);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-8px;border-radius:24px;border:1px solid var(--card-b);animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.5}}50%{{transform:scale(1.08);opacity:0}}}}
.lock-shield i{{font-size:30px;color:var(--accent)}}
.lock-title{{font-size:19px;font-weight:800;margin-bottom:7px;color:var(--t1)}}
.lock-sub{{font-size:12.5px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:26px 34px 34px}}
.lock-field{{position:relative;margin-bottom:14px}}
.lock-inp{{width:100%;padding:14px 46px;border-radius:16px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.03);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.14em;transition:.18s}}
[data-theme="dark"] .lock-inp{{background:rgba(0,0,0,0.15)}}
.lock-inp:focus{{border-color:var(--accent);box-shadow:0 0 0 4px var(--accent-d)}}
.lock-eye{{position:absolute;left:14px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:17px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--accent)}}
.lock-lockicon{{position:absolute;right:15px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:16px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:12px;margin-bottom:10px;min-height:18px;display:flex;align-items:center;justify-content:center;gap:5px}}
.lock-btn{{width:100%;justify-content:center;padding:14px;font-size:14px;border-radius:16px;background:var(--gradient);color:#fff}}
.lock-footer{{padding:16px 34px;border-top:1px solid var(--card-b);font-size:10.5px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:7px}}
.empty-state{{text-align:center;padding:90px 20px;color:var(--t3)}}
.empty-state i{{font-size:40px;display:block;margin-bottom:16px}}
.toast{{position:fixed;bottom:24px;right:50%;transform:translateX(50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:14px;padding:12px 22px;font-size:13px;font-weight:600;opacity:0;transition:all .3s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap;backdrop-filter:blur(20px)}}
.toast.show{{opacity:1;transform:translateX(50%) translateY(0)}}
.toast.ok{{border-color:rgba(0,184,148,0.3);background:var(--green-bg);color:var(--green-t)}}
.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--card);border:1px solid var(--card-b);border-radius:24px;padding:28px;text-align:center;max-width:360px;width:100%;backdrop-filter:blur(20px)}}
.qr-title{{font-size:14px;font-weight:800;margin-bottom:18px;color:var(--t1)}}
.qr-img{{border-radius:16px;overflow:hidden;margin-bottom:16px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:12px;border-radius:16px}}
.footer{{text-align:center;padding-top:30px;font-size:11px;color:var(--t3)}}
.footer a{{color:var(--accent);font-weight:700;text-decoration:none}}
@media(max-width:520px){{
  .app-rec-section{{grid-template-columns:1fr}}
  .action-buttons{{grid-template-columns:1fr}}
  .sub-name{{font-size:20px}}
  .wrap{{padding:18px 14px 56px}}
  .lock-banner{{padding:36px 24px 24px}}
  .lock-form{{padding:22px 24px 28px}}
  .qr-instructions{{flex-direction:column;align-items:center;gap:12px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
</style>
</head>
<body>
<div class="bg-layer">
  <svg class="tl" viewBox="0 0 400 400" fill="none">
    <line x1="200" y1="0" x2="200" y2="400" stroke="#636E72" stroke-width="0.4"/>
    <line x1="0" y1="200" x2="400" y2="200" stroke="#636E72" stroke-width="0.4"/>
    <line x1="59" y1="0" x2="341" y2="400" stroke="#636E72" stroke-width="0.3"/>
    <line x1="341" y1="0" x2="59" y2="400" stroke="#636E72" stroke-width="0.3"/>
    <circle cx="200" cy="200" r="60" stroke="#636E72" stroke-width="0.4"/>
    <circle cx="200" cy="200" r="140" stroke="#636E72" stroke-width="0.3"/>
    <path d="M140 110L155 165L210 175L155 185L140 240L125 185L70 175L125 165Z" stroke="#636E72" stroke-width="0.5"/>
  </svg>
  <svg class="br" viewBox="0 0 400 400" fill="none">
    <line x1="200" y1="0" x2="200" y2="400" stroke="#636E72" stroke-width="0.4"/>
    <line x1="0" y1="200" x2="400" y2="200" stroke="#636E72" stroke-width="0.4"/>
    <circle cx="200" cy="200" r="80" stroke="#636E72" stroke-width="0.4"/>
    <circle cx="200" cy="200" r="160" stroke="#636E72" stroke-width="0.3"/>
    <path d="M140 110L155 165L210 175L155 185L140 240L125 185L70 175L125 165Z" stroke="#636E72" stroke-width="0.5"/>
  </svg>
</div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <svg class="brand-svg" viewBox="0 0 48 48" fill="none"><circle cx="24" cy="24" r="22" stroke="url(#pubGrad)" stroke-width="1.5"/><defs><linearGradient id="pubGrad" x1="0" y1="0" x2="48" y2="48"><stop stop-color="#2B66FF"/><stop offset="0.5" stop-color="#6C5CE7"/><stop offset="1" stop-color="#FF3B65"/></linearGradient></defs><path d="M24 6L26 22L42 24L26 26L24 42L22 26L6 24L22 22Z" fill="url(#pubGrad)" opacity="0.9"/><circle cx="24" cy="24" r="3.5" fill="url(#pubGrad)"/></svg>
      <div><div class="brand-name">SPIDER PANEL</div><div class="brand-sub">مدیریت شبکه سازمانی</div></div>
    </div>
    <div class="top-actions">
      <button class="icon-btn" id="theme-toggle" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-moon" id="theme-icon"></i></button>
      <a class="icon-btn" href="https://t.me/CodeBoxo" target="_blank" title="تلگرام"><i class="ti ti-brand-telegram"></i></a>
    </div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
  </div>
  <div class="footer">SPIDER PANEL · <a href="https://t.me/CodeBoxo" target="_blank">@CodeBoxo</a></div>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';
let isDark=localStorage.getItem('sp-pub-theme')==='dark';
function applyTheme(dark){{
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  document.getElementById('theme-icon').className='ti '+(dark?'ti-sun':'ti-moon');
}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('sp-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);
function toast(msg,type){{
  type=type||'';
  var t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(function(){{t.classList.remove('show');}},2400);
}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c];}})}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1048576)return (b/1024).toFixed(1)+' KB';if(b<1073741824)return (b/1048576).toFixed(2)+' MB';return (b/1073741824).toFixed(2)+' GB'}}
function protoChip(p){{
  if(p==='xhttp-stream-one')return '<span class="proto-chip pc-ultra"><i class="ti ti-bolt"></i> XHTTP ULTRA</span>';
  if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp">'+esc(p)+'</span>';
  return '<span class="proto-chip pc-ws">VLESS · WS</span>';
}}
function showQR(label,link){{
  document.getElementById('qr-label').textContent=label;
  document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);
  document.getElementById('qr-modal').classList.add('open');
}}
function toggleLink(i){{
  var wrap=document.getElementById('vw-'+i);
  var btn=document.getElementById('vt-'+i);
  var open=wrap.classList.toggle('open');
  btn.classList.toggle('open',open);
  btn.querySelector('.ltl span').textContent = open ? 'پنهان کردن لینک' : 'نمایش لینک';
}}
async function loadData(pw){{
  pw=pw||'';
  var url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');
  var r=await fetch(url);
  return r.json();
}}
function renderLock(name,errMsg){{
  errMsg=errMsg||'';
  document.getElementById('root').innerHTML=
    '<div class="lock-stage"><div class="lock-card"><div class="lock-banner"><div class="lock-shield"><i class="ti ti-shield-lock"></i></div><div class="lock-title">'+esc(name)+'</div><div class="lock-sub">این گروه با رمز عبور محافظت می‌شود. برای مشاهده کانفیگ‌ها رمز عبور را وارد کنید.</div></div><div class="lock-form"><div class="lock-err" id="lock-err">'+(errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : '')+'</div><div class="lock-field"><i class="ti ti-lock lock-lockicon"></i><input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus><button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button></div><button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> باز کردن قفل گروه</button></div><div class="lock-footer"><i class="ti ti-shield-check"></i> ارتباط رمزنگاری شده است</div></div></div>';
  var inp=document.getElementById('lock-pw');
  inp.addEventListener('keydown',function(e){{if(e.key==='Enter')submitLock();}});
}}
function togglePwVis(){{
  var inp=document.getElementById('lock-pw');
  var icon=document.getElementById('lock-eye-icon');
  var toText = inp.type==='password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti '+(toText ? 'ti-eye-off' : 'ti-eye');
}}
async function submitLock(){{
  var pw=document.getElementById('lock-pw').value;
  var data=await loadData(pw);
  if(data.locked){{renderLock(data.name,'رمز عبور اشتباه است');return}}
  savedPw=pw;
  renderContent(data);
}}
function renderContent(d){{
  var activeCount=d.links.filter(function(l){{return l.active;}}).length;
  var baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/sub-group/' + UUID_KEY);
  var subUrl = baseSubUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');
  window._rvgSubUrl  = subUrl;
  window._rvgSubName = d.name;
  window._rvgLinks   = d.links.map(function(l) {{ return {{vless:l.vless_link,sub:l.sub_url + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : ''),label:l.label}}; }});
  // Calculate total GB used across all configs
  var totalUsedGb = 0;
  d.links.forEach(function(l){{ totalUsedGb += l.used_bytes; }});
  totalUsedGb = (totalUsedGb / 1073741824).toFixed(2);
  document.getElementById('root').innerHTML=
    '<div class="sub-info"><span class="status-pill"><i class="ti ti-circle-check"></i> اشتراک شما فعال است</span><div class="sub-name" style="margin-top:14px">'+esc(d.name)+'</div>'+
    (d.desc ? '<div class="sub-desc">'+esc(d.desc)+'</div>' : '')+
    '<div class="sub-detail-table"><div class="sub-detail-row"><span class="sub-detail-key"><i class="ti ti-user"></i> نام کاربری</span><span class="sub-detail-val">'+esc(d.name)+'</span></div><div class="sub-detail-row"><span class="sub-detail-key"><i class="ti ti-database"></i> حجم کل</span><span class="sub-detail-val">'+esc(d.total_used_fmt)+'</span></div><div class="sub-detail-row"><span class="sub-detail-key"><i class="ti ti-clock"></i> زمان باقی‌مانده</span><span class="sub-detail-val">نامحدود</span></div><div class="sub-detail-row"><span class="sub-detail-key"><i class="ti ti-shield-check"></i> وضعیت</span><span class="sub-detail-val active"><i class="ti ti-circle-check"></i> فعال</span></div></div>'+
    '<div class="usage-bar-section"><div class="usage-header"><span>مصرف داده</span><span>'+totalUsedGb+' GB از ۲۰ GB</span></div><div class="usage-bar"><div class="usage-fill" style="width:62%"></div></div><div class="usage-label">۶۲٪ مصرف شده</div></div></div>'+
    '<div class="action-buttons"><button class="action-btn config" onclick="navigator.clipboard.writeText(window._rvgLinks.length?window._rvgLinks[0].vless:\'\').then(function(){{toast(\'کانفیگ کپی شد\',\'ok\');}})"><i class="ti ti-copy"></i> کپی کانفیگ</button><button class="action-btn sub" onclick="navigator.clipboard.writeText(window._rvgSubUrl).then(function(){{toast(\'لینک اشتراک کپی شد\',\'ok\');}})"><i class="ti ti-link"></i> کپی لینک اشتراک</button></div>'+
    '<div class="qr-section"><div class="qr-center"><img src="https://api.qrserver.com/v1/create-qr-code/?size=160x160&data='+encodeURIComponent(window._rvgSubUrl)+'" alt="QR"><div class="qr-spider"><svg viewBox="0 0 60 60" fill="none"><path d="M30 6L31 24L48 25L31 26L30 44L29 26L12 25L29 24Z" fill="rgba(43,102,255,0.6)"/><circle cx="30" cy="26" r="4" fill="rgba(255,59,101,0.6)"/></svg></div></div><div class="qr-instructions"><div><i class="ti ti-camera"></i> اسکن با دوربین</div><div><i class="ti ti-copy"></i> وارد کردن دستی</div></div></div>'+
    '<div class="app-rec-section"><div class="app-card"><div class="app-icon"><i class="ti ti-download"></i></div><div class="app-info"><div class="app-name">Hiddify Next</div><div class="app-desc">اپلیکیشن پیشنهادی برای اندروید و iOS</div></div></div><div class="app-card"><div class="app-icon"><i class="ti ti-apps"></i></div><div class="app-info"><div class="app-name">v2rayNG</div><div class="app-desc">کلاینت محبوب برای اندروید</div></div></div></div>'+
    '<div class="cfg-title"><i class="ti ti-link"></i> کانفیگ‌ها ('+d.links.length+' مورد)</div>'+
    '<div class="cfg-grid">'+
    d.links.map(function(l, i) {{
      var pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
      var bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
      var lim = l.limit_bytes === 0 ? '&infin;' : fmtB(l.limit_bytes);
      return '<div class="cfg-card'+(l.active ? '' : ' inactive')+'"><div class="cfg-top"><div class="cfg-head"><div><div class="cfg-label">'+esc(l.label)+'</div><div class="cfg-badges">'+protoChip(l.protocol)+
        (l.connections > 0 ? '<span class="conn-chip"><span class="dot"></span> '+l.connections+' اتصال</span>' : '')+
        '</div></div><span class="cfg-status '+(l.active ? 'ok' : 'no')+'">'+(l.active ? '<i class="ti ti-circle-check"></i> فعال' : '<i class="ti ti-circle-x"></i> غیرفعال')+'</span></div>'+
        '<div class="cfg-usage"><div class="ubar"><div class="ubar-f" style="width:'+pct+'%;background:'+bc+'"></div></div><div class="utxt"><span>'+esc(l.used_fmt)+' مصرف شده</span><span>سهمیه: '+lim+'</span></div></div></div>'+
        '<div class="cfg-tear"></div><div class="cfg-bottom"><button class="cfg-link-toggle" id="vt-'+i+'" onclick="toggleLink('+i+')"><span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک</span></span><i class="ti ti-chevron-down"></i></button>'+
        '<div class="cfg-vless-wrap" id="vw-'+i+'"><div class="cfg-vless-inner"><div class="cfg-vless">'+esc(l.vless_link)+'</div></div></div>'+
        '<div class="cfg-actions"><button class="btn btn-p" onclick="navigator.clipboard.writeText(window._rvgLinks['+i+'].vless).then(function(){{toast(\'لینک کپی شد\',\'ok\');}})"><i class="ti ti-copy"></i> کپی لینک</button>'+
        '<button class="btn btn-g" onclick="showQR(window._rvgLinks['+i+'].label, window._rvgLinks['+i+'].vless)"><i class="ti ti-qrcode"></i> QR</button></div></div></div>';
    }}).join('')+'</div>';
  setTimeout(function() {{ autoRefresh(); }}, 30000);
}}
function copyAllConfigs(){{
  var links=window._rvgLinks||[];
  if(!links.length){{toast('کانفیگی برای کپی وجود ندارد','');return}}
  var text=links.map(function(l){{return l.vless;}}).join('\\n');
  navigator.clipboard.writeText(text).then(function(){{toast('تمام '+links.length+' کانفیگ کپی شد','ok');}});
}}
async function autoRefresh(){{
  try{{
    var data = await loadData(savedPw);
    if (!data.locked) renderContent(data);
  }} catch(e) {{}}
}}
async function init(){{
  try{{
    var data = await loadData();
    if (data.locked) {{ renderLock(data.name); return; }}
    renderContent(data);
  }} catch(e) {{
    document.getElementById('root').innerHTML = '<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری اطلاعات</div>';
  }}
}}
init();
</script>
</body></html>"""
