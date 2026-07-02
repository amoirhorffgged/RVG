# pages.py  -  SPIDER PANEL Enterprise v1.0
# Contains: LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login · SPIDER PANEL</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Vazirmatn:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#060f1d;--card:rgba(10,22,40,0.85);--accent:#2B7FFF;--accent2:#7B61FF;--text:#F1F5F9;--dim:#64748B;--mid:#94A3B8;--border:rgba(43,127,255,0.15);--radius:24px}
[data-theme="light"]{--bg:#F8FAFC;--card:rgba(255,255,255,0.8);--text:#0F172A;--dim:#64748B;--mid:#475569;--border:rgba(43,127,255,0.12)}
html,body{height:100%;overflow:hidden}
body{font-family:'Inter',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px;transition:background .4s}
.bg-layer{position:fixed;inset:0;z-index:0}
.bg-blobs{position:absolute;inset:0;overflow:hidden}
.blob{position:absolute;border-radius:50%;filter:blur(120px);animation:blobFloat 12s ease-in-out infinite}
.blob1{width:500px;height:500px;background:rgba(43,127,255,0.15);top:-120px;left:-100px}
.blob2{width:400px;height:400px;background:rgba(123,97,255,0.12);bottom:-100px;right:-80px;animation-delay:4s}
.blob3{width:350px;height:350px;background:rgba(255,35,82,0.08);top:40%;right:-60px;animation-delay:8s}
@keyframes blobFloat{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(40px,-30px) scale(1.05)}66%{transform:translate(-20px,20px) scale(0.95)}}
.spider-web{position:absolute;inset:0;opacity:.04;pointer-events:none}
.spider-web svg{width:100%;height:100%}
.particles{position:absolute;inset:0;pointer-events:none}
.particle{position:absolute;width:2px;height:2px;background:rgba(43,127,255,0.5);border-radius:50%;animation:particleFloat 8s ease-in-out infinite}
@keyframes particleFloat{0%,100%{transform:translateY(0);opacity:0}20%{opacity:1}50%{transform:translateY(-40px)}80%{opacity:0}}
.wrap{position:relative;z-index:10;width:100%;max-width:440px}
.card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:42px 38px 38px;backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);box-shadow:0 8px 40px rgba(0,0,0,0.15),0 0 0 1px rgba(255,255,255,0.05);transition:all .3s}
.card:hover{box-shadow:0 12px 48px rgba(0,0,0,0.2),0 0 0 1px rgba(255,255,255,0.08)}
.spider-logo{display:flex;align-items:center;justify-content:center;margin-bottom:8px}
.spider-svg{width:52px;height:52px}
.brand-row{text-align:center;margin-bottom:6px}
.brand-name{font-size:26px;font-weight:800;letter-spacing:-.02em;background:linear-gradient(90deg,#2B7FFF,#7B61FF,#FF2352);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.brand-tagline{font-size:11px;color:var(--dim);font-weight:500;margin-top:2px;letter-spacing:.03em}
.separator{width:40px;height:3px;background:linear-gradient(90deg,#2B7FFF,#7B61FF);border-radius:3px;margin:20px auto}
.welcome{font-size:18px;font-weight:700;color:var(--text);margin-bottom:5px;letter-spacing:-.01em}
.subtitle{font-size:12.5px;color:var(--mid);margin-bottom:24px;line-height:1.6}
.hint-box{display:flex;align-items:center;gap:10px;background:rgba(43,127,255,0.06);border:1px solid rgba(43,127,255,0.12);border-radius:14px;padding:10px 14px;margin-bottom:20px}
.hint-label{font-size:11px;color:var(--dim);flex:1}
.hint-val{font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:14px;font-weight:700;color:var(--accent);background:rgba(43,127,255,0.1);border:1px solid rgba(43,127,255,0.2);padding:4px 12px;border-radius:8px;cursor:pointer;transition:.15s;letter-spacing:.05em}
.hint-val:hover{background:rgba(43,127,255,0.2)}
.field{margin-bottom:18px}
.field label{display:block;font-size:10.5px;font-weight:600;color:var(--dim);margin-bottom:7px;text-transform:uppercase;letter-spacing:.08em}
.inp-wrap{position:relative}
input[type=password]{width:100%;padding:14px 46px 14px 16px;border-radius:18px;border:1.5px solid var(--border);background:rgba(0,0,0,0.2);color:var(--text);font-family:inherit;font-size:14px;outline:none;transition:.2s}
[data-theme="light"] input[type=password]{background:rgba(43,127,255,0.03)}
input[type=password]:focus{border-color:rgba(43,127,255,0.5);background:rgba(0,0,0,0.25);box-shadow:0 0 0 4px rgba(43,127,255,0.08)}
input[type=password]::placeholder{color:var(--dim)}
.ic{position:absolute;right:16px;top:50%;transform:translateY(-50%);color:var(--dim);font-size:18px;pointer-events:none;transition:.2s}
input:focus+.ic{color:var(--accent)}
.err{display:none;background:rgba(220,38,38,0.08);border:1px solid rgba(220,38,38,0.2);border-radius:14px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:#EF4444;align-items:center;gap:8px}
.err.show{display:flex}
.btn{width:100%;padding:14px;border-radius:18px;border:none;cursor:pointer;background:linear-gradient(135deg,#2B7FFF,#7B61FF);color:#fff;font-family:inherit;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 4px 24px rgba(43,127,255,0.35);transition:.25s;position:relative;overflow:hidden}
.btn::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(255,255,255,0.1),transparent);opacity:0;transition:.25s}
.btn:hover{box-shadow:0 6px 32px rgba(43,127,255,0.5);transform:translateY(-1px)}
.btn:hover::before{opacity:1}
.btn:active{transform:translateY(0) scale(.98)}
.btn:disabled{opacity:.5;cursor:not-allowed;transform:none}
.theme-switch{position:absolute;top:16px;right:16px;background:rgba(43,127,255,0.08);border:1px solid var(--border);color:var(--dim);width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:20;transition:.15s;font-size:16px}
.theme-switch:hover{background:rgba(43,127,255,0.15);color:var(--accent)}
.footer{margin-top:22px;padding-top:18px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11px;color:var(--dim)}
.footer a{color:var(--accent);font-weight:600;text-decoration:none;display:flex;align-items:center;gap:4px;transition:.15s}
.footer a:hover{color:var(--accent2)}
@keyframes spin{to{transform:rotate(360deg)}}
@media(max-width:480px){.card{padding:32px 24px 28px;border-radius:20px}.brand-name{font-size:22px}}
</style>
</head>
<body>
<div class="bg-layer">
  <div class="bg-blobs"><div class="blob blob1"></div><div class="blob blob2"></div><div class="blob blob3"></div></div>
  <div class="spider-web"><svg viewBox="0 0 800 600" fill="none"><path d="M400 0L420 300L800 320L420 340L400 600L380 340L0 320L380 300Z" stroke="rgba(43,127,255,0.15)" stroke-width="0.5"/><circle cx="400" cy="300" r="100" stroke="rgba(43,127,255,0.08)" stroke-width="0.3"/><circle cx="400" cy="300" r="200" stroke="rgba(123,97,255,0.06)" stroke-width="0.3"/><circle cx="400" cy="300" r="300" stroke="rgba(255,35,82,0.04)" stroke-width="0.3"/><line x1="400" y1="0" x2="400" y2="600" stroke="rgba(43,127,255,0.06)" stroke-width="0.3"/><line x1="0" y1="300" x2="800" y2="300" stroke="rgba(43,127,255,0.06)" stroke-width="0.3"/><line x1="152" y1="48" x2="648" y2="552" stroke="rgba(123,97,255,0.04)" stroke-width="0.3"/><line x1="648" y1="48" x2="152" y2="552" stroke="rgba(123,97,255,0.04)" stroke-width="0.3"/><path d="M350 200L365 250L420 260L365 270L350 320L335 270L280 260L335 250Z" stroke="rgba(43,127,255,0.2)" stroke-width="0.5"/></svg></div>
  <div class="particles" id="particles"></div>
</div>
<button class="theme-switch" id="theme-btn" onclick="toggleTheme()" title="Toggle theme"><i class="ti ti-sun" id="theme-icon"></i></button>
<div class="wrap">
  <div class="card">
    <div class="spider-logo">
      <svg class="spider-svg" viewBox="0 0 64 64" fill="none">
        <circle cx="32" cy="32" r="30" stroke="url(#spiderGrad)" stroke-width="1.5"/>
        <defs><linearGradient id="spiderGrad" x1="0" y1="0" x2="64" y2="64"><stop stop-color="#2B7FFF"/><stop offset="0.5" stop-color="#7B61FF"/><stop offset="1" stop-color="#FF2352"/></linearGradient></defs>
        <path d="M32 8L34 28L54 30L34 32L32 56L30 32L10 30L30 28Z" fill="url(#spiderGrad)" opacity="0.9"/>
        <circle cx="32" cy="32" r="4" fill="url(#spiderGrad)"/>
        <path d="M22 18L28 26" stroke="url(#spiderGrad)" stroke-width="1.5"/>
        <path d="M42 18L36 26" stroke="url(#spiderGrad)" stroke-width="1.5"/>
        <path d="M22 46L28 38" stroke="url(#spiderGrad)" stroke-width="1.5"/>
        <path d="M42 46L36 38" stroke="url(#spiderGrad)" stroke-width="1.5"/>
      </svg>
    </div>
    <div class="brand-row"><div class="brand-name">SPIDER PANEL</div><div class="brand-tagline">Enterprise Network Management</div></div>
    <div class="separator"></div>
    <h1 class="welcome">Welcome to Spider Panel</h1>
    <p class="subtitle">Enter your password to access the dashboard</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="hint">
      <span class="hint-label">Default password</span>
      <span class="hint-val" onclick="document.getElementById('pw').value='123456';document.getElementById('pw').focus()">123456</span>
    </div>
    <form id="form">
      <div class="field">
        <label>Password</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="Enter your password" autofocus required>
          <i class="ti ti-lock ic"></i>
        </div>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> Sign In</button>
    </form>
    <div class="footer"><a href="https://t.me/CodeBoxo" target="_blank"><i class="ti ti-brand-telegram"></i>@CodeBoxo</a></div>
  </div>
</div>
<script>
(function(){var p=document.getElementById('particles');var h='';for(var i=0;i<30;i++){var l=Math.random()*100;var t=Math.random()*100;var d=Math.random()*8+4;var s=Math.random()*2+1;h+='<div class="particle" style="left:'+l+'%;top:'+t+'%;animation-delay:'+d+'s;width:'+s+'px;height:'+s+'px"></div>';}p.innerHTML=h;})();
var isDark=localStorage.getItem('sp-theme')!=='light';
function applyTheme(dark){document.documentElement.setAttribute('data-theme',dark?'dark':'light');var icon=document.getElementById('theme-icon'),btn=document.getElementById('theme-btn');icon.className='ti '+(dark?'ti-sun':'ti-moon');btn.title=dark?'Switch to light':'Switch to dark';}
function toggleTheme(){isDark=!isDark;localStorage.setItem('sp-theme',isDark?'dark':'light');applyTheme(isDark);}
applyTheme(isDark);
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  var btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> Signing in...';
  try{
    var r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){var d=await r.json().catch(function(){return{};});throw new Error(d.detail||'Error');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> Sign In';
  }
});
</script>
</body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SPIDER PANEL · Enterprise</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Vazirmatn:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#F8FAFC;--bg2:#F1F5F9;--bg3:#E2E8F0;
  --card:rgba(255,255,255,0.75);--card-b:rgba(43,127,255,0.1);--card-bh:rgba(43,127,255,0.25);
  --accent:#2B7FFF;--accent2:#7B61FF;--accent-d:rgba(43,127,255,0.08);
  --green:#16A34A;--green-bg:rgba(22,163,74,0.08);--green-t:#166534;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#991B1B;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-t:#92400E;
  --purple:#7B61FF;--purple-bg:rgba(123,97,255,0.08);--purple-t:#5B21B6;
  --t1:#0F172A;--t2:#334155;--t3:#64748B;
  --sidebar-w:260px;--radius:24px;
  --shadow:0 4px 24px rgba(0,0,0,0.08);
  --gradient:linear-gradient(90deg,#2B7FFF,#7B61FF,#FF2352);
  --font:'Inter',sans-serif;
}
[data-theme="dark"]{
  --bg:#0B1120;--bg2:#111827;--bg3:#1E293B;
  --card:rgba(17,24,39,0.8);--card-b:rgba(43,127,255,0.12);--card-bh:rgba(43,127,255,0.25);
  --accent:#3B82F6;--accent2:#8B7CFF;--accent-d:rgba(59,130,246,0.1);
  --green:#22C55E;--green-bg:rgba(34,197,94,0.1);--green-t:#4ADE80;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#FCA5A5;
  --amber:#FBBF24;--amber-bg:rgba(251,191,36,0.1);--amber-t:#FCD34D;
  --purple:#A78BFA;--purple-bg:rgba(167,139,250,0.1);--purple-t:#C4B5FD;
  --t1:#F1F5F9;--t2:#94A3B8;--t3:#64748B;
  --shadow:0 4px 24px rgba(0,0,0,0.3);
}
html,body{height:100%}
body{font-family:var(--font);background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:13.5px;transition:background .35s,color .35s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}

/* Background effects */
.bg-blobs{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.bg-blob{position:absolute;border-radius:50%;filter:blur(130px);animation:blobDrift 15s ease-in-out infinite}
.bg-blob.b1{width:600px;height:600px;background:rgba(43,127,255,0.07);top:-150px;left:-150px}
.bg-blob.b2{width:500px;height:500px;background:rgba(123,97,255,0.05);bottom:-120px;right:-120px;animation-delay:5s}
.bg-blob.b3{width:400px;height:400px;background:rgba(255,35,82,0.04);top:50%;right:-80px;animation-delay:10s}
@keyframes blobDrift{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(30px,-30px) scale(1.1)}66%{transform:translate(-20px,20px) scale(0.9)}}

/* Sidebar */
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--card);border-right:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;left:0;top:0;bottom:0;z-index:200;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);transition:transform .3s cubic-bezier(.4,0,.2,1),background .35s,border-color .35s}
.sidebar::before{content:'';position:absolute;inset:0;background:rgba(255,255,255,0.02);pointer-events:none}
.logo{padding:22px 20px 18px;border-bottom:1px solid var(--card-b);display:flex;align-items:center;gap:12px}
.logo-svg{width:40px;height:40px;flex-shrink:0}
.logo-text{min-width:0}
.logo-name{font-size:15px;font-weight:800;letter-spacing:-.01em;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.logo-sub{font-size:9.5px;color:var(--t3);font-weight:500;margin-top:1px}
.sb-close{display:none;position:absolute;right:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:10px;font-size:16px;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.sb-close:hover{background:rgba(220,38,38,0.1);color:var(--red-t)}
.nav-wrap{flex:1;overflow-y:auto;padding:8px 0}
.nav-sec{padding:16px 20px 6px;font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:10px;padding:10px 16px;margin:2px 10px;color:var(--t2);font-size:12.5px;font-weight:500;cursor:pointer;border-radius:14px;transition:all .18s;position:relative}
.nav-it i{font-size:17px;width:20px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t1)}
.nav-it.on{background:var(--accent-d);color:var(--t1);font-weight:600}
.nav-it.on::before{content:'';position:absolute;left:0;top:50%;transform:translateY(-50%);width:3px;height:24px;border-radius:0 3px 3px 0;background:var(--gradient)}
.nav-badge{margin-left:auto;background:var(--accent-d);color:var(--accent);font-size:9.5px;padding:2px 8px;border-radius:20px;font-weight:700}
.sb-foot{padding:14px 16px;border-top:1px solid var(--card-b);display:flex;flex-direction:column;gap:7px}
.tg-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#0098e6,#0077bb);color:#fff;border-radius:12px;padding:10px;font-size:12px;font-weight:600;font-family:inherit;border:none;cursor:pointer;width:100%;transition:.15s}
.tg-btn:hover{filter:brightness(1.1)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:12px;padding:9px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.15s}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:12px;padding:9px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(220,38,38,0.2);cursor:pointer;width:100%;transition:.15s}
.logout-btn:hover{background:rgba(220,38,38,0.2)}

/* Mobile */
.mob-top{display:none;position:fixed;top:0;left:0;right:0;height:54px;background:var(--card);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 16px;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.mob-top .ml{display:flex;align-items:center;gap:10px}
.mob-logo-svg{width:30px;height:30px}
.mob-title{font-size:14px;font-weight:800;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.mob-right{display:flex;gap:7px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:36px;height:36px;border-radius:12px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.menu-btn:hover,.theme-mob:hover{color:var(--accent)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}

/* Content */
.main{margin-left:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .3s;position:relative;z-index:1}
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
.badge{font-size:10px;padding:4px 12px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
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
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:20px 20px 18px;transition:all .25s;position:relative;overflow:hidden;cursor:default;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.metric::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--gradient);opacity:0;transition:.25s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:var(--shadow)}
.metric:hover::before{opacity:1}
.metric.suc::before{background:var(--green)}
.metric.dan::before{background:var(--red)}
.m-icon{width:38px;height:38px;border-radius:12px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:var(--accent);font-size:18px}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:5px;font-weight:600;text-transform:uppercase;letter-spacing:.06em}
.m-val{font-size:28px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:13px;font-weight:500;color:var(--t3)}
.m-sub{font-size:10.5px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:4px}

/* Default VLESS box */
.vless-box{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px;margin-bottom:20px;position:relative;overflow:hidden;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.vless-box::before{content:'';position:absolute;top:-50px;right:-50px;width:180px;height:180px;background:radial-gradient(circle,rgba(43,127,255,0.1),transparent 70%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px;position:relative;z-index:1}
.vl-title{color:var(--t2);font-size:11.5px;display:flex;align-items:center;gap:7px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent);font-size:16px}
.vl-code{background:rgba(0,0,0,0.08);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px;font-size:11.5px;font-family:'SF Mono','Fira Code',ui-monospace,monospace;color:var(--accent);word-break:break-all;line-height:1.8;position:relative;z-index:1}
[data-theme="dark"] .vl-code{background:rgba(0,0,0,0.2)}
.vl-actions{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap;position:relative;z-index:1}

/* Buttons */
.btn{font-family:inherit;font-size:12px;font-weight:600;border-radius:14px;padding:9px 16px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border:none;transition:all .18s;white-space:nowrap}
.btn i{font-size:14px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{background:var(--accent);color:#fff;box-shadow:0 3px 14px rgba(43,127,255,0.3)}
.btn-p:hover{background:#2563EB;box-shadow:0 5px 20px rgba(43,127,255,0.4);transform:translateY(-1px)}
.btn-o{background:transparent;border:1.5px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:rgba(43,127,255,0.3)}
.btn-g{background:var(--accent-d);color:var(--accent);border:1px solid rgba(43,127,255,0.12)}
.btn-g:hover{background:rgba(43,127,255,0.18)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(220,38,38,0.15)}
.btn-d:hover{background:rgba(220,38,38,0.2)}
.btn-pur{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(123,97,255,0.15)}
.btn-pur:hover{background:rgba(123,97,255,0.2)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,0.15)}
.btn-amber:hover{background:rgba(245,158,11,0.2)}
.btn-sm{padding:6px 10px;font-size:10.5px;border-radius:10px}
.btn-icon{width:32px;height:32px;padding:0;justify-content:center;border-radius:10px}

/* Cards */
.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:20px 22px;transition:border-color .25s,background .35s,transform .25s;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.card:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.card-title{font-size:13px;font-weight:700;color:var(--t1);margin-bottom:16px;display:flex;align-items:center;gap:8px}
.card-title i{font-size:17px;color:var(--accent)}
.ml-auto{margin-left:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:18px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:14px;margin-bottom:18px}
.mb16{margin-bottom:16px}

/* Status rows */
.sr{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(43,127,255,0.05);font-size:12px}
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
.fg label{font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em}
.fi,.fs{padding:10px 13px;border-radius:12px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.03);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s;min-width:100px}
[data-theme="dark"] .fi,[data-theme="dark"] .fs{background:rgba(0,0,0,0.2)}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:rgba(43,127,255,0.45);box-shadow:0 0 0 3px rgba(43,127,255,0.08)}
.fs option{background:var(--bg2)}
.cl{background:var(--accent-d);border:1px solid rgba(43,127,255,0.12);border-radius:12px;padding:12px 14px;font-size:11.5px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.7;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(245,158,11,0.15);color:var(--amber-t)}
.cl.amber i{color:var(--amber)}

/* Create Panel */
.create-panel{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;margin-bottom:18px;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);position:relative}
.create-panel::before{content:'';position:absolute;top:-60px;right:-60px;width:220px;height:220px;background:radial-gradient(circle,rgba(43,127,255,0.12),transparent 70%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:14px;padding:24px 26px 20px;position:relative;z-index:1}
.cp-head-icon{width:48px;height:48px;border-radius:16px;background:var(--gradient);display:flex;align-items:center;justify-content:center;color:#fff;font-size:21px;flex-shrink:0;box-shadow:0 6px 18px rgba(43,127,255,0.3)}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:16px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:3px}
.cp-body{padding:4px 26px 24px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:16px;margin-bottom:18px}
.cp-block{background:rgba(0,0,0,0.03);border:1px solid var(--card-b);border-radius:16px;padding:16px 18px}
[data-theme="dark"] .cp-block{background:rgba(0,0,0,0.15)}
.cp-block-label{font-size:10.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:7px;margin-bottom:12px}
.cp-block-label i{color:var(--accent);font-size:15px}
.cp-input-full{width:100%;padding:11px 14px;border-radius:13px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.04);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
[data-theme="dark"] .cp-input-full{background:rgba(0,0,0,0.2)}
.cp-input-full:focus{border-color:rgba(43,127,255,0.5);box-shadow:0 0 0 3px rgba(43,127,255,0.1)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:10px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
.chip{font-size:10.5px;font-weight:700;padding:6px 13px;border-radius:10px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;white-space:nowrap}
.chip:hover{background:rgba(43,127,255,0.18);color:var(--accent)}
.chip.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 12px rgba(43,127,255,0.35)}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.proto-card{border:1.5px solid var(--card-b);border-radius:16px;padding:15px 13px;cursor:pointer;transition:.2s;text-align:center;position:relative;background:rgba(0,0,0,0.02)}
[data-theme="dark"] .proto-card{background:rgba(0,0,0,0.1)}
.proto-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(43,127,255,0.08)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-check{position:absolute;top:8px;right:8px;width:18px;height:18px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.22s}
.proto-card-icon{width:36px;height:36px;border-radius:12px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:17px;margin:0 auto 9px}
.proto-card.active .proto-card-icon{background:var(--accent);color:#fff}
.proto-card-title{font-size:11.5px;font-weight:800;color:var(--t1)}
.proto-card-desc{font-size:9.5px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:14px;padding-top:18px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:9px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:16px;flex-shrink:0}
.cp-submit-btn{background:var(--gradient);color:#fff;border:none;border-radius:16px;padding:14px 28px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 22px rgba(43,127,255,0.3);transition:.2s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(43,127,255,0.45)}
.cp-submit-btn:active{transform:translateY(0) scale(.98)}
@media(max-width:760px){.cp-row{grid-template-columns:1fr}.proto-cards{grid-template-columns:1fr}.cp-footer{flex-direction:column;align-items:stretch}.cp-submit-btn{justify-content:center}}

/* Server panel */
.srv-panel{background:var(--card);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;position:relative;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.srv-panel::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,rgba(43,127,255,0.1),transparent 70%);pointer-events:none}
.srv-hero{display:flex;align-items:center;gap:16px;padding:24px 26px;position:relative;z-index:1;border-bottom:1px solid var(--card-b)}
.srv-hero-icon{width:52px;height:52px;border-radius:16px;background:var(--gradient);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(43,127,255,0.3)}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:15.5px;font-weight:800;color:var(--t1);word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:22px 24px;position:relative;z-index:1}
.srv-tile{display:flex;align-items:center;gap:12px;background:rgba(0,0,0,0.03);border:1px solid var(--card-b);border-radius:16px;padding:14px 16px;transition:.18s}
[data-theme="dark"] .srv-tile{background:rgba(0,0,0,0.15)}
.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.srv-tile-icon{width:38px;height:38px;border-radius:12px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12.5px;font-weight:700;color:var(--t1);word-break:break-word}

/* Password panel */
.pw-panel{background:var(--card);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;position:relative;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.pw-panel::before{content:'';position:absolute;bottom:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,rgba(123,97,255,0.12),transparent 70%);pointer-events:none}
.pw-hero{display:flex;align-items:center;gap:16px;padding:24px 26px 20px;position:relative;z-index:1}
.pw-hero-icon{width:52px;height:52px;border-radius:16px;background:linear-gradient(135deg,#7B61FF,#FF2352);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(123,97,255,0.35)}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:15.5px;font-weight:800;color:var(--t1)}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:4px 26px 24px;position:relative;z-index:1}
.pw-field{position:relative;margin-bottom:14px}
.pw-field label{display:block;font-size:10.5px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}
.pw-input{width:100%;padding:12px 44px 12px 15px;border-radius:14px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.03);color:var(--t1);font-family:inherit;font-size:13px;outline:none;transition:.18s}
[data-theme="dark"] .pw-input{background:rgba(0,0,0,0.2)}
.pw-input:focus{border-color:rgba(123,97,255,0.5);box-shadow:0 0 0 3px rgba(123,97,255,0.1)}
.pw-eye{position:absolute;right:13px;top:36px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.pw-eye:hover{color:var(--purple)}
.pw-strength{height:5px;border-radius:3px;background:var(--accent-d);margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:rgba(100,116,139,0.2);transition:.25s}
.pw-strength-label{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:7px;margin-top:12px;margin-bottom:18px}
.pw-req{font-size:9.5px;padding:4px 10px;border-radius:8px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.18s}
.pw-req.met{background:var(--green-bg);color:var(--green-t)}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,#7B61FF,#FF2352);color:#fff;border:none;border-radius:16px;padding:13px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(123,97,255,0.3);transition:.2s}
.pw-submit:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(123,97,255,0.45)}
.pw-submit:active{transform:translateY(0) scale(.98)}

/* Sub groups */
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:18px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:12px 42px 12px 16px;border-radius:15px;border:1.5px solid var(--card-b);background:var(--card);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s;backdrop-filter:blur(12px)}
.subs-search input:focus{border-color:rgba(123,97,255,0.5);box-shadow:0 0 0 3px rgba(123,97,255,0.08)}
.subs-search i{position:absolute;right:15px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:16px}
.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:18px;margin-bottom:20px}
.sub-card{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;transition:all .3s cubic-bezier(.4,0,.2,1);position:relative;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.sub-card:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:0 16px 40px rgba(0,0,0,0.12)}
.sub-card-top{background:linear-gradient(155deg,rgba(123,97,255,0.06) 0%,transparent 65%);padding:22px 22px 18px;position:relative}
.sub-card-top::before{content:'';position:absolute;top:-30px;right:-30px;width:140px;height:140px;background:radial-gradient(circle,rgba(123,97,255,0.12),transparent 70%);pointer-events:none}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:14px;position:relative;z-index:1}
.sub-card-icon{width:50px;height:50px;border-radius:16px;background:linear-gradient(135deg,#7B61FF,#FF2352);display:flex;align-items:center;justify-content:center;color:#fff;font-size:21px;flex-shrink:0;box-shadow:0 6px 18px rgba(123,97,255,0.3)}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:16px;font-weight:800;color:var(--t1);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:28px;height:28px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:13px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}
.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative;z-index:1;margin-top:18px;background:rgba(0,0,0,0.03);border:1px solid var(--card-b);border-radius:16px;overflow:hidden}
[data-theme="dark"] .sub-card-stats{background:rgba(0,0,0,0.12)}
.sub-card-stat{padding:12px 8px;text-align:center;border-right:1px solid var(--card-b)}
.sub-card-stat:last-child{border-right:none}
.sub-card-stat-val{font-size:16px;font-weight:800;color:var(--t1);line-height:1.2}
.sub-card-stat-label{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}
.sub-card-url-row{margin:16px 22px 0;background:rgba(123,97,255,0.06);border:1px dashed rgba(123,97,255,0.2);border-radius:14px;padding:10px 13px;display:flex;align-items:center;gap:8px}
.sub-card-url-text{font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:10px;color:var(--purple);flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
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
.spbar{height:5px;border-radius:3px;background:var(--accent-d);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:var(--gradient);transition:width 1s}
.cfg-card{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:0;transition:all .25s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 6px 28px rgba(0,0,0,0.1)}
.cfg-card.is-off{opacity:.55}
.cfg-card.is-exp{opacity:.75}
.cfg-row{display:flex;align-items:center;gap:18px;padding:16px 20px}
.cfg-status-dot{width:10px;height:10px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 4px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 4px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 4px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:14px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:8px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:9.5px;color:var(--accent);background:var(--accent-d);padding:3px 8px;border-radius:6px;cursor:pointer;transition:.15s}
.cfg-uuid-mini:hover{background:rgba(43,127,255,0.2)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:6px;border-radius:4px;background:rgba(43,127,255,0.08);overflow:hidden}
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
.conn-hero-tile{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:18px 20px;position:relative;overflow:hidden;transition:.25s;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.conn-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;left:0;right:0;height:3px;background:var(--gradient)}
.conn-hero-icon{width:36px;height:36px;border-radius:12px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:16px;margin-bottom:12px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-d);color:var(--accent)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.conn-hero-val{font-size:24px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.conn-hero-unit{font-size:11px;color:var(--t3);font-weight:500}
.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:16px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12.5px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}
.conn-toolbar-title i{color:var(--green);font-size:16px}
.conn-live-badge{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--green-t);background:var(--green-bg);padding:6px 13px;border-radius:20px;border:1px solid rgba(22,163,74,0.15)}
.conn-live-dot{width:7px;height:7px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite}
.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}
.conn-card-v2{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;transition:all .3s cubic-bezier(.4,0,.2,1);position:relative;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.conn-card-v2:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 36px rgba(0,0,0,0.15)}
.conn-card-v2-glow{position:absolute;top:-40px;right:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(22,163,74,0.08),transparent 70%);pointer-events:none}
.conn-card-v2-top{display:flex;align-items:center;gap:14px;padding:18px 20px 15px;position:relative;z-index:1}
.conn-avatar{width:46px;height:46px;border-radius:16px;background:linear-gradient(135deg,#16A34A,#0D9668);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;position:relative;box-shadow:0 4px 16px rgba(22,163,74,0.25)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:19px;border:1.5px solid var(--green);opacity:.4;animation:breathe2 2.4s ease-in-out infinite}
@keyframes breathe2{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.12);opacity:0}}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
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
.conn-stat-text-label{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.conn-stat-text-val{font-size:12px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-duration-track{height:6px;border-radius:4px;background:var(--accent-d);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,#16A34A,#3FD79C);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);width:40%;animation:shimmer 1.8s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}
.conn-empty-v2{text-align:center;padding:80px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:22px}
.conn-empty-v2-icon{width:70px;height:70px;border-radius:20px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:30px;color:var(--t3);margin:0 auto 18px}
.conn-empty-v2-title{font-size:14px;font-weight:700;color:var(--t2);margin-bottom:6px}
.conn-empty-v2-sub{font-size:11px;color:var(--t3)}

/* Logs */
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:13px;padding:12px 0;border-bottom:1px solid rgba(43,127,255,0.04);position:relative}
.log-item:last-child{border-bottom:none}
.log-ic{width:32px;height:32px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.log-ic.err{background:var(--red-bg);color:var(--red-t)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-ic.info{background:var(--accent-d);color:var(--accent)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:9px;padding:2px 8px;border-radius:10px;background:var(--accent-d);color:var(--accent);font-weight:700;text-transform:uppercase;letter-spacing:.05em}
.erow{padding:10px 0;border-bottom:1px solid rgba(43,127,255,0.04)}
.erow:last-child{border-bottom:none}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px;display:flex;align-items:center;gap:5px}
.emsg{color:var(--red-t);font-family:'SF Mono','Fira Code',ui-monospace,monospace;background:var(--red-bg);padding:7px 10px;border-radius:8px;word-break:break-all;font-size:10.5px}

/* Empty state */
.empty{text-align:center;padding:60px 20px;color:var(--t3)}
.empty i{font-size:42px;opacity:.3;margin-bottom:14px;display:block}
.empty p{font-size:13px;margin-top:4px}

/* Modal v2 */
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(6px)}
.modal-bg.open{display:flex}
.modal-v2{background:var(--card);border:1px solid var(--card-b);border-radius:28px;padding:0;max-width:460px;width:calc(100% - 32px);max-height:92vh;overflow-y:auto;position:relative;animation:modalIn .25s ease;box-shadow:0 24px 70px rgba(0,0,0,0.3);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px)}
@keyframes modalIn{from{opacity:0;transform:translateY(10px) scale(.97)}to{opacity:1;transform:none}}
.modal-v2-head{background:linear-gradient(155deg,rgba(123,97,255,0.08) 0%,transparent 65%);padding:20px 24px 16px;position:relative;overflow:hidden}
.modal-v2-head::before{content:'';position:absolute;top:-50px;right:-50px;width:160px;height:160px;background:radial-gradient(circle,rgba(123,97,255,0.15),transparent 70%);pointer-events:none}
.modal-v2-close{position:absolute;top:14px;right:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:32px;height:32px;border-radius:11px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:.15s}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(220,38,38,0.25)}
.modal-v2-icon{width:46px;height:46px;border-radius:16px;background:linear-gradient(135deg,#7B61FF,#FF2352);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;margin-bottom:12px;position:relative;z-index:1;box-shadow:0 8px 20px rgba(123,97,255,0.35)}
.modal-v2-title{font-size:16px;font-weight:800;color:var(--t1);position:relative;z-index:1;letter-spacing:-.01em}
.modal-v2-sub{font-size:11px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:18px 24px 22px;border-top:1px solid var(--card-b)}
.modal-v2-field{margin-bottom:12px}
.modal-v2-field label{display:flex;align-items:center;gap:6px;font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.modal-v2-field label i{color:var(--purple);font-size:14px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none;transition:.15s;z-index:1}
.modal-v2-input{width:100%;padding:10px 40px 10px 14px;border-radius:14px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.03);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
[data-theme="dark"] .modal-v2-input{background:rgba(0,0,0,0.15)}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-input:focus{border-color:rgba(123,97,255,0.55);box-shadow:0 0 0 3px rgba(123,97,255,0.12)}
.modal-v2-input:focus~i{color:var(--purple)}
.modal-v2-hint{background:rgba(43,127,255,0.06);border:1px solid rgba(43,127,255,0.12);border-radius:13px;padding:10px 13px;font-size:10.5px;color:var(--t2);display:flex;gap:7px;align-items:flex-start;line-height:1.6;margin-top:3px}
.modal-v2-hint i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:9px;margin-top:16px}
.modal-v2-btn-cancel{flex:.75;justify-content:center;padding:11px;border-radius:14px;background:transparent;border:1.5px solid var(--card-b);color:var(--t2);font-family:inherit;font-size:12.5px;font-weight:700;cursor:pointer;transition:.15s;display:flex;align-items:center}
.modal-v2-btn-cancel:hover{background:var(--accent-d);color:var(--t1)}
.modal-v2-btn-submit{flex:1;justify-content:center;padding:11px;border-radius:14px;background:linear-gradient(135deg,#7B61FF,#FF2352);color:#fff;border:none;font-family:inherit;font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;box-shadow:0 6px 20px rgba(123,97,255,0.35);transition:.2s}
.modal-v2-btn-submit:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(123,97,255,0.5)}
.modal-v2-btn-submit:active{transform:translateY(0) scale(.98)}

/* Links modal */
.lmodal-head{background:linear-gradient(155deg,rgba(43,127,255,0.08) 0%,transparent 70%);padding:24px 26px 20px;position:relative;border-bottom:1px solid var(--card-b)}
.lmodal-icon-row{display:flex;align-items:center;gap:14px;position:relative;z-index:1}
.lmodal-icon{width:48px;height:48px;border-radius:16px;background:var(--gradient);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 18px rgba(43,127,255,0.3)}
.lmodal-title-v2{font-size:15px;font-weight:800;color:var(--t1)}
.lmodal-sub-v2{font-size:10.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:16px;position:relative}
.lmodal-search input{width:100%;padding:11px 40px 11px 14px;border-radius:14px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.03);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.18s}
[data-theme="dark"] .lmodal-search input{background:rgba(0,0,0,0.15)}
.lmodal-search input:focus{border-color:rgba(43,127,255,0.5);box-shadow:0 0 0 3px rgba(43,127,255,0.08)}
.lmodal-search i{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:12px;position:relative;z-index:1}
.lmodal-qbtn{font-size:10.5px;font-weight:700;padding:6px 12px;border-radius:10px;background:var(--accent-d);color:var(--accent);border:1px solid var(--card-b);cursor:pointer;transition:.15s;font-family:inherit}
.lmodal-qbtn:hover{background:rgba(43,127,255,0.2)}
.lmodal-count{margin-left:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}
.lmodal-list{padding:12px 16px;max-height:380px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:16px;cursor:pointer;transition:.15s;margin-bottom:4px;border:1px solid transparent}
.lrow-v2:hover{background:var(--accent-d)}
.lrow-v2.checked{background:rgba(43,127,255,0.08);border-color:rgba(43,127,255,0.2)}
.lrow-v2-check{width:22px;height:22px;border-radius:8px;border:2px solid var(--card-b);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s;background:rgba(0,0,0,0.04)}
[data-theme="dark"] .lrow-v2-check{background:rgba(0,0,0,0.15)}
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
.modal{background:var(--card);border:1px solid var(--card-b);border-radius:28px;padding:30px 28px;max-width:540px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:modalIn .25s ease;backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px)}
.modal-close{position:absolute;top:14px;right:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:32px;height:32px;border-radius:10px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none}
.modal-close:hover{background:var(--red-bg);color:var(--red-t)}
.modal-title{font-size:17px;font-weight:700;color:var(--t1);margin-bottom:20px;display:flex;align-items:center;gap:9px}
.modal-title i{color:var(--accent)}
.lrow{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid rgba(43,127,255,0.05)}
.lrow:last-child{border-bottom:none}
.lrow-check{width:16px;height:16px;border-radius:4px;cursor:pointer;accent-color:var(--accent)}
.lrow-label{flex:1;font-size:12px;color:var(--t1)}
.lrow-badge{font-size:9px;padding:2px 7px;border-radius:5px;background:var(--green-bg);color:var(--green-t);font-weight:700}

/* Toast */
.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:14px;padding:12px 22px;font-size:12.5px;font-weight:600;opacity:0;transition:all .3s cubic-bezier(.4,0,.2,1);z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:0 8px 30px rgba(0,0,0,0.15);white-space:nowrap;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(22,163,74,0.3);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(220,38,38,0.3);background:var(--red-bg);color:var(--red-t)}

/* Dashboard footer */
.dash-footer{border-top:1px solid var(--card-b);margin-top:16px;padding-top:16px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10.5px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent);display:flex;align-items:center;gap:6px;font-weight:600}
.df-link:hover{color:var(--accent2)}

/* Traffic page */
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:14px;margin-bottom:20px}
.traf-main-stat{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px 26px;position:relative;overflow:hidden;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.traf-main-stat::before{content:'';position:absolute;top:-50px;right:-50px;width:200px;height:200px;background:radial-gradient(circle,rgba(43,127,255,0.1),transparent 70%);pointer-events:none}
.traf-main-label{font-size:11px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:7px;margin-bottom:12px;position:relative;z-index:1}
.traf-main-val{font-size:36px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;display:flex;align-items:baseline;gap:6px;position:relative;z-index:1}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 11px;border-radius:20px;margin-top:14px;position:relative;z-index:1}
.traf-trend.up{background:var(--green-bg);color:var(--green-t)}
.traf-trend.down{background:var(--red-bg);color:var(--red-t)}
.traf-mini{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:20px;display:flex;flex-direction:column;justify-content:space-between;transition:.25s;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.traf-mini:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px}
.traf-mini-icon{width:34px;height:34px;border-radius:12px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}
.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.traf-mini-val{font-size:22px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.traf-mini-sub{font-size:10px;color:var(--t3);margin-top:4px}
.traf-chart-card{background:var(--card);border:1px solid var(--card-b);border-radius:24px;padding:24px 26px 20px;margin-bottom:18px;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:14.5px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:19px}
.traf-chart-sub{font-size:11px;color:var(--t3);margin-top:4px}
.traf-legend{display:flex;gap:16px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:11px;color:var(--t2);font-weight:600}
.traf-legend-dot{width:9px;height:9px;border-radius:3px}
.traf-range-tabs{display:flex;gap:4px;background:var(--accent-d);padding:3px;border-radius:12px;border:1px solid var(--card-b)}
.traf-range-tab{padding:7px 14px;border-radius:10px;font-size:11px;font-weight:700;color:var(--t3);cursor:pointer;transition:.15s;border:none;background:transparent;font-family:inherit}
.traf-range-tab.on{background:var(--accent);color:#fff;box-shadow:0 2px 8px rgba(43,127,255,0.3)}
.traf-chart-body{height:340px;margin-top:16px;position:relative}

/* Subscriptions */
.sub-box{background:rgba(123,97,255,0.06);border:1px solid rgba(123,97,255,0.18);border-radius:14px;padding:16px 18px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:12px}
.sub-url{font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:11px;color:var(--purple);word-break:break-all;flex:1}

@media(max-width:900px){.traf-hero{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.traf-hero{grid-template-columns:1fr}.traf-chart-body{height:280px}}
@media(max-width:760px){.conn-hero{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.srv-tiles{grid-template-columns:1fr}}
@media(max-width:500px){.sub-grid{grid-template-columns:1fr}.sub-card-stats{grid-template-columns:repeat(3,1fr)}.conn-grid-v2{grid-template-columns:1fr}}

@media(max-width:1050px){
  .sidebar{transform:translateX(-100%)}
  .sidebar.open{transform:translateX(0);box-shadow:10px 0 40px rgba(0,0,0,.3)}
  .sb-close{display:flex}
  .main{margin-left:0;padding-top:72px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:64px 14px 50px}
  .sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}
  .sub-grid{grid-template-columns:1fr}
}
</style>
</head>
<body>
<div class="bg-blobs"><div class="bg-blob b1"></div><div class="bg-blob b2"></div><div class="bg-blob b3"></div></div>
<div class="toast" id="toast"></div>

<!-- Links Modal -->
<div class="modal-bg" id="modal-links">
  <div class="modal-v2" style="max-width:520px">
    <div class="lmodal-head">
      <button class="modal-v2-close" onclick="closeModal('modal-links')"><i class="ti ti-x"></i></button>
      <div class="lmodal-icon-row">
        <div class="lmodal-icon"><i class="ti ti-link-plus"></i></div>
        <div>
          <div class="lmodal-title-v2">Manage Configs for <span id="modal-sub-name" style="color:var(--accent)">—</span></div>
          <div class="lmodal-sub-v2">Select which configs belong to this group</div>
        </div>
      </div>
      <div class="lmodal-search">
        <i class="ti ti-search"></i>
        <input type="text" id="lmodal-search-inp" placeholder="Search configs..." oninput="filterLmodal(this.value)">
      </div>
      <div class="lmodal-quickbar">
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> Select All</button>
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> Deselect All</button>
        <span class="lmodal-count" id="lmodal-count">0 selected</span>
      </div>
    </div>
    <div class="lmodal-list" id="modal-links-body">Loading...</div>
    <div class="lmodal-footer">
      <div class="lmodal-footer-info"><i class="ti ti-info-circle"></i> Changes apply immediately</div>
      <div class="lmodal-footer-btns">
        <button class="btn btn-o" onclick="closeModal('modal-links')">Cancel</button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> Save</button>
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
      <div class="modal-v2-title">Create New Group</div>
      <div class="modal-v2-sub">Create a separate public page for managing configs</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> Group Name</label>
        <input class="modal-v2-input" id="ns-name" placeholder="e.g. Telegram Channel">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> Description (optional)</label>
        <input class="modal-v2-input" id="ns-desc" placeholder="Short description">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-lock"></i> Public Page Password (optional)</label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="Leave empty = no password">
      </div>
      <div class="cl" style="margin-top:16px"><i class="ti ti-info-circle"></i><span>The public page will be accessible via a unique link on the internet.</span></div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-sub')" style="flex:.6">Cancel</button>
        <button class="btn btn-pur" onclick="createSub()"><i class="ti ti-folder-plus"></i> Create Group</button>
      </div>
    </div>
  </div>
</div>

<!-- Edit Link Modal -->
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> Edit Config</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:14px"><label>Label</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:14px">
      <div class="fg" style="flex:1"><label>Quota (0 = Unlimited)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>Unit</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:14px"><label>Expiry (days from now, 0 = no change/unlimited)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:18px"><label>Note</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>Set expiry to 0 to keep current expiration date.</span></div>
    <div style="margin-top:18px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">Cancel</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> Save Changes</button>
    </div>
  </div>
</div>

<!-- Mobile Topbar -->
<div class="mob-top">
  <div class="ml">
    <svg class="mob-logo-svg" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="16" stroke="url(#mobGrad)" stroke-width="1.2"/><defs><linearGradient id="mobGrad" x1="0" y1="0" x2="36" y2="36"><stop stop-color="#2B7FFF"/><stop offset="0.5" stop-color="#7B61FF"/><stop offset="1" stop-color="#FF2352"/></linearGradient></defs><path d="M18 5L20 16L31 18L20 20L18 31L16 20L5 18L16 16Z" fill="url(#mobGrad)" opacity="0.9"/></svg>
    <span class="mob-title">SPIDER PANEL</span>
  </div>
  <div class="mob-right">
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>

<div class="overlay" id="overlay"></div>

<!-- Sidebar -->
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <svg class="logo-svg" viewBox="0 0 48 48" fill="none">
      <circle cx="24" cy="24" r="22" stroke="url(#sbGrad)" stroke-width="1.5"/>
      <defs><linearGradient id="sbGrad" x1="0" y1="0" x2="48" y2="48"><stop stop-color="#2B7FFF"/><stop offset="0.5" stop-color="#7B61FF"/><stop offset="1" stop-color="#FF2352"/></linearGradient></defs>
      <path d="M24 6L26 22L42 24L26 26L24 42L22 26L6 24L22 22Z" fill="url(#sbGrad)" opacity="0.9"/>
      <circle cx="24" cy="24" r="3.5" fill="url(#sbGrad)"/>
      <path d="M17 14L21 20" stroke="url(#sbGrad)" stroke-width="1.2"/>
      <path d="M31 14L27 20" stroke="url(#sbGrad)" stroke-width="1.2"/>
      <path d="M17 34L21 28" stroke="url(#sbGrad)" stroke-width="1.2"/>
      <path d="M31 34L27 28" stroke="url(#sbGrad)" stroke-width="1.2"/>
    </svg>
    <div class="logo-text"><div class="logo-name">SPIDER PANEL</div><div class="logo-sub">Enterprise Network Management</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">Panel</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> Dashboard</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> Configs <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> Sub Groups <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> Subscriptions</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> Traffic</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> Connections <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-sec">System</div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> Security</div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> Activity Log</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> Errors</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> WebSocket Test</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> Settings</div>
  </div>
  <div class="sb-foot">
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">Dark Mode</span></button>
    <a class="tg-btn" href="https://t.me/CodeBoxo" target="_blank" rel="noopener"><i class="ti ti-brand-telegram"></i> @CodeBoxo</a>
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> Sign Out</button>
  </div>
</aside>

<!-- Main Content -->
<main class="main">

<!-- Overview -->
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div class="tb-left"><div class="tb-title"><i class="ti ti-layout-dashboard"></i> Dashboard</div><div class="tb-sub" id="last-upd">Loading...</div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot dg pulse"></span> Online</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh</button>
    </div>
  </div>
  <div class="metrics">
    <div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">Active Connections</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span class="dot dg pulse"></span> WebSocket / XHTTP Live</div></div>
    <div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label">Total Traffic</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">Since startup</div></div>
    <div class="metric suc"><div class="m-icon suc"><i class="ti ti-link"></i></div><div class="m-label">Active Configs</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">of total</div></div>
    <div class="metric pur"><div class="m-icon pur"><i class="ti ti-folders"></i></div><div class="m-label">Sub Groups</div><div class="m-val" id="m-subs">—</div><div class="m-sub">Active</div></div>
  </div>
  <div class="vless-box">
    <div class="vl-header">
      <div class="vl-title"><i class="ti ti-link"></i> Default Config (Unlimited)</div>
      <span class="badge bg-blue"><span class="dot db"></span> TLS 443 · WS</span>
    </div>
    <div class="vl-code" id="vless-main">Loading...</div>
    <div class="vl-actions">
      <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> Copy</button>
      <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> Limited Configs</button>
      <button class="btn btn-pur" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> Sub Groups</button>
    </div>
  </div>
  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> Hourly Traffic (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-donut"></i> Distribution</div><div class="ch-sm"><canvas id="ch2"></canvas></div></div>
  </div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-activity"></i> Service Status</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● Active · Strict</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS Tunnel</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● Active · 3 modes</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-folders"></i> Sub Groups</span><span class="sr-v" style="color:var(--green-t)">● Active v9</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> Subscription API</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> Uptime</span><span class="sr-v" id="uptime-inline">—</span></div>
      <div class="sr" style="flex-direction:column;align-items:flex-start;gap:6px">
        <div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> Relative Load</span><span class="sr-v" id="bw-pct">—%</span></div>
        <div class="spbar" style="width:100%"><div class="spfill" id="bw-bar" style="width:0%"></div></div>
      </div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> Config Summary <span class="ml-auto badge bg-blue" id="lsummary-badge">0</span></div>
      <div id="lsummary">—</div>
    </div>
  </div>
  <div class="dash-footer">
    <span class="df-text">SPIDER PANEL v1.0 · Railway · 2025</span>
    <a class="df-link" href="https://t.me/CodeBoxo" target="_blank"><i class="ti ti-brand-telegram"></i> t.me/CodeBoxo</a>
  </div>
</section>

<!-- Configs -->
<section class="pg" id="pg-links">
  <div class="topbar">
    <div class="tb-left"><div class="tb-title"><i class="ti ti-link-plus"></i> Configs</div><div class="tb-sub">Create and manage configs with quota, expiry and grouping</div></div>
    <div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">0 Configs</span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">Create New Config</div>
        <div class="cp-head-sub">Random UUID · Select quota, expiry and protocol</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> Config Identity</div>
          <input class="cp-input-full" id="nl-label" placeholder="e.g. User Ali">
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-note" placeholder="Note (optional)">
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> Sub Group &amp; Expiry</div>
          <select class="cp-input-full fs" id="nl-sub"><option value="">— No Group —</option></select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="Expiry (days) · 0 = Unlimited">
          </div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">Unlimited</span>
            <span class="chip" onclick="setExpiry(7,this)">7 Days</span>
            <span class="chip active" onclick="setExpiry(30,this)">30 Days</span>
            <span class="chip" onclick="setExpiry(90,this)">90 Days</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> Traffic Quota</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = Unlimited">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)">Unlimited</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">500 MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">1 GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">5 GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">10 GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">50 GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> Transport Protocol</div>
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
            <div class="proto-card-desc">Stable &amp; general purpose</div>
          </div>
          <div class="proto-card" data-val="xhttp-packet-up" onclick="selectProto('xhttp-packet-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-bolt"></i></div>
            <div class="proto-card-title">XHTTP · packet-up</div>
            <div class="proto-card-desc">CDN compatible</div>
          </div>
          <div class="proto-card" data-val="xhttp-stream-up" onclick="selectProto('xhttp-stream-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-rocket"></i></div>
            <div class="proto-card-title">XHTTP · stream-up</div>
            <div class="proto-card-desc">Lower latency</div>
          </div>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID is generated randomly · Only registered UUIDs can connect · Protocol cannot be changed after creation.</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> Create Config</button>
      </div>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>No configs yet</p></div>
</section>

<!-- Sub Groups -->
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div class="tb-left"><div class="tb-title"><i class="ti ti-folders"></i> Sub Groups</div><div class="tb-sub">Each group has its own public page with dedicated configs</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">0 Groups</span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> New Group</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="Search groups..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">No groups yet</div><div class="subs-empty-v2-sub">Create a group to organize your configs</div></div>
  </div>
</section>

<!-- Subscriptions -->
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-rss"></i> Subscriptions</div><div class="tb-sub">Subscription links for v2ray apps</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-rss"></i> Individual Subscriptions</div>
      <p style="font-size:12px;color:var(--t3);line-height:1.8;margin-bottom:14px">Each config has its own subscription URL. Click the <i class="ti ti-rss"></i> icon on the config card.</p>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-database"></i> Full Subscription (Admin)</div>
      <p style="font-size:12px;color:var(--t3);line-height:1.8;margin-bottom:4px">Includes all active configs.</p>
      <div class="sub-box"><span class="sub-url" id="sub-all-url">Loading...</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
      <div class="cl amber" style="margin-top:13px"><i class="ti ti-alert-triangle"></i><span>This address only works in a browser logged into the panel (requires session cookie).</span></div>
    </div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-folders"></i> Group Subscription Links</div>
    <div id="sub-groups-list">Loading...</div>
  </div>
</section>

<!-- Traffic -->
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div class="tb-left"><div class="tb-title"><i class="ti ti-chart-area"></i> Traffic</div><div class="tb-sub">Bandwidth usage analytics and monitoring</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh</button></div>
  </div>
  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> Total Traffic</div>
      <div class="traf-main-val" id="t-traffic">—<span class="m-unit">MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">Hourly Avg</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB per hour</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">Peak Usage</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">Highest hour</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">Lowest Usage</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB per hour</div></div>
    </div>
  </div>
  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> Traffic Trend</div>
        <div class="traf-chart-sub">Megabytes per hour</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> Usage</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> Average</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>

<!-- Connections -->
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div class="tb-left"><div class="tb-title"><i class="ti ti-plug-connected"></i> Active Connections</div><div class="tb-sub">Live IP and traffic monitoring per connection</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh</button></div>
  </div>
  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="conn-hero-label">Live Connections</div>
      <div class="conn-hero-val" id="ch-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-transfer"></i></div>
      <div class="conn-hero-label">Total Instant Traffic</div>
      <div class="conn-hero-val" id="ch-traffic">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-clock"></i></div>
      <div class="conn-hero-label">Avg Connection Time</div>
      <div class="conn-hero-val" id="ch-avgdur">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div>
      <div class="conn-hero-label">Unique IPs</div>
      <div class="conn-hero-val" id="ch-uniq">—</div>
    </div>
  </div>
  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> Connection List</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> Auto-refresh every 5s</div>
  </div>
  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">No active connections</div>
    <div class="conn-empty-v2-sub">Connected clients will appear here</div>
  </div>
</section>

<!-- Security -->
<section class="pg" id="pg-security">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-shield-lock"></i> Security</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-lock"></i> Encryption</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● Active (443)</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> Protocols</span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> Password Hash</span><span class="sr-v">SHA-256 + Salt</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> Session</span><span class="sr-v">HttpOnly · 7 days</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-shield-check"></i> Access Control</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> Strict UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● Active v9</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> Config Enable/Disable</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> Traffic Quota</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> Expiry Date</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> Sub Page Password</span><span class="sr-v" style="color:var(--green-t)">● Optional · SHA-256</span></div>
    </div>
  </div>
</section>

<!-- Logs -->
<section class="pg" id="pg-logs">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-history"></i> Activity Log</div><div class="tb-sub">Complete event history</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>No activity logged yet</p></div></div>
</section>

<!-- Errors -->
<section class="pg" id="pg-errors">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-alert-triangle"></i> Errors</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">0</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> Error Log</div><div id="errs-full">—</div></div>
</section>

<!-- WebSocket Test -->
<section class="pg" id="pg-testws">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-wifi"></i> WebSocket Test</div></div></div>
  <div class="card" style="max-width:700px">
    <div class="cl amber" style="margin-top:0;margin-bottom:14px"><i class="ti ti-alert-triangle"></i><span>Only registered and active UUIDs can connect (this tests VLESS/WS only; XHTTP must be tested from the client).</span></div>
    <div class="form-row" style="margin-bottom:14px">
      <div class="fg" style="flex:1"><label>UUID (must exist in configs)</label><input class="fi" id="ws-uuid" placeholder="UUID of an active config" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> Connect</button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> Disconnect</button>
    </div>
    <div class="form-row" style="margin-bottom:14px">
      <input class="fi" id="ws-msg" placeholder="Test message..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> Send</button>
    </div>
    <div style="background:rgba(0,0,0,0.05);border:1.5px solid var(--card-b);border-radius:14px;padding:16px;height:260px;overflow-y:auto;font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:11px;line-height:2" id="ws-log">
      <p style="color:var(--t3)">Waiting for connection...</p>
    </div>
  </div>
</section>

<!-- Settings -->
<section class="pg" id="pg-settings">
  <div class="topbar"><div class="tb-left"><div class="tb-title"><i class="ti ti-settings"></i> Settings</div></div></div>
  <div class="g2">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> Online · Railway</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Port</div><div class="srv-tile-val">443 (TLS)</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Version</div><div class="srv-tile-val">v1.0</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Framework</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Platform</div><div class="srv-tile-val">Railway</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Storage</div><div class="srv-tile-val">JSON File (/data)</div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">Change Password</div>
          <div class="pw-hero-sub">Choose a strong password and store it securely</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field">
          <label>Current Password</label>
          <input class="pw-input" type="password" id="cp-cur" placeholder="Enter current password">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field" style="margin-bottom:6px">
          <label>New Password</label>
          <input class="pw-input" type="password" id="cp-new" placeholder="Minimum 4 characters" oninput="checkPwStrength(this.value)">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-strength" id="pw-strength-bar">
          <div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div>
        </div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> Password Strength</div>
        <div class="pw-reqs">
          <span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> Min 4 characters</span>
          <span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> Includes digit</span>
          <span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> Upper/Lowercase</span>
        </div>
        <div class="pw-field" style="margin-bottom:20px">
          <label>Confirm New Password</label>
          <input class="pw-input" type="password" id="cp-cf" placeholder="Repeat new password">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
        </div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> Save New Password</button>
      </div>
    </div>
  </div>
</section>
</main>

<script>
var isDark=localStorage.getItem('sp-theme')==='dark';
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  var icon=document.getElementById('theme-icon'),label=document.getElementById('theme-label');
  icon.className='ti '+(dark?'ti-sun':'ti-moon');
  label.textContent=dark?'Light Mode':'Dark Mode';
  var mobI=document.getElementById('theme-mob-icon');if(mobI)mobI.className='ti '+(dark?'ti-sun':'ti-moon');
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
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> Expired</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> Unlimited</span>';
  var d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> Expired</span>';
  if(d<=3)return '<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> '+d+' days left</span>';
  return '<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> '+d+' days left</span>';
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
var prevTraf=0,ch1,ch2,ch3,currentSubId;
async function fetchStats(){
  try{
    var r=await authF('/stats'),d=await r.json();
    document.getElementById('m-conns').textContent=d.active_connections;
    document.getElementById('conns-nb').textContent=d.active_connections;
    document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    document.getElementById('m-alinks').textContent=d.active_links||'—';
    document.getElementById('m-lsub').textContent='of '+d.links_count+' configs';
    document.getElementById('m-subs').textContent=d.subs_count||'—';
    document.getElementById('errs-badge').textContent=d.total_errors+' Errors';
    document.getElementById('uptime-inline').textContent=d.uptime;
    document.getElementById('uptime-badge').textContent='Railway · '+d.uptime;
    document.getElementById('last-upd').textContent='Last update: '+new Date().toLocaleTimeString('en-US');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' connections';
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
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:12px;font-size:12.5px;display:flex;align-items:center;gap:6px"><i class="ti ti-circle-check"></i> No errors</div>';return}
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
    var kindFa={link:'Config',sub:'Group',auth:'Login',connection:'Connection',system:'System'};
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
    nlSub.innerHTML='<option value="">&mdash; No Group &mdash;</option>'+subs.map(function(s){return '<option value="'+esc(s.sub_id)+'">'+esc(s.name)+'</option>';}).join('');
    document.getElementById('links-nb').textContent=links.length;
    document.getElementById('links-pg-cnt').textContent=links.length+' Configs';
    document.getElementById('lsummary-badge').textContent=links.length;
    var grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!links.length){grid.innerHTML='';empty.style.display='block';document.getElementById('lsummary').innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>No configs</p></div>';return}
    empty.style.display='none';
    var subMap={};subs.forEach(function(s){subMap[s.sub_id]=s.name;});
    grid.innerHTML=links.map(function(l){
  var lim=l.limit_bytes===0?'&infin;':fmtB(l.limit_bytes);
  var pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
  var bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
  var allowed=l.active&&!l.expired;
  var cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
  return '<div class="cfg-card '+cardCls+'"><div class="cfg-row"><span class="cfg-status-dot '+(allowed?'pulse':'')+'"></span><div class="cfg-identity"><div class="cfg-label">'+esc(l.label)+'</div><div class="cfg-sub-meta"><span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText(\''+l.uuid+'\').then(function(){toast(\'UUID copied\',\'ok\');})" title="'+l.uuid+'"><i class="ti ti-fingerprint"></i> '+l.uuid.slice(0,10)+'&hellip;</span><span>'+new Date(l.created_at).toLocaleDateString('en-US')+'</span></div></div><div class="cfg-divider-v"></div><div class="cfg-usage-col"><div class="ubar"><div class="ubar-f" style="width:'+pct+'%;background:'+bc+'"></div></div><div class="utxt"><span>'+fmtB(l.used_bytes)+'</span><span>of '+lim+'</span></div></div><div class="cfg-divider-v"></div><div class="cfg-exp-col">'+expChip(l.expires_at,l.expired)+'</div><div class="cfg-divider-v"></div><div class="cfg-badges-col">'+protoBadge(l.protocol)+(l.sub_id&&allSubsList.find(function(s){return s.sub_id===l.sub_id;})?'<span class="cfg-sub-tag"><i class="ti ti-folder"></i> '+esc(allSubsList.find(function(s){return s.sub_id===l.sub_id;}).name)+'</span>':'')+'</div><div class="cfg-divider-v"></div><div class="cfg-actions"><button class="tog'+(allowed?' on':'')+'" onclick="toggleActive(\''+l.uuid+'\','+(!l.active)+')" title="Toggle"></button><button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText(\''+esc(l.vless_link)+'\').then(function(){toast(\'Link copied\',\'ok\');})" title="Copy Link"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText(\''+esc(l.sub_url)+'\').then(function(){toast(\'Sub copied\',\'ok\');})" title="Sub URL"><i class="ti ti-rss"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="showQR(\''+esc(l.vless_link)+'\')" title="QR"><i class="ti ti-qrcode"></i></button><button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink(\''+l.uuid+'\')" title="Edit"><i class="ti ti-edit"></i></button><button class="btn btn-sm btn-g btn-icon" onclick="resetUsage(\''+l.uuid+'\')" title="Reset Usage"><i class="ti ti-rotate"></i></button><button class="btn btn-sm btn-d btn-icon" onclick="deleteLink(\''+l.uuid+'\')" title="Delete"><i class="ti ti-trash"></i></button></div></div></div>';
}).join('');
    document.getElementById('lsummary').innerHTML=links.slice(0,6).map(function(l){return '<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti '+(l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x')+'" style="color:'+(l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)')+'"></i>'+esc(l.label)+'</span><span class="sr-v" style="font-size:10px">'+fmtB(l.used_bytes)+' / '+(l.limit_bytes===0?'&infin;':fmtB(l.limit_bytes))+'</span></div>';}).join('');
  }catch(e){console.error(e)}
}
async function createLink(){
  var label=document.getElementById('nl-label').value.trim()||'New Config';
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
    toast('Config created','ok');loadLinks();
  }catch(e){toast('Error creating config','err')}
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
    toast('Config updated','ok');loadLinks();
  }catch(e){toast('Error updating','err')}
}
async function toggleActive(uuid,newState){
  try{var r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'Activated':'Deactivated','ok');loadLinks();}catch(e){toast('Error','err')}
}
async function resetUsage(uuid){
  try{var r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('Usage reset','ok');loadLinks();}catch(e){toast('Error','err')}
}
async function deleteLink(uuid){
  if(!confirm('Delete this config?'))return;
  try{var r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('Deleted','ok');loadLinks();}catch(e){toast('Error','err')}
}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
var allSubsRaw=[];
async function loadSubs(){
  try{
    var r=await authF('/api/subs'),d=await r.json();
    var subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-nb').textContent=subs.length;
    document.getElementById('subs-pg-cnt').textContent=subs.length+' Groups';
    renderSubsGrid(subs);
  }catch(e){console.error(e)}
}
function renderSubsGrid(subs){
  var grid=document.getElementById('subs-grid');
  if(!subs.length){
    grid.innerHTML='<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">No groups yet</div><div class="subs-empty-v2-sub">Create a group to organize your configs</div></div>';
    return;
  }
  grid.innerHTML=subs.map(function(s){
    return '<div class="sub-card"><div class="sub-card-top"><div class="sub-card-head-v2"><div class="sub-card-icon"><i class="ti ti-folder"></i></div><div class="sub-card-titles"><div class="sub-card-name-v2">'+esc(s.name)+'</div>'+(s.desc?'<div class="sub-card-desc-v2">'+esc(s.desc)+'</div>':'<div class="sub-card-desc-v2" style="opacity:.5">No description</div>')+'</div><div class="sub-card-lock-badge '+(s.has_password?'locked':'open')+'" title="'+(s.has_password?'Password protected':'Public')+'"><i class="ti '+(s.has_password?'ti-lock':'ti-lock-open')+'"></i></div></div><div class="sub-card-stats"><div class="sub-card-stat"><div class="sub-card-stat-val">'+s.links_count+'</div><div class="sub-card-stat-label">Configs</div></div><div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">'+s.active_count+'</div><div class="sub-card-stat-label">Active</div></div><div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">'+esc(s.total_used_fmt)+'</div><div class="sub-card-stat-label">Usage</div></div></div></div><div class="sub-card-url-row"><span class="sub-card-url-text">'+esc(s.public_url)+'</span><button class="sub-card-url-copy" onclick="navigator.clipboard.writeText(\''+esc(s.public_url)+'\').then(function(){toast(\'Public link copied\',\'ok\');})" title="Copy"><i class="ti ti-copy"></i></button><button class="sub-card-url-copy" onclick="window.open(\''+esc(s.public_url)+'\',\'_blank\')" title="Open"><i class="ti ti-external-link"></i></button></div><div class="sub-card-bottom"><button class="btn btn-sm btn-g" onclick="openSubLinks(\''+esc(s.sub_id)+'\',\''+esc(s.name)+'\')"><i class="ti ti-link-plus"></i> Configs</button><button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText(\''+esc(s.sub_url)+'\').then(function(){toast(\'Sub link copied\',\'ok\');})"><i class="ti ti-rss"></i> Sub</button><button class="btn btn-sm btn-g btn-icon" onclick="showQR(\''+esc(s.sub_url)+'\')" title="QR"><i class="ti ti-qrcode"></i></button><button class="btn btn-sm btn-d btn-icon" onclick="deleteSub(\''+esc(s.sub_id)+'\')" title="Delete"><i class="ti ti-trash"></i></button></div></div>';
  }).join('');
}
function filterSubs(q){
  q=q.trim().toLowerCase();
  if(!q){renderSubsGrid(allSubsRaw);return}
  renderSubsGrid(allSubsRaw.filter(function(s){return s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q);}));
}
async function createSub(){
  var name=document.getElementById('ns-name').value.trim()||'New Group';
  var desc=document.getElementById('ns-desc').value.trim();
  var pw=document.getElementById('ns-pw').value;
  try{
    var r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:name,desc:desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(function(id){document.getElementById(id).value='';});
    closeModal('modal-create-sub');
    toast('Group created','ok');loadSubs();
  }catch(e){toast('Error creating group','err')}
}
async function deleteSub(sub_id){
  if(!confirm('Delete this group? Configs will not be deleted.'))return;
  try{var r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('Group deleted','ok');loadSubs();loadLinks();}catch(e){toast('Error','err')}
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
  }catch(e){toast('Error loading','err')}
}
function renderLmodalList(links){
  var body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div class="empty" style="padding:36px"><i class="ti ti-link-off"></i><p>No configs yet</p></div>';updateLmodalCount();return}
  body.innerHTML=links.map(function(l){
    var checked=lmodalInSub.has(l.uuid);
    var on=l.active&&!l.expired;
    return '<div class="lrow-v2 '+(checked?'checked':'')+'" data-uuid="'+l.uuid+'" data-name="'+esc(l.label).toLowerCase()+'" onclick="toggleLrow(\''+l.uuid+'\',this)"><div class="lrow-v2-check"><i class="ti ti-check"></i></div><div class="lrow-v2-avatar"><i class="ti ti-key"></i></div><div class="lrow-v2-info"><div class="lrow-v2-name">'+esc(l.label)+'</div><div class="lrow-v2-meta"><i class="ti ti-database" style="font-size:10px"></i> '+fmtB(l.used_bytes)+'</div></div><span class="lrow-v2-status '+(on?'on':'off')+'">'+(on?'Active':'Inactive')+'</span></div>';
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
  if(el)el.textContent=lmodalInSub.size+' selected';
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
    toast('Group configs saved','ok');
    loadSubs();loadLinks();
  }catch(e){toast('Error saving','err')}
}
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  try{
    var r=await authF('/api/subs'),d=await r.json();
    var subs=d.subs||[];
    var el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>No groups yet</p></div>';return}
    el.innerHTML=subs.map(function(s){
      return '<div style="padding:15px 17px;background:var(--accent-d);border:1px solid var(--card-b);border-radius:16px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap"><div><div style="font-weight:700;font-size:13.5px;margin-bottom:3px">'+esc(s.name)+'</div><div style="font-family:\'SF Mono\',\'Fira Code\',ui-monospace,monospace;font-size:10.5px;color:var(--purple)">'+esc(s.sub_url)+'</div><div style="font-size:10px;color:var(--t3);margin-top:3px">'+s.links_count+' configs &middot; '+esc(s.total_used_fmt)+' usage'+(s.has_password?' &middot; &#128274; Password':'' )+'</div></div><div style="display:flex;gap:6px;flex-wrap:wrap"><button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText(\''+esc(s.sub_url)+'\').then(function(){toast(\'Copied\',\'ok\');})"><i class="ti ti-copy"></i> Sub</button><button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText(\''+esc(s.public_url)+'\').then(function(){toast(\'Copied\',\'ok\');})"><i class="ti ti-globe"></i> Public</button><button class="btn btn-sm btn-g" onclick="showQR(\''+esc(s.sub_url)+'\')"><i class="ti ti-qrcode"></i></button></div></div>';
    }).join('');
  }catch(e){}
}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(function(){toast('Copied','ok');})}
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
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.count+' connections';
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
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+'s':avgSec<3600?Math.floor(avgSec/60)+'m':Math.floor(avgSec/3600)+'h';
    var maxDur=Math.max.apply(null,durs.concat([1]));
    grid.innerHTML=conns.map(function(c){
      var secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      var dur=secs<60?secs+' seconds':secs<3600?Math.floor(secs/60)+' minutes':Math.floor(secs/3600)+' hours';
      var durPct=Math.min(100,Math.round((secs/maxDur)*100));
      var protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');
      return '<div class="conn-card-v2"><div class="conn-card-v2-glow"></div><div class="conn-card-v2-top"><div class="conn-avatar"><i class="ti ti-device-desktop"></i></div><div class="conn-card-v2-id"><div class="conn-ip-v2">'+esc(c.ip)+'<button class="conn-ip-copy" onclick="navigator.clipboard.writeText(\''+esc(c.ip)+'\').then(function(){toast(\'IP copied\',\'ok\');})" title="Copy IP"><i class="ti ti-copy"></i></button></div><div class="conn-label-v2">'+esc(c.label)+'</div></div><span class="conn-status-pill"><span class="dot dg pulse"></span> Live</span></div><div class="conn-card-v2-divider"></div><div class="conn-card-v2-body"><div class="conn-proto-row">'+protoBadge(protoVal)+'</div><div class="conn-stat-row"><div class="conn-stat-box"><div class="conn-stat-icon"><i class="ti ti-transfer"></i></div><div><div class="conn-stat-text-label">Traffic</div><div class="conn-stat-text-val">'+esc(c.bytes_fmt)+'</div></div></div><div class="conn-stat-box"><div class="conn-stat-icon time"><i class="ti ti-clock"></i></div><div><div class="conn-stat-text-label">Duration</div><div class="conn-stat-text-val">'+dur+'</div></div></div></div><div class="conn-duration-track"><div class="conn-duration-fill" style="width:'+durPct+'%"></div></div></div></div>';
    }).join('');
  }catch(e){console.error(e)}
}
async function loadErrs(){try{var r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}
async function fetchDefaultVless(){
  try{var r=await authF('/api/links'),d=await r.json();var links=d.links||[];var def=links.find(function(l){return l.limit_bytes===0&&l.active&&!l.expired;})||links.find(function(l){return l.active&&!l.expired;})||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'No configs yet';}catch(e){}
}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(function(){toast('Copied','ok');})}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('Refreshed','ok')}
async function changePw(){
  var cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;
  if(!cur||!nw||!cf){toast('Fill all fields','err');return}
  if(nw.length<4){toast('Min 4 characters','err');return}
  if(nw!==cf){toast('Passwords do not match','err');return}
  try{
    var r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});
    var d=await r.json().catch(function(){return{};});
    if(!r.ok)throw new Error(d.detail||'Error');
    toast('Password changed','ok');
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
  var colors=['#EF4444','#F59E0B','#3B82F6','#16A34A'],labels=['Very Weak','Weak','Medium','Strong'];
  segs.forEach(function(s,i){s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,116,139,.2)';});
  if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> Password Strength';return}
  label.innerHTML='<i class="ti ti-shield-check" style="color:'+colors[Math.max(0,score-1)]+'"></i> '+labels[Math.max(0,score-1)];
}
function makeGradient(ctx,color1,color2){
  var g=ctx.createLinearGradient(0,0,0,260);
  g.addColorStop(0,color1);g.addColorStop(1,color2);
  return g;
}
function initCharts(){
  var c1ctx=document.getElementById('ch1').getContext('2d');
  var grad1=makeGradient(c1ctx,'rgba(43,127,255,.35)','rgba(43,127,255,0)');
  var opts={
    responsive:true,maintainAspectRatio:false,
    interaction:{mode:'index',intersect:false},
    plugins:{
      legend:{display:false},
      tooltip:{
        backgroundColor:'rgba(15,23,42,.97)',borderColor:'rgba(43,127,255,.3)',borderWidth:1,
        titleColor:'#F1F5F9',bodyColor:'#94A3B8',padding:12,cornerRadius:12,displayColors:false,
        titleFont:{family:'Inter',size:11,weight:'700'},bodyFont:{family:'Inter',size:11},
        callbacks:{label:function(v){return v.parsed.y.toFixed(2)+' MB';}}
      }
    },
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:'#64748B',font:{size:9,family:'Inter'}}},
      y:{grid:{color:'rgba(43,127,255,.05)'},border:{display:false},ticks:{color:'#64748B',font:{size:9,family:'Inter'},callback:function(v){return v+' MB';}}}
    },
    elements:{line:{capBezierPoints:true}}
  };
  var ds1={label:'MB',data:[],borderColor:'#2B7FFF',backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:'#2B7FFF',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5};
  ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[ds1]},options:opts});

  function makeGradientV2(ctx,c1,c2,c3){
    var g=ctx.createLinearGradient(0,0,0,340);
    g.addColorStop(0,c1);g.addColorStop(.6,c2);g.addColorStop(1,c3);
    return g;
  }
  var c3ctx=document.getElementById('ch3').getContext('2d');
  var gradFill3=makeGradientV2(c3ctx,'rgba(43,127,255,.4)','rgba(43,127,255,.06)','rgba(43,127,255,0)');
  ch3=new Chart(document.getElementById('ch3'),{
    type:'line',
    data:{labels:[],datasets:[
      {label:'Usage',data:[],borderColor:'#2B7FFF',backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#2B7FFF',pointHoverBorderWidth:3,borderWidth:3,order:2},
      {label:'Average',data:[],borderColor:'#F59E0B',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}
    ]},
    options:{
      responsive:true,maintainAspectRatio:false,
      interaction:{mode:'index',intersect:false},
      plugins:{
        legend:{display:false},
        tooltip:{
          backgroundColor:'rgba(15,23,42,.97)',borderColor:'rgba(43,127,255,.35)',borderWidth:1,
          titleColor:'#F1F5F9',bodyColor:'#94A3B8',padding:14,cornerRadius:12,displayColors:true,boxPadding:4,
          titleFont:{family:'Inter',size:12,weight:'700'},bodyFont:{family:'Inter',size:11},
          callbacks:{label:function(v){return ' '+v.dataset.label+': '+v.parsed.y.toFixed(2)+' MB';}}
        }
      },
      scales:{
        x:{grid:{display:false},border:{display:false},ticks:{color:'#64748B',font:{size:9.5,family:'Inter'},maxRotation:0}},
        y:{grid:{color:'rgba(43,127,255,.04)'},border:{display:false},ticks:{color:'#64748B',font:{size:9.5,family:'Inter'},callback:function(v){return v+' MB';}}}
      }
    }
  });

  var cardBg=getComputedStyle(document.documentElement).getPropertyValue('--card')||'#FFFFFF';
  ch2=new Chart(document.getElementById('ch2'),{
    type:'doughnut',
    data:{labels:['VLESS/WS','XHTTP Ultra','HTTP Proxy'],datasets:[{
      data:[55,35,10],
      backgroundColor:['#2B7FFF','#16A34A','#7B61FF'],
      borderColor:cardBg,
      borderWidth:4,hoverOffset:12,borderRadius:7,spacing:4
    }]},
    options:{
      responsive:true,maintainAspectRatio:false,cutout:'70%',
      plugins:{
        legend:{position:'bottom',labels:{color:'var(--t2)',font:{size:10,family:'Inter'},padding:14,usePointStyle:true,pointStyle:'circle'}},
        tooltip:{backgroundColor:'rgba(15,23,42,.97)',borderColor:'rgba(43,127,255,.3)',borderWidth:1,padding:11,cornerRadius:11,bodyFont:{family:'Inter'},titleFont:{family:'Inter'}}
      }
    }
  });
}
var ws;
function wsLog(c,m){var l=document.getElementById('ws-log'),p=document.createElement('p');var colors={ok:'#4ADE80',err:'#FCA5A5',info:'#94A3B8',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('en-US')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){var u=document.getElementById('ws-uuid').value.trim();if(!u){toast('Enter UUID','err');return}var url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','Connecting: '+url);ws=new WebSocket(url);ws.onopen=function(){wsLog('ok','✓ Connected - Valid UUID');};ws.onerror=function(){wsLog('err','✗ Error - Invalid or inactive UUID');};ws.onmessage=function(m){wsLog('info','Received '+(m.data.size||m.data.length)+' bytes');};ws.onclose=function(e){wsLog('err','Disconnected ('+e.code+')'+(e.code===1008?' - Access denied':''));}}
function wsSend(){var m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','Sent: '+m);document.getElementById('ws-msg').value=''}
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
    """Public sub page v3 — SPIDER PANEL Enterprise design"""
    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>SPIDER PANEL · Sub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Vazirmatn:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{
  --bg:#F8FAFC;--bg2:#F1F5F9;--bg3:#E2E8F0;
  --card:rgba(255,255,255,0.75);--card-b:rgba(43,127,255,0.1);--card-bh:rgba(43,127,255,0.25);
  --accent:#2B7FFF;--accent2:#7B61FF;--accent-d:rgba(43,127,255,0.08);
  --green:#16A34A;--green-bg:rgba(22,163,74,0.08);--green-t:#166534;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#991B1B;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-t:#92400E;
  --purple:#7B61FF;--purple-bg:rgba(123,97,255,0.08);--purple-t:#5B21B6;
  --t1:#0F172A;--t2:#334155;--t3:#64748B;
  --radius:24px;--shadow:0 4px 30px rgba(0,0,0,0.08);
  --font:'Inter',sans-serif;
  --gradient:linear-gradient(90deg,#2B7FFF,#7B61FF,#FF2352);
}}
[data-theme="dark"]{{
  --bg:#0B1120;--bg2:#111827;--bg3:#1E293B;
  --card:rgba(17,24,39,0.8);--card-b:rgba(43,127,255,0.12);--card-bh:rgba(43,127,255,0.25);
  --accent:#3B82F6;--accent2:#8B7CFF;--accent-d:rgba(59,130,246,0.1);
  --green:#22C55E;--green-bg:rgba(34,197,94,0.1);--green-t:#4ADE80;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#FCA5A5;
  --amber:#FBBF24;--amber-bg:rgba(251,191,36,0.1);--amber-t:#FCD34D;
  --purple:#A78BFA;--purple-bg:rgba(167,139,250,0.1);--purple-t:#C4B5FD;
  --t1:#F1F5F9;--t2:#94A3B8;--t3:#64748B;
  --shadow:0 4px 30px rgba(0,0,0,0.3);
}}
html,body{{min-height:100%;background:var(--bg);font-family:var(--font);color:var(--t1);font-size:14px;transition:background .35s,color .35s}}
.bg-blobs{{position:fixed;inset:0;z-index:0;overflow:hidden;pointer-events:none}}
.bg-blob{{position:absolute;border-radius:50%;filter:blur(120px);animation:blobDrift 15s ease-in-out infinite}}
.bg-blob.b1{{width:600px;height:600px;background:rgba(43,127,255,0.06);top:-150px;left:-150px}}
.bg-blob.b2{{width:500px;height:500px;background:rgba(123,97,255,0.04);bottom:-120px;right:-120px;animation-delay:5s}}
@keyframes blobDrift{{0%,100%{{transform:translate(0,0) scale(1)}}33%{{transform:translate(30px,-30px) scale(1.1)}}66%{{transform:translate(-20px,20px) scale(0.9)}}}}
.wrap{{position:relative;z-index:10;max-width:880px;margin:0 auto;padding:28px 18px 70px}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:28px;gap:10px}}
.brand{{display:flex;align-items:center;gap:12px;min-width:0}}
.brand-svg{{width:42px;height:42px;flex-shrink:0}}
.brand-name{{font-size:16px;font-weight:800;letter-spacing:-.01em;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.brand-sub{{font-size:10px;color:var(--t3);font-weight:500}}
.top-actions{{display:flex;align-items:center;gap:7px;flex-shrink:0}}
.icon-btn{{width:38px;height:38px;border-radius:13px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:17px;cursor:pointer;transition:.18s;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}}
.icon-btn:hover{{background:var(--accent-d);color:var(--accent);border-color:var(--card-bh)}}
.sub-info{{background:var(--card);border:1px solid var(--card-b);border-radius:24px;padding:28px;margin-bottom:18px;position:relative;overflow:hidden;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}}
.sub-info::before{{content:'';position:absolute;top:0;right:0;width:180px;height:180px;background:radial-gradient(circle at top right,rgba(43,127,255,0.08),transparent 70%);pointer-events:none}}
.sub-eyebrow{{font-size:10.5px;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:.12em;margin-bottom:10px;display:flex;align-items:center;gap:7px}}
.sub-name{{font-size:24px;font-weight:800;color:var(--t1);margin-bottom:8px;letter-spacing:-.02em}}
.sub-desc{{font-size:13px;color:var(--t2);line-height:1.8;margin-bottom:16px}}
.sub-meta-row{{font-size:11px;color:var(--t3);margin-bottom:16px;display:flex;align-items:center;gap:7px}}
.sub-sub-box{{background:var(--accent-d);border:1px solid var(--card-b);border-radius:16px;padding:14px 16px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}}
.sub-sub-url{{font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:10.5px;color:var(--accent);word-break:break-all;flex:1;min-width:140px}}
.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:20px}}
.stat-card{{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:20px;transition:.25s;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}}
.stat-card:hover{{border-color:var(--card-bh);transform:translateY(-2px)}}
.stat-label{{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:8px}}
.stat-val{{font-size:24px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.01em}}
.stat-sub{{font-size:10.5px;color:var(--t3);margin-top:7px}}
.copy-all-bar{{display:flex;align-items:center;gap:14px;background:var(--gradient);border-radius:20px;padding:18px 22px;margin-bottom:20px;flex-wrap:wrap}}
.copy-all-text{{flex:1;min-width:160px}}
.copy-all-title{{font-size:14px;font-weight:800;color:#fff;display:flex;align-items:center;gap:7px}}
.copy-all-sub{{font-size:10.5px;color:rgba(255,255,255,.75);margin-top:3px}}
.copy-all-btn{{background:#fff;color:#1D4ED8;border:none;border-radius:14px;padding:11px 22px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:7px;transition:.18s;white-space:nowrap}}
.copy-all-btn:hover{{transform:translateY(-2px);box-shadow:0 6px 18px rgba(0,0,0,.2)}}
.cfg-title{{font-size:13px;font-weight:800;color:var(--t2);margin-bottom:14px;display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.07em}}
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
.ubar{{height:7px;border-radius:5px;background:rgba(43,127,255,0.08);overflow:hidden;margin-bottom:6px}}
.ubar-f{{height:100%;border-radius:5px;transition:width .5s ease}}
.utxt{{font-size:10.5px;color:var(--t3);display:flex;justify-content:space-between}}
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 22px}}
.cfg-tear::before,.cfg-tear::after{{content:'';position:absolute;top:50%;width:20px;height:20px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-b)}}
.cfg-tear::before{{right:-30px}}
.cfg-tear::after{{left:-30px}}
.cfg-bottom{{padding:18px 22px 20px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1.5px dashed var(--card-b);border-radius:14px;padding:11px 15px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:12px;font-weight:600;transition:.15s}}
.cfg-link-toggle:hover{{background:var(--accent-d);border-color:var(--card-bh);color:var(--accent)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,0.03);border:1px solid var(--card-b);border-radius:12px;padding:12px 15px;font-size:10px;font-family:'SF Mono','Fira Code',ui-monospace,monospace;color:var(--accent);word-break:break-all;line-height:1.8;margin-top:10px;max-height:100px;overflow-y:auto}}
[data-theme="dark"] .cfg-vless{{background:rgba(0,0,0,0.2)}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap;margin-top:12px}}
.btn{{font-family:inherit;font-size:12px;font-weight:700;border-radius:14px;padding:9px 17px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border:none;transition:all .18s;white-space:nowrap}}
.btn i{{font-size:14px}}
.btn-p{{background:var(--accent);color:#fff;box-shadow:0 3px 14px rgba(43,127,255,0.3)}}
.btn-p:hover{{background:#2563EB;box-shadow:0 5px 20px rgba(43,127,255,0.4);transform:translateY(-1px)}}
.btn-g{{background:var(--accent-d);color:var(--accent);border:1px solid rgba(43,127,255,0.12)}}
.btn-g:hover{{background:rgba(43,127,255,0.18)}}
.btn-pur{{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(123,97,255,0.15)}}
.btn-pur:hover{{background:rgba(123,97,255,0.2)}}
.conn-chip{{display:inline-flex;align-items:center;gap:5px;font-size:9.5px;padding:4px 9px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-weight:700}}
.dot{{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:75vh;padding:20px 0}}
.lock-card{{background:var(--card);border:1px solid var(--card-b);border-radius:28px;padding:0;text-align:center;max-width:400px;width:100%;overflow:hidden;position:relative;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}}
.lock-banner{{background:linear-gradient(150deg,rgba(43,127,255,0.1),rgba(123,97,255,0.03) 70%);padding:44px 32px 30px;position:relative}}
.lock-shield{{width:70px;height:70px;border-radius:20px;background:var(--accent-d);border:1px solid var(--card-bh);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-8px;border-radius:24px;border:1px solid var(--card-b);animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.5}}50%{{transform:scale(1.08);opacity:0}}}}
.lock-shield i{{font-size:30px;color:var(--accent)}}
.lock-title{{font-size:19px;font-weight:800;margin-bottom:7px;color:var(--t1);letter-spacing:-.01em}}
.lock-sub{{font-size:12.5px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:26px 34px 34px}}
.lock-field{{position:relative;margin-bottom:14px}}
.lock-inp{{width:100%;padding:14px 46px;border-radius:16px;border:1.5px solid var(--card-b);background:rgba(0,0,0,0.03);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.14em;transition:.18s}}
[data-theme="dark"] .lock-inp{{background:rgba(0,0,0,0.15)}}
.lock-inp:focus{{border-color:var(--accent);box-shadow:0 0 0 4px var(--accent-d)}}
.lock-eye{{position:absolute;right:14px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:17px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--accent)}}
.lock-lockicon{{position:absolute;left:15px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:16px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:12px;margin-bottom:10px;min-height:18px;display:flex;align-items:center;justify-content:center;gap:5px}}
.lock-btn{{width:100%;justify-content:center;padding:14px;font-size:14px;border-radius:16px}}
.lock-footer{{padding:16px 34px;border-top:1px solid var(--card-b);font-size:10.5px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:7px}}
.empty-state{{text-align:center;padding:90px 20px;color:var(--t3)}}
.empty-state i{{font-size:40px;display:block;margin-bottom:16px}}
.toast{{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:14px;padding:12px 22px;font-size:13px;font-weight:600;opacity:0;transition:all .3s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap;backdrop-filter:blur(20px)}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(22,163,74,0.3);background:var(--green-bg);color:var(--green-t)}}
.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--card);border:1px solid var(--card-b);border-radius:24px;padding:28px;text-align:center;max-width:360px;width:100%;backdrop-filter:blur(20px)}}
.qr-title{{font-size:14px;font-weight:800;margin-bottom:18px;color:var(--t1)}}
.qr-img{{border-radius:16px;overflow:hidden;margin-bottom:16px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:12px;border-radius:16px}}
.footer{{text-align:center;padding-top:30px;font-size:11px;color:var(--t3)}}
.footer a{{color:var(--accent);font-weight:700;text-decoration:none}}
@media(max-width:520px){{
  .stats-bar{{grid-template-columns:1fr 1fr}}
  .stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}
  .sub-name{{font-size:20px}}
  .copy-all-bar{{flex-direction:column;align-items:stretch}}
  .copy-all-btn{{justify-content:center}}
  .wrap{{padding:18px 14px 56px}}
  .lock-banner{{padding:36px 24px 24px}}
  .lock-form{{padding:22px 24px 28px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
</style>
</head>
<body>
<div class="bg-blobs"><div class="bg-blob b1"></div><div class="bg-blob b2"></div></div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> Close</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <svg class="brand-svg" viewBox="0 0 48 48" fill="none"><circle cx="24" cy="24" r="22" stroke="url(#pubGrad)" stroke-width="1.5"/><defs><linearGradient id="pubGrad" x1="0" y1="0" x2="48" y2="48"><stop stop-color="#2B7FFF"/><stop offset="0.5" stop-color="#7B61FF"/><stop offset="1" stop-color="#FF2352"/></linearGradient></defs><path d="M24 6L26 22L42 24L26 26L24 42L22 26L6 24L22 22Z" fill="url(#pubGrad)" opacity="0.9"/><circle cx="24" cy="24" r="3.5" fill="url(#pubGrad)"/></svg>
      <div><div class="brand-name">SPIDER PANEL</div><div class="brand-sub">Enterprise Network Management</div></div>
    </div>
    <div class="top-actions">
      <button class="icon-btn" id="theme-toggle" onclick="toggleTheme()" title="Toggle theme"><i class="ti ti-sun" id="theme-icon"></i></button>
      <a class="icon-btn" href="https://t.me/CodeBoxo" target="_blank" title="Telegram"><i class="ti ti-brand-telegram"></i></a>
    </div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>Loading...</div>
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
  btn.querySelector('.ltl span').textContent = open ? 'Hide Link' : 'Show Link';
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
    '<div class="lock-stage"><div class="lock-card"><div class="lock-banner"><div class="lock-shield"><i class="ti ti-shield-lock"></i></div><div class="lock-title">'+esc(name)+'</div><div class="lock-sub">This group is password-protected. Enter the password to view configs.</div></div><div class="lock-form"><div class="lock-err" id="lock-err">'+(errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : '')+'</div><div class="lock-field"><i class="ti ti-lock lock-lockicon"></i><input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus><button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button></div><button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> Unlock Group</button></div><div class="lock-footer"><i class="ti ti-shield-check"></i> Connection is encrypted</div></div></div>';
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
  if(data.locked){{renderLock(data.name,'Incorrect password');return}}
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
  document.getElementById('root').innerHTML=
    '<div class="sub-info"><div class="sub-eyebrow"><i class="ti ti-folders"></i> Access Group</div><div class="sub-name">'+esc(d.name)+'</div>'+
    (d.desc ? '<div class="sub-desc">'+esc(d.desc)+'</div>' : '')+
    '<div class="sub-meta-row"><i class="ti ti-clock"></i> Last update: '+new Date().toLocaleTimeString('en-US')+'</div>'+
    '<div class="sub-sub-box"><span class="sub-sub-url">'+esc(subUrl)+'</span>'+
    '<button class="btn btn-pur" style="padding:8px 14px;font-size:11px" onclick="navigator.clipboard.writeText(window._rvgSubUrl).then(function(){{toast(\'Sub link copied\',\'ok\');}})"><i class="ti ti-copy"></i> Copy Sub</button>'+
    '<button class="btn btn-g" style="padding:8px 14px;font-size:11px" onclick="showQR(window._rvgSubName + \' — All\', window._rvgSubUrl)"><i class="ti ti-qrcode"></i> QR All</button></div></div>'+
    '<div class="copy-all-bar"><div class="copy-all-text"><div class="copy-all-title"><i class="ti ti-copy"></i> Copy All Configs</div><div class="copy-all-sub">Copy all active links from this group at once</div></div>'+
    '<button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> Copy All ('+activeCount+')</button></div>'+
    '<div class="stats-bar"><div class="stat-card"><div class="stat-label">Active Configs</div><div class="stat-val">'+activeCount+'</div><div class="stat-sub">of '+d.links.length+' configs</div></div>'+
    '<div class="stat-card"><div class="stat-label">Live Connections</div><div class="stat-val">'+d.active_connections+'</div><div class="stat-sub" style="color:var(--green-t);display:flex;align-items:center;gap:5px"><span class="dot"></span> Online</div></div>'+
    '<div class="stat-card"><div class="stat-label">Total Usage</div><div class="stat-val" style="font-size:18px;margin-top:3px">'+esc(d.total_used_fmt)+'</div><div class="stat-sub">All configs</div></div></div>'+
    '<div class="cfg-title"><i class="ti ti-link"></i> Configs ('+d.links.length+' items)</div>'+
    '<div class="cfg-grid">'+
    d.links.map(function(l, i) {{
      var pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
      var bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
      var lim = l.limit_bytes === 0 ? '&infin;' : fmtB(l.limit_bytes);
      return '<div class="cfg-card'+(l.active ? '' : ' inactive')+'"><div class="cfg-top"><div class="cfg-head"><div><div class="cfg-label">'+esc(l.label)+'</div><div class="cfg-badges">'+protoChip(l.protocol)+
        (l.connections > 0 ? '<span class="conn-chip"><span class="dot"></span> '+l.connections+' connections</span>' : '')+
        '</div></div><span class="cfg-status '+(l.active ? 'ok' : 'no')+'">'+(l.active ? '<i class="ti ti-circle-check"></i> Active' : '<i class="ti ti-circle-x"></i> Inactive')+'</span></div>'+
        '<div class="cfg-usage"><div class="ubar"><div class="ubar-f" style="width:'+pct+'%;background:'+bc+'"></div></div><div class="utxt"><span>'+esc(l.used_fmt)+' used</span><span>Quota: '+lim+'</span></div></div></div>'+
        '<div class="cfg-tear"></div><div class="cfg-bottom"><button class="cfg-link-toggle" id="vt-'+i+'" onclick="toggleLink('+i+')"><span class="ltl"><i class="ti ti-eye"></i> <span>Show Link</span></span><i class="ti ti-chevron-down"></i></button>'+
        '<div class="cfg-vless-wrap" id="vw-'+i+'"><div class="cfg-vless-inner"><div class="cfg-vless">'+esc(l.vless_link)+'</div></div></div>'+
        '<div class="cfg-actions"><button class="btn btn-p" onclick="navigator.clipboard.writeText(window._rvgLinks['+i+'].vless).then(function(){{toast(\'Link copied\',\'ok\');}})"><i class="ti ti-copy"></i> Copy Link</button>'+
        '<button class="btn btn-g" onclick="showQR(window._rvgLinks['+i+'].label, window._rvgLinks['+i+'].vless)"><i class="ti ti-qrcode"></i> QR</button></div></div></div>';
    }}).join('')+'</div>';
  setTimeout(function() {{ autoRefresh(); }}, 30000);
}}
function copyAllConfigs(){{
  var links=window._rvgLinks||[];
  if(!links.length){{toast('No configs to copy','');return}}
  var text=links.map(function(l){{return l.vless;}}).join('\\n');
  navigator.clipboard.writeText(text).then(function(){{toast('All '+links.length+' configs copied','ok');}});
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
    document.getElementById('root').innerHTML = '<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>Error loading data</div>';
  }}
}}
init();
</script>
</body></html>"""
