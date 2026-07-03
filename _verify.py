"""Verify all required features in main.py"""
path = r"C:\Users\Administrator\.openclaw-autoclaw\workspace\spider-panel\rvg-gateway\main.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

checks = [
    ("USERS dict", "USERS: dict = {}"),
    ("USERS_LOCK", "USERS_LOCK = asyncio.Lock()"),
    ("load_state USERS", "USERS.update"),
    ("save_state USERS", '"users": dict(USERS)'),
    ("QR_AVAILABLE", "QR_AVAILABLE"),
    ("qrcode import", "import qrcode"),
    ("PIL import", "from PIL import Image"),
    ("io import", "import io"),
    ("base64 module import at top", "\nimport base64\n"),
    ("generate_user_config", "def generate_user_config"),
    ("generate_short_id", "def generate_short_id"),
    ("is_user_allowed", "def is_user_allowed"),
    ("auto_check_user_expiry", "def auto_check_user_expiry"),
    ("USER_PROTOCOLS", "USER_PROTOCOLS"),
    ("list_users endpoint", "async def list_users"),
    ("create_user endpoint", "async def create_user"),
    ("toggle_user endpoint", "async def toggle_user"),
    ("reset_user_traffic endpoint", "async def reset_user_traffic"),
    ("delete_user endpoint", "async def delete_user"),
    ("get_user_config endpoint", "async def get_user_config"),
    ("get_user_qr endpoint", "async def get_user_qr"),
    ("get_user_subscription endpoint", "async def get_user_subscription"),
    ("VLESS config gen", 'vless://'),
    ("VMESS config gen", 'vmess://'),
    ("Trojan config gen", 'trojan://'),
    ("Shadowsocks config gen", 'ss://'),
    ("WireGuard config gen", '[Interface]'),
    ("Enhanced stats active_users", '"active_users": active_users'),
    ("Enhanced stats server_status", '"server_status": server_status'),
    ("Enhanced stats cpu_percent", '"cpu_percent": cpu_percent'),
    ("Enhanced stats ram_percent", '"ram_percent": ram_percent'),
    ("Enhanced stats disk_percent", '"disk_percent": disk_percent'),
    ("Enhanced stats network_mbps", '"network_mbps": network_mbps'),
    ("Enhanced stats recent_activity", '"recent_activity": list(activity_logs)'),
    ("WebSocket route", "app.add_api_websocket_route"),
    ("XHTTP router", "xhttp_router"),
    ("relay_vless imports", "from relay_vless import"),
    ("HTTP proxy", "/proxy/{target_url:path}"),
    ("Session auth", "rvg_session"),
    ("Link CRUD", "/api/links"),
    ("Sub groups", "/api/subs"),
    ("Public sub page", "/p/{uuid_key}"),
    ("Sub endpoints", "/sub/{uuid}"),
    ("Sub all", "/sub-all"),
    ("State persistence", "def load_state"),
    ("Traffic stats", "hourly_traffic"),
    ("Error logs", "error_logs"),
    ("Connection tracking", "connections: dict"),
    ("Password hashing for users", 'hash_password(password)'),
    ("Auto-expire in stats", "auto_check_user_expiry(user)"),
    ("version 9.2", '"version": "9.2"'),
    ("hashlib import", "import hashlib"),
    ("hash_password function", "def hash_password"),
]

all_ok = True
for name, pattern in checks:
    found = pattern in content
    if not found:
        print(f"MISSING: {name}")
        all_ok = False

if all_ok:
    print(f"ALL {len(checks)} CHECKS PASSED")
else:
    print("Some checks failed!")
