# pages.py - پنل عقاب (Eagle Panel) با صفحه ساب‌لینک

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · پنل عقاب</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0a0a0f;--card:rgba(20,20,35,0.85);--accent:#3B82F6;--accent2:#60A5FA;--text:#F0F0FF;--dim:#4A4A6A;--mid:#8A8AAA;--border:rgba(59,130,246,0.2)}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px}
.bg{position:fixed;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(59,130,246,0.08),transparent 70%),var(--bg);z-index:0}
.orb{position:fixed;border-radius:50%;filter:blur(100px);z-index:0;animation:fl 10s ease-in-out infinite}
.o1{width:350px;height:350px;background:rgba(59,130,246,0.06);top:-120px;right:-100px}
.o2{width:250px;height:250px;background:rgba(139,92,246,0.04);bottom:-80px;left:-80px;animation-delay:5s}
@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-20px)}}
.wrap{position:relative;z-index:10;width:100%;max-width:400px}
.card{background:var(--card);border:1px solid var(--border);border-radius:24px;padding:40px 34px 34px;backdrop-filter:blur(24px);box-shadow:0 0 80px rgba(59,130,246,0.05),0 20px 60px rgba(0,0,0,.5)}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:28px}
.brand-icon{width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#3B82F6,#8B5CF6);display:flex;align-items:center;justify-content:center;font-size:26px;flex-shrink:0;box-shadow:0 0 30px rgba(59,130,246,0.2)}
.brand-name{font-size:18px;font-weight:800;color:var(--text)}
.brand-sub{font-size:11px;color:var(--dim);margin-top:2px}
h1{font-size:21px;font-weight:700;color:var(--text);margin-bottom:5px}
.sub{font-size:12px;color:var(--mid);margin-bottom:24px;line-height:1.6}
.hint{display:flex;align-items:center;gap:10px;background:rgba(59,130,246,0.06);border:1px solid rgba(59,130,246,0.12);border-radius:10px;padding:10px 14px;margin-bottom:20px}
.hint-label{font-size:11px;color:var(--dim);flex:1}
.hint-val{font-family:ui-monospace,monospace;font-size:14px;font-weight:700;color:var(--accent);background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.2);padding:3px 11px;border-radius:7px;cursor:pointer}
.hint-val:hover{background:rgba(59,130,246,0.2)}
.field{margin-bottom:18px}
.field label{display:block;font-size:10.5px;font-weight:600;color:var(--mid);margin-bottom:7px;text-transform:uppercase;letter-spacing:.06em}
.inp-wrap{position:relative}
input[type=password]{width:100%;padding:13px 44px 13px 16px;border-radius:11px;border:1px solid var(--border);background:rgba(0,0,0,.3);color:var(--text);font-family:inherit;font-size:14px;outline:none;transition:.2s}
input[type=password]:focus{border-color:rgba(59,130,246,.5);background:rgba(0,0,0,.4);box-shadow:0 0 0 3px rgba(59,130,246,.08)}
.ic{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--dim);font-size:18px;pointer-events:none}
input:focus+.ic{color:var(--accent)}
.err{display:none;background:rgba(239,68,68,.08);border:1px solid rgba(239,68,68,.2);border-radius:10px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:#F87171;align-items:center;gap:8px}
.err.show{display:flex}
.btn{width:100%;padding:13px;border-radius:11px;border:none;cursor:pointer;background:linear-gradient(135deg,#3B82F6,#8B5CF6);color:#fff;font-family:inherit;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 4px 20px rgba(59,130,246,.3);transition:.2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(59,130,246,.4)}
.btn:disabled{opacity:.5;cursor:not-allowed;transform:none}
.footer{margin-top:22px;padding-top:18px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11px;color:var(--dim)}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<div class="bg"></div>
<div class="orb o1"></div><div class="orb o2"></div>
<div class="wrap">
  <div class="card">
    <div class="brand">
      <div class="brand-icon">🦅</div>
      <div><div class="brand-name">پنل عقاب</div><div class="brand-sub">مدیریت کاربران</div></div>
    </div>
    <h1>ورود به پنل عقاب</h1>
    <p class="sub">رمز عبور را برای دسترسی به داشبورد وارد کنید</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="hint">
      <span class="hint-label">رمز پیش‌فرض</span>
      <span class="hint-val" onclick="document.getElementById('pw').value='123456';document.getElementById('pw').focus()">123456</span>
    </div>
    <form id="form">
      <div class="field">
        <label>رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required>
          <i class="ti ti-lock ic"></i>
        </div>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به پنل</button>
    </form>
    <div class="footer">🦅 پنل عقاب · v9.2</div>
  </div>
</div>
<script>
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به پنل';
  }
});
</script>
</body></html>"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>پنل عقاب · مدیریت کاربران</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0a0a0f;--bg2:#111122;--bg3:#181830;
  --card:#0d0d1a;--card-b:rgba(59,130,246,0.12);--card-bh:rgba(59,130,246,0.28);
  --accent:#3B82F6;--accent2:#60A5FA;--accent-d:rgba(59,130,246,0.08);
  --green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-t:#34D399;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-t:#F87171;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-t:#FCD34D;
  --purple:#8B5CF6;--purple-bg:rgba(139,92,246,0.08);
  --t1:#F0F0FF;--t2:#8A8AAA;--t3:#4A4A6A;
  --sidebar-w:220px;--radius:14px;
  --shadow:0 4px 24px rgba(0,0,0,0.35);
}
[data-theme="light"]{
  --bg:#F0F2F8;--bg2:#E4E8F4;--bg3:#D5DDF0;
  --card:#FFFFFF;--card-b:rgba(59,130,246,0.14);--card-bh:rgba(59,130,246,0.3);
  --accent:#2563EB;--accent2:#1D4ED8;--accent-d:rgba(37,99,235,0.08);
  --green:#059669;--green-bg:rgba(5,150,105,0.08);--green-t:#065F46;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#991B1B;
  --amber:#D97706;--amber-bg:rgba(217,119,6,0.08);--amber-t:#92400E;
  --purple:#7C3AED;--purple-bg:rgba(124,58,237,0.08);
  --t1:#0F172A;--t2:#334155;--t3:#64748B;
  --shadow:0 4px 20px rgba(0,0,0,0.08);
}
[data-theme="purple"]{
  --bg:#0a0a1a;--bg2:#12122a;--bg3:#1a1a3a;
  --card:#0d0d20;--card-b:rgba(139,92,246,0.15);--card-bh:rgba(139,92,246,0.35);
  --accent:#8B5CF6;--accent2:#A78BFA;--accent-d:rgba(139,92,246,0.1);
  --green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-t:#34D399;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-t:#F87171;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-t:#FCD34D;
  --purple:#8B5CF6;--purple-bg:rgba(139,92,246,0.12);
  --t1:#F0EEFF;--t2:#8A7AAA;--t3:#5A4A7A;
  --shadow:0 4px 24px rgba(0,0,0,0.5);
}
[data-theme="purple-light"]{
  --bg:#F0EEFF;--bg2:#E4E0F5;--bg3:#D5D0E8;
  --card:#FFFFFF;--card-b:rgba(139,92,246,0.15);--card-bh:rgba(139,92,246,0.3);
  --accent:#7C3AED;--accent2:#6D28D9;--accent-d:rgba(124,58,237,0.08);
  --green:#059669;--green-bg:rgba(5,150,105,0.08);--green-t:#065F46;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#991B1B;
  --amber:#D97706;--amber-bg:rgba(217,119,6,0.08);--amber-t:#92400E;
  --purple:#7C3AED;--purple-bg:rgba(124,58,237,0.08);
  --t1:#0F0A1A;--t2:#4A3A6A;--t3:#7A6A9A;
  --shadow:0 4px 20px rgba(0,0,0,0.08);
}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg2);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s,background .3s}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b)}
.logo-icon{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--purple));display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0;box-shadow:0 0 20px rgba(59,130,246,0.15)}
.logo-name{font-size:14px;font-weight:800;color:var(--t1)}
.logo-sub{font-size:9px;color:var(--t3);margin-top:1px}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12px;cursor:pointer;border-right:2px solid transparent;transition:all .15s;margin:1px 6px;border-radius:8px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t2)}
.nav-it.on{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600}
.nav-badge{margin-right:auto;background:rgba(59,130,246,0.15);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:11px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.15s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.2);cursor:pointer;width:100%;transition:.15s}
.logout-btn:hover{background:rgba(239,68,68,0.2)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--bg2);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,var(--accent),var(--purple));display:flex;align-items:center;justify-content:center;font-size:16px}
.mob-title{color:var(--t1);font-size:13px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:24px 28px 40px;min-width:0;transition:margin .25s}
.pg{display:none}
.pg.on{display:block;animation:fi .2s ease}
@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:20px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:20px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.tb-title i{color:var(--accent);font-size:22px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-purple{background:var(--purple-bg);color:#A78BFA}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:18px}
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:16px 18px;transition:all .2s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.m-label{font-size:10px;color:var(--t3);font-weight:600;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}
.m-val{font-size:24px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px}
.metric .m-icon{font-size:20px;margin-bottom:8px;display:block}
.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:border-color .2s}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:14px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.btn{font-family:inherit;font-size:11.5px;font-weight:600;border-radius:9px;padding:7px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}
.btn i{font-size:13px}
.btn-p{background:linear-gradient(135deg,var(--accent),var(--purple));color:#fff;box-shadow:0 2px 12px rgba(59,130,246,.25)}
.btn-p:hover{transform:translateY(-1px);box-shadow:0 4px 18px rgba(59,130,246,.35)}
.btn-o{background:transparent;border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:rgba(59,130,246,.3)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.2)}
.btn-d:hover{background:rgba(239,68,68,.2)}
.btn-pur{background:var(--purple-bg);color:#A78BFA;border:1px solid rgba(139,92,246,.2)}
.btn-pur:hover{background:rgba(139,92,246,.22)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,0.2)}
.btn-amber:hover{background:rgba(245,158,11,0.22)}
.btn-sm{padding:5px 10px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:7px}
.fg{display:flex;flex-direction:column;gap:5px;margin-bottom:12px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;display:flex;align-items:center;gap:4px}
.fi{width:100%;padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.15s}
.fi:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(59,130,246,.08);background:rgba(0,0,0,.3)}
.fi::placeholder{color:var(--t3)}
select.fi{appearance:none;cursor:pointer}
.user-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px}
.user-card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:16px 18px;transition:all .2s;box-shadow:var(--shadow)}
.user-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.user-card .head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.user-card .name{font-size:14px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:6px}
.user-card .status{font-size:10px;font-weight:700;padding:3px 10px;border-radius:12px}
.user-card .status.on{background:var(--green-bg);color:var(--green-t)}
.user-card .status.off{background:var(--red-bg);color:var(--red-t)}
.user-card .uuid{font-family:monospace;font-size:9.5px;color:var(--t3);margin-bottom:8px;word-break:break-all}
.user-card .info{display:flex;justify-content:space-between;font-size:11px;color:var(--t2);gap:8px;flex-wrap:wrap;margin-bottom:6px}
.user-card .quota-info{display:flex;justify-content:space-between;font-size:11px;color:var(--t2);margin-bottom:4px}
.user-card .quota-bar{height:6px;border-radius:4px;background:var(--accent-d);overflow:hidden;margin-bottom:10px}
.user-card .quota-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--accent),var(--purple));transition:width .6s ease}
.user-card .actions{display:flex;gap:5px;flex-wrap:wrap;margin-top:8px}
.user-card .actions .btn{flex:1;justify-content:center;min-width:fit-content;font-size:10px}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:38px;opacity:.3;display:block;margin-bottom:12px}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.3);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.3);background:var(--red-bg);color:var(--red-t)}
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:28px 26px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:fi .2s ease}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;transition:.15s}
.modal-close:hover{background:var(--red-bg);color:var(--red-t)}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--accent);font-size:18px}
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.conn-card{background:var(--card);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px;transition:.2s}
.conn-card:hover{border-color:var(--card-bh)}
.conn-card .ip{font-family:monospace;font-size:13px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-card .label{font-size:10px;color:var(--t3);margin-top:2px}
.conn-card .conn-info{display:flex;justify-content:space-between;margin-top:8px;font-size:10px;color:var(--t2);gap:6px;flex-wrap:wrap}
.conn-status-dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--green);animation:pulse 1.5s infinite;margin-right:3px}

@media(max-width:900px){.metrics{grid-template-columns:1fr 1fr}}
@media(max-width:768px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.4)}
  .main{margin-right:0;padding-top:66px}
  .mob-top{display:flex}
  .user-grid{grid-template-columns:1fr}
}
@media(max-width:500px){.metrics{grid-template-columns:1fr}.main{padding:62px 12px 30px}}
</style>
</head>
<body>
<div class="toast" id="toast"></div>

<!-- ===== مودال ساخت کانفیگ ===== -->
<div class="modal-bg" id="modal-user">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-user')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-user-plus"></i> 🦅 ساخت کانفیگ جدید</div>
    
    <div class="fg">
      <label><i class="ti ti-tag"></i> نام کاربری</label>
      <input class="fi" id="user-label" placeholder="مثلاً: کاربر علی">
    </div>
    
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">
      <div class="fg">
        <label><i class="ti ti-database"></i> حجم</label>
        <input class="fi" id="user-quota" type="number" min="0.5" step="0.5" value="2">
      </div>
      <div class="fg">
        <label><i class="ti ti-ruler"></i> واحد</label>
        <select class="fi" id="user-unit"><option value="GB">GB</option><option value="MB">MB</option></select>
      </div>
      <div class="fg">
        <label><i class="ti ti-calendar"></i> انقضا (روز)</label>
        <input class="fi" id="user-exp" type="number" min="0" value="30" placeholder="0=نامحدود">
      </div>
    </div>
    
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div class="fg">
        <label><i class="ti ti-fingerprint"></i> فینگرپرینت</label>
        <select class="fi" id="user-fingerprint">
          <option value="chrome">Chrome</option>
          <option value="firefox">Firefox</option>
          <option value="safari">Safari</option>
          <option value="edge">Edge</option>
          <option value="random">Random</option>
          <option value="none">None</option>
        </select>
      </div>
      <div class="fg">
        <label><i class="ti ti-devices"></i> محدودیت دستگاه</label>
        <input class="fi" id="user-devices" type="number" min="0" max="10" value="1" placeholder="0=نامحدود">
      </div>
    </div>
    
    <div class="fg">
      <label><i class="ti ti-settings"></i> پروتکل</label>
      <select class="fi" id="user-protocol">
        <option value="vless-ws">VLESS (WebSocket)</option>
        <option value="xhttp-stream-up">XHTTP (Stream)</option>
      </select>
    </div>
    
    <div style="display:flex;gap:8px;margin-top:16px">
      <button class="btn btn-p" onclick="saveUser()" style="flex:2"><i class="ti ti-check"></i> ساخت کانفیگ</button>
      <button class="btn btn-o" onclick="closeModal('modal-user')" style="flex:1">انصراف</button>
    </div>
  </div>
</div>

<!-- ===== هدر موبایل ===== -->
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo">🦅</div>
    <span class="mob-title">پنل عقاب</span>
  </div>
  <div class="mob-right">
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-palette" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>

<!-- ===== سایدبار ===== -->
<aside class="sidebar" id="sb">
  <div class="logo">
    <div class="logo-icon">🦅</div>
    <div><div class="logo-name">پنل عقاب</div><div class="logo-sub">مدیریت کاربران</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-it on" data-pg="users"><i class="ti ti-users"></i> کاربران</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات زنده</div>
  </div>
  <div class="sb-foot">
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-palette" id="theme-icon"></i> <span id="theme-label">تغییر تم</span></button>
    <button class="logout-btn" onclick="logout()"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>

<!-- ===== محتوای اصلی ===== -->
<main class="main">

<!-- ===== صفحه کاربران ===== -->
<section class="pg on" id="pg-users">
  <div class="topbar">
    <div>
      <div class="tb-title">🦅 کاربران</div>
      <div class="tb-sub" id="user-count">۰ کاربر</div>
    </div>
    <div class="tb-right">
      <span class="badge bg-green" id="online-badge"><span class="dot dg"></span> ۰ آنلاین</span>
      <button class="btn btn-p" onclick="openModal('modal-user')"><i class="ti ti-plus"></i> کانفیگ جدید</button>
    </div>
  </div>

  <!-- ===== کارت‌های آماری ===== -->
  <div class="metrics">
    <div class="metric"><div class="m-icon">👥</div><div class="m-label">کل کاربران</div><div class="m-val" id="total-users">۰</div></div>
    <div class="metric"><div class="m-icon">🟢</div><div class="m-label">آنلاین</div><div class="m-val" id="online-count">۰</div></div>
    <div class="metric"><div class="m-icon">📊</div><div class="m-label">مصرف کل</div><div class="m-val" id="total-usage">۰ GB</div></div>
    <div class="metric"><div class="m-icon">⛔</div><div class="m-label">غیرفعال</div><div class="m-val" id="inactive-count">۰</div></div>
  </div>

  <!-- ===== لیست کاربران ===== -->
  <div id="users-grid" class="user-grid">
    <div class="empty"><i class="ti ti-users"></i><p>هیچ کاربری ساخته نشده</p></div>
  </div>
</section>

<!-- ===== صفحه اتصالات زنده ===== -->
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title">🔌 اتصالات زنده</div><div class="tb-sub" id="conn-count">۰ اتصال</div></div>
    <div class="tb-right">
      <span class="badge bg-green" id="conn-live-badge"><span class="dot dg pulse"></span> فعال</span>
      <button class="btn btn-sm btn-o" onclick="loadConnections()"><i class="ti ti-refresh"></i> بروزرسانی</button>
    </div>
  </div>
  <div id="conns-grid" class="conn-grid">
    <div class="empty"><i class="ti ti-plug-off"></i><p>هیچ اتصال فعالی وجود ندارد</p></div>
  </div>
</section>

</main>

<script>
// ===== تنظیمات تم =====
const THEMES = ['dark', 'light', 'purple', 'purple-light'];
let currentTheme = localStorage.getItem('eagle-theme') || 'dark';

function applyTheme(theme) {
  currentTheme = theme;
  localStorage.setItem('eagle-theme', theme);
  document.documentElement.setAttribute('data-theme', theme);
  
  const icon = document.getElementById('theme-icon');
  const mobIcon = document.getElementById('theme-mob-icon');
  const label = document.getElementById('theme-label');
  
  const icons = {
    'dark': 'ti-moon',
    'light': 'ti-sun',
    'purple': 'ti-moon',
    'purple-light': 'ti-sun'
  };
  const labels = {
    'dark': 'تم تاریک',
    'light': 'تم روشن',
    'purple': 'تم بنفش',
    'purple-light': 'تم بنفش روشن'
  };
  
  icon.className = 'ti ' + icons[theme];
  if (mobIcon) mobIcon.className = 'ti ' + icons[theme];
  label.textContent = labels[theme];
}

function toggleTheme() {
  const idx = THEMES.indexOf(currentTheme);
  const next = THEMES[(idx + 1) % THEMES.length];
  applyTheme(next);
}

applyTheme(currentTheme);

// ===== توابع کمکی =====
function toast(msg, type='') {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast show' + (type ? ' ' + type : '');
  setTimeout(() => t.classList.remove('show'), 2500);
}

function fmtB(b) {
  if (!b || b === 0) return '0 B';
  if (b < 1024) return b + ' B';
  if (b < 1024**2) return (b/1024).toFixed(1) + ' KB';
  if (b < 1024**3) return (b/1024**2).toFixed(2) + ' MB';
  return (b/1024**3).toFixed(2) + ' GB';
}

function esc(s) {
  return String(s || '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function openModal(id) { document.getElementById(id).classList.add('open'); }
function closeModal(id) { document.getElementById(id).classList.remove('open'); }

// ===== احراز هویت =====
async function authF(url, opts={}) {
  const r = await fetch(url, opts);
  if (r.status === 401) { location.href = '/login'; throw new Error('unauthorized'); }
  return r;
}

async function logout() {
  try { await fetch('/api/logout', {method:'POST'}); } catch(e) {}
  location.href = '/login';
}

// ===== ناوبری =====
function navTo(name) {
  document.querySelectorAll('.nav-it').forEach(n => n.classList.toggle('on', n.dataset.pg === name));
  document.querySelectorAll('.pg').forEach(p => p.classList.toggle('on', p.id === 'pg-' + name));
  closeSb();
  if (name === 'users') loadUsers();
  if (name === 'connections') loadConnections();
}

document.querySelectorAll('.nav-it').forEach(el => {
  el.addEventListener('click', () => navTo(el.dataset.pg));
});

const sb = document.getElementById('sb'), overlay = document.getElementById('overlay');
function openSb(){ sb.classList.add('open'); overlay.classList.add('show'); }
function closeSb(){ sb.classList.remove('open'); overlay.classList.remove('show'); }
document.getElementById('open-sb').addEventListener('click', openSb);
overlay.addEventListener('click', closeSb);

// ===== بارگذاری کاربران =====
async function loadUsers() {
  try {
    const r = await authF('/api/links');
    const { links=[] } = await r.json();
    const grid = document.getElementById('users-grid');
    
    // آمار
    const total = links.length;
    const online = links.filter(l => l.active && !l.expired).length;
    const inactive = links.filter(l => !l.active || l.expired).length;
    const totalBytes = links.reduce((sum, l) => sum + (l.used_bytes || 0), 0);
    
    document.getElementById('total-users').textContent = total;
    document.getElementById('online-count').textContent = online;
    document.getElementById('inactive-count').textContent = inactive;
    document.getElementById('total-usage').textContent = fmtB(totalBytes);
    document.getElementById('user-count').textContent = total + ' کاربر';
    document.getElementById('online-badge').innerHTML = '<span class="dot dg"></span> ' + online + ' آنلاین';
    
    if (!links.length) {
      grid.innerHTML = '<div class="empty"><i class="ti ti-users"></i><p>هیچ کاربری ساخته نشده</p></div>';
      return;
    }
    
    const host = window.location.host;
    grid.innerHTML = links.map(l => {
      const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
      const bc = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--accent)';
      const active = l.active && !l.expired;
      const devices = l.max_devices || 0;
      const fp = l.fingerprint || 'chrome';
      const subLink = `https://${host}/sub/${l.uuid}`;
      
      return `<div class="user-card">
        <div class="head">
          <div class="name">🦅 ${esc(l.label)}</div>
          <span class="status ${active ? 'on' : 'off'}">${active ? '● آنلاین' : '● آفلاین'}</span>
        </div>
        <div class="uuid">🔑 ${esc(l.uuid)}</div>
        <div class="info">
          <span>📱 ${devices === 0 ? '∞' : devices + ' دستگاه'}</span>
          <span>🔑 ${esc(fp)}</span>
          <span>📅 ${l.expires_at ? new Date(l.expires_at).toLocaleDateString('fa-IR') : 'نامحدود'}</span>
        </div>
        <div class="quota-info">
          <span>📊 مصرف شده: ${fmtB(l.used_bytes)}</span>
          <span>📦 کل: ${l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes)}</span>
        </div>
        <div class="quota-bar">
          <div class="quota-fill" style="width: ${pct}%; background: ${bc}"></div>
        </div>
        <div class="actions">
          <button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))">
            <i class="ti ti-copy"></i> لینک
          </button>
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(subLink)}').then(()=>toast('ساب‌لینک کپی شد','ok'))">
            <i class="ti ti-link"></i> ساب
          </button>
          <button class="btn btn-sm btn-amber" onclick="resetUsage('${l.uuid}')">
            <i class="ti ti-rotate"></i> ریست
          </button>
          <button class="btn btn-sm btn-d" onclick="deleteUser('${l.uuid}')">
            <i class="ti ti-trash"></i> حذف
          </button>
        </div>
      </div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== ساخت کانفیگ جدید =====
async function saveUser() {
  const label = document.getElementById('user-label').value.trim() || 'کاربر';
  const quota = parseFloat(document.getElementById('user-quota').value) || 2;
  const unit = document.getElementById('user-unit').value || 'GB';
  const exp = parseInt(document.getElementById('user-exp').value) || 0;
  const fingerprint = document.getElementById('user-fingerprint').value || 'chrome';
  const devices = parseInt(document.getElementById('user-devices').value) || 0;
  const protocol = document.getElementById('user-protocol').value || 'vless-ws';
  
  try {
    const r = await authF('/api/links', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        label,
        limit_value: quota,
        limit_unit: unit,
        expires_days: exp,
        fingerprint: fingerprint,
        max_devices: devices,
        protocol: protocol,
        note: ''
      })
    });
    if (!r.ok) throw new Error();
    
    document.getElementById('user-label').value = '';
    document.getElementById('user-quota').value = '2';
    document.getElementById('user-unit').value = 'GB';
    document.getElementById('user-exp').value = '30';
    document.getElementById('user-fingerprint').value = 'chrome';
    document.getElementById('user-devices').value = '1';
    document.getElementById('user-protocol').value = 'vless-ws';
    
    closeModal('modal-user');
    toast('🦅 کانفیگ ساخته شد ✓', 'ok');
    loadUsers();
  } catch(e) {
    toast('خطا در ساخت', 'err');
  }
}

// ===== ریست مصرف =====
async function resetUsage(uuid) {
  if (!confirm('مصرف این کاربر ریست شود؟')) return;
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ reset_usage: true })
    });
    if (!r.ok) throw new Error();
    toast('مصرف ریست شد ✓', 'ok');
    loadUsers();
  } catch(e) { toast('خطا', 'err'); }
}

// ===== حذف کاربر =====
async function deleteUser(uuid) {
  if (!confirm('🦅 حذف این کاربر؟')) return;
  try {
    const r = await authF('/api/links/' + uuid, { method: 'DELETE' });
    if (!r.ok) throw new Error();
    toast('کاربر حذف شد', 'ok');
    loadUsers();
  } catch(e) { toast('خطا در حذف', 'err'); }
}

// ===== اتصالات زنده =====
async function loadConnections() {
  try {
    const r = await authF('/api/connections');
    const d = await r.json();
    const grid = document.getElementById('conns-grid');
    const count = d.count || 0;
    document.getElementById('conn-count').textContent = count + ' اتصال';
    
    if (!count) {
      grid.innerHTML = '<div class="empty"><i class="ti ti-plug-off"></i><p>هیچ اتصال فعالی وجود ندارد</p></div>';
      return;
    }
    
    grid.innerHTML = d.connections.map(c => {
      const secs = c.connected_at ? Math.max(0, Math.floor((Date.now() - new Date(c.connected_at).getTime()) / 1000)) : 0;
      const dur = secs < 60 ? secs + ' ث' : secs < 3600 ? Math.floor(secs/60) + ' د' : Math.floor(secs/3600) + ' س';
      return `<div class="conn-card">
        <div class="ip"><span class="conn-status-dot"></span> ${esc(c.ip)}</div>
        <div class="label">${esc(c.label || 'نامشخص')}</div>
        <div class="conn-info">
          <span>📥 ${esc(c.bytes_fmt || '0 B')}</span>
          <span>⏱ ${dur}</span>
        </div>
      </div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== بارگذاری اولیه =====
document.addEventListener('DOMContentLoaded', async () => {
  try {
    const r = await fetch('/api/me');
    const d = await r.json();
    if (!d.authenticated) location.href = '/login';
  } catch(e) { location.href = '/login'; }
  
  loadUsers();
  loadConnections();
  
  setInterval(() => {
    if (document.getElementById('pg-users').classList.contains('on')) loadUsers();
    if (document.getElementById('pg-connections').classList.contains('on')) loadConnections();
  }, 5000);
});
</script>
</body></html>"""


# ===== صفحه ساب‌لینک عقابی =====
def get_sub_page_html(uuid: str, link: dict) -> str:
    """صفحه نمایش اطلاعات کاربر با طراحی عقابی"""
    
    used = link.get('used_bytes', 0)
    limit = link.get('limit_bytes', 0)
    active = link.get('active', True)
    expired = link.get('expired', False)
    label = link.get('label', 'کاربر')
    fingerprint = link.get('fingerprint', 'chrome')
    max_devices = link.get('max_devices', 0)
    protocol = link.get('protocol', 'vless-ws')
    
    percent = 0
    if limit > 0:
        percent = min(100, (used / limit) * 100)
    
    expires_at = link.get('expires_at')
    if expires_at:
        try:
            from datetime import datetime
            exp_date = datetime.fromisoformat(expires_at.replace('Z', '+00:00'))
            days_left = (exp_date - datetime.now().astimezone()).days
            if days_left < 0:
                days_left = 0
        except:
            days_left = 'نامشخص'
    else:
        days_left = 'نامحدود'
    
    is_allowed = active and not expired
    vless_link = link.get('vless_link', '')
    sub_url = link.get('sub_url', '')
    
    def fmt_bytes(b):
        if not b or b == 0:
            return '0 B'
        if b < 1024:
            return f'{b} B'
        if b < 1024**2:
            return f'{b/1024:.1f} KB'
        if b < 1024**3:
            return f'{b/1024**2:.2f} MB'
        return f'{b/1024**3:.2f} GB'
    
    used_fmt = fmt_bytes(used)
    limit_fmt = 'نامحدود' if limit == 0 else fmt_bytes(limit)
    
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🦅 اطلاعات اشتراک - {label}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{
    font-family:'Vazirmatn',sans-serif;
    background:#0a0a0f;
    min-height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    padding:20px;
    color:#F0F0FF;
    position:relative;
    overflow-x:hidden;
}}
.bg-fx{{
    position:fixed;inset:0;
    background:radial-gradient(ellipse 70% 50% at 30% 20%,rgba(59,130,246,0.06),transparent 60%),
               radial-gradient(ellipse 60% 40% at 70% 80%,rgba(139,92,246,0.04),transparent 60%);
    z-index:0;
    pointer-events:none;
}}
.eagle-bg{{
    position:fixed;
    inset:0;
    z-index:0;
    pointer-events:none;
    opacity:0.03;
    font-size:300px;
    display:flex;
    align-items:center;
    justify-content:center;
    color:#F0F0FF;
}}
.orb{{
    position:fixed;
    border-radius:50%;
    filter:blur(120px);
    z-index:0;
    animation:float 12s ease-in-out infinite;
}}
.orb1{{width:400px;height:400px;background:rgba(59,130,246,0.04);top:-150px;right:-100px}}
.orb2{{width:300px;height:300px;background:rgba(139,92,246,0.04);bottom:-100px;left:-80px;animation-delay:6s}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-30px)}}}}
.card{{
    position:relative;
    z-index:10;
    background:rgba(15,15,30,0.85);
    backdrop-filter:blur(30px);
    -webkit-backdrop-filter:blur(30px);
    border:1px solid rgba(59,130,246,0.12);
    border-radius:28px;
    padding:40px 38px 34px;
    max-width:480px;
    width:100%;
    box-shadow:0 0 100px rgba(59,130,246,0.04),0 25px 70px rgba(0,0,0,0.6);
}}
.brand{{
    display:flex;
    align-items:center;
    gap:14px;
    margin-bottom:28px;
    padding-bottom:18px;
    border-bottom:1px solid rgba(59,130,246,0.08);
}}
.brand-icon{{
    width:52px;height:52px;border-radius:16px;
    background:linear-gradient(135deg,#3B82F6,#8B5CF6);
    display:flex;align-items:center;justify-content:center;
    font-size:28px;
    flex-shrink:0;
    box-shadow:0 0 40px rgba(59,130,246,0.15);
}}
.brand-text .name{{
    font-size:18px;font-weight:800;
    background:linear-gradient(135deg,#3B82F6,#8B5CF6);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}}
.brand-text .sub{{
    font-size:10.5px;color:#4A4A6A;margin-top:2px;-webkit-text-fill-color:#4A4A6A;
}}
.user-header{{
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom:6px;
}}
.user-name{{
    font-size:24px;font-weight:800;color:#F0F0FF;
    display:flex;align-items:center;gap:8px;
}}
.user-name .eagle{{font-size:20px}}
.status{{
    display:inline-flex;
    align-items:center;
    gap:5px;
    padding:5px 14px;
    border-radius:20px;
    font-size:12px;
    font-weight:700;
}}
.status.active{{
    background:rgba(16,185,129,0.12);
    color:#34D399;
    border:1px solid rgba(16,185,129,0.15);
}}
.status.inactive{{
    background:rgba(239,68,68,0.12);
    color:#F87171;
    border:1px solid rgba(239,68,68,0.15);
}}
.uuid-box{{
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.04);
    border-radius:10px;
    padding:8px 12px;
    font-size:10px;
    font-family:monospace;
    color:#4A4A6A;
    word-break:break-all;
    margin:6px 0 16px;
    cursor:pointer;
    transition:.15s;
}}
.uuid-box:hover{{
    background:rgba(59,130,246,0.05);
    border-color:rgba(59,130,246,0.1);
}}
.info-grid{{
    display:grid;
    gap:10px;
    margin:16px 0;
}}
.info-item{{
    background:rgba(255,255,255,0.02);
    border:1px solid rgba(255,255,255,0.04);
    border-radius:12px;
    padding:13px 16px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    transition:.15s;
}}
.info-item:hover{{
    background:rgba(255,255,255,0.03);
    border-color:rgba(255,255,255,0.06);
}}
.info-label{{
    font-size:12px;
    color:#6A6A8A;
    display:flex;
    align-items:center;
    gap:6px;
}}
.info-label i{{font-size:15px;color:#3B82F6}}
.info-value{{
    font-size:14px;
    font-weight:700;
    color:#F0F0FF;
}}
.info-value.used{{color:#8B5CF6}}
.info-value.remain{{color:#34D399}}
.info-value.proto{{
    font-size:11px;
    background:rgba(59,130,246,0.08);
    padding:4px 12px;
    border-radius:8px;
    border:1px solid rgba(59,130,246,0.08);
}}
.progress{{
    margin:18px 0 20px;
}}
.progress-bar{{
    height:7px;
    border-radius:5px;
    background:rgba(255,255,255,0.05);
    overflow:hidden;
}}
.progress-fill{{
    height:100%;
    border-radius:5px;
    background:linear-gradient(90deg,#3B82F6,#8B5CF6);
    width:{percent:.1f}%;
    transition:width 1s ease;
}}
.progress-text{{
    display:flex;
    justify-content:space-between;
    font-size:11px;
    color:#6A6A8A;
    margin-top:6px;
}}
.progress-text .pct{{font-weight:700;color:#F0F0FF}}
.vless-section{{
    background:rgba(255,255,255,0.02);
    border:1px solid rgba(255,255,255,0.04);
    border-radius:12px;
    padding:14px 16px;
    margin:16px 0;
}}
.vless-label{{
    font-size:10px;
    color:#6A6A8A;
    font-weight:700;
    text-transform:uppercase;
    letter-spacing:.06em;
    display:flex;
    align-items:center;
    gap:6px;
    margin-bottom:8px;
}}
.vless-label i{{color:#8B5CF6;font-size:13px}}
.vless-link{{
    font-family:monospace;
    font-size:10px;
    color:#A78BFA;
    word-break:break-all;
    line-height:1.8;
    background:rgba(0,0,0,0.2);
    padding:10px 12px;
    border-radius:8px;
    border:1px solid rgba(139,92,246,0.06);
}}
.actions{{
    display:flex;
    gap:8px;
    margin-top:14px;
    flex-wrap:wrap;
}}
.btn{{
    font-family:inherit;
    font-size:12px;
    font-weight:600;
    border-radius:10px;
    padding:9px 16px;
    cursor:pointer;
    display:inline-flex;
    align-items:center;
    gap:6px;
    border:none;
    transition:all .2s;
    white-space:nowrap;
    flex:1;
    justify-content:center;
}}
.btn i{{font-size:14px}}
.btn-primary{{
    background:linear-gradient(135deg,#3B82F6,#8B5CF6);
    color:#fff;
    box-shadow:0 4px 20px rgba(59,130,246,0.2);
}}
.btn-primary:hover{{
    transform:translateY(-2px);
    box-shadow:0 8px 30px rgba(59,130,246,0.3);
}}
.btn-secondary{{
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.06);
    color:#8A8AAA;
}}
.btn-secondary:hover{{
    background:rgba(255,255,255,0.08);
    color:#F0F0FF;
}}
.btn-success{{
    background:rgba(16,185,129,0.1);
    border:1px solid rgba(16,185,129,0.15);
    color:#34D399;
}}
.btn-success:hover{{
    background:rgba(16,185,129,0.15);
}}
.footer{{
    margin-top:22px;
    padding-top:16px;
    border-top:1px solid rgba(255,255,255,0.03);
    text-align:center;
    font-size:10px;
    color:#4A4A6A;
}}
.footer .eagle{{
    color:#3B82F6;
    font-weight:700;
}}
.toast{{
    position:fixed;
    bottom:30px;
    left:50%;
    transform:translateX(-50%) translateY(60px);
    background:rgba(15,15,30,0.95);
    backdrop-filter:blur(20px);
    border:1px solid rgba(59,130,246,0.12);
    color:#F0F0FF;
    border-radius:12px;
    padding:12px 22px;
    font-size:13px;
    opacity:0;
    transition:all .3s;
    z-index:999;
    pointer-events:none;
    display:flex;
    align-items:center;
    gap:8px;
    box-shadow:0 10px 40px rgba(0,0,0,0.4);
}}
.toast.show{{
    opacity:1;
    transform:translateX(-50%) translateY(0);
}}
.toast.ok{{
    border-color:rgba(16,185,129,0.2);
    color:#34D399;
}}
@media(max-width:520px){{
    .card{{padding:28px 20px 24px}}
    .user-name{{font-size:20px}}
    .brand-icon{{width:44px;height:44px;font-size:22px}}
    .info-item{{padding:11px 14px}}
    .btn{{font-size:11px;padding:8px 12px}}
}}
</style>
</head>
<body>
<div class="bg-fx"></div>
<div class="eagle-bg">🦅</div>
<div class="orb orb1"></div>
<div class="orb orb2"></div>
<div class="toast" id="toast"></div>

<div class="card">
    <div class="brand">
        <div class="brand-icon">🦅</div>
        <div class="brand-text">
            <div class="name">پنل عقاب</div>
            <div class="sub">اطلاعات اشتراک</div>
        </div>
    </div>

    <div class="user-header">
        <div class="user-name">
            <span class="eagle">🦅</span>
            {label}
        </div>
        <span class="status {'active' if is_allowed else 'inactive'}">
            <i class="ti {'ti-circle-check' if is_allowed else 'ti-circle-x'}"></i>
            {'فعال' if is_allowed else 'غیرفعال'}
        </span>
    </div>

    <div class="uuid-box" onclick="copyUUID()" title="کلیک برای کپی UUID">
        🔑 {uuid}
    </div>

    <div class="info-grid">
        <div class="info-item">
            <span class="info-label"><i class="ti ti-database"></i> مصرف</span>
            <span class="info-value used">{used_fmt}</span>
        </div>
        <div class="info-item">
            <span class="info-label"><i class="ti ti-package"></i> سهمیه</span>
            <span class="info-value">{limit_fmt}</span>
        </div>
        <div class="info-item">
            <span class="info-label"><i class="ti ti-calendar"></i> زمان باقیمانده</span>
            <span class="info-value">{days_left if days_left == 'نامحدود' else f'{days_left} روز'}</span>
        </div>
        <div class="info-item">
            <span class="info-label"><i class="ti ti-devices"></i> دستگاه‌ها</span>
            <span class="info-value">{max_devices if max_devices > 0 else '∞'}</span>
        </div>
        <div class="info-item">
            <span class="info-label"><i class="ti ti-fingerprint"></i> فینگرپرینت</span>
            <span class="info-value proto">{fingerprint}</span>
        </div>
        <div class="info-item">
            <span class="info-label"><i class="ti ti-settings"></i> پروتکل</span>
            <span class="info-value proto">{protocol}</span>
        </div>
    </div>

    <div class="progress">
        <div class="progress-bar">
            <div class="progress-fill" style="width:{percent:.1f}%"></div>
        </div>
        <div class="progress-text">
            <span>میزان مصرف</span>
            <span class="pct">{percent:.1f}%</span>
        </div>
    </div>

    <div class="vless-section">
        <div class="vless-label">
            <i class="ti ti-link"></i> لینک کانفیگ (VLESS)
        </div>
        <div class="vless-link" id="vless-link">{vless_link}</div>
    </div>

    <div class="actions">
        <button class="btn btn-primary" onclick="copyVless()">
            <i class="ti ti-copy"></i> کپی لینک
        </button>
        <button class="btn btn-success" onclick="copySub()">
            <i class="ti ti-link"></i> کپی ساب‌لینک
        </button>
        <button class="btn btn-secondary" onclick="showQR()">
            <i class="ti ti-qrcode"></i> QR
        </button>
    </div>

    <div class="footer">
        <span class="eagle">🦅</span> پنل عقاب · اطلاعات شخصی شما محفوظ است
    </div>
</div>

<script>
const vless = `{vless_link}`;
const subUrl = `{sub_url}`;
const uuid = `{uuid}`;

function toast(msg, type=''){{
    const t=document.getElementById('toast');
    t.textContent=msg;
    t.className='toast show'+(type?' '+type:'');
    setTimeout(()=>t.classList.remove('show'),2500);
}}

function copyVless(){{
    navigator.clipboard.writeText(vless).then(()=>toast('✅ لینک کانفیگ کپی شد','ok'));
}}

function copySub(){{
    navigator.clipboard.writeText(subUrl).then(()=>toast('✅ ساب‌لینک کپی شد','ok'));
}}

function copyUUID(){{
    navigator.clipboard.writeText(uuid).then(()=>toast('✅ UUID کپی شد','ok'));
}}

function showQR(){{
    window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(vless),'_blank');
}}
</script>
</body></html>"""
