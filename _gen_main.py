"""
Generator script for main.py
Reads the original main.py and adds user management features.
Run: python _gen_main.py
"""
import re

ORIG = r"C:\Users\Administrator\.openclaw-autoclaw\workspace\.openclaw-attachments\20260703-113140-1aa8ba76-f22-main.py"
TARGET = r"C:\Users\Administrator\.openclaw-autoclaw\workspace\spider-panel\rvg-gateway\main.py"

with open(ORIG, "r", encoding="utf-8") as f:
    original = f.read()

# ── 1. Add new imports at module level ──────────────────────────────────────
new_imports = """import base64
import io

try:
    import qrcode
    from PIL import Image
    QR_AVAILABLE = True
except ImportError:
    QR_AVAILABLE = False
    logger.warning("qrcode/PIL not installed -- QR endpoints will return 501")
"""

# Remove the existing `import base64` that appears inside functions, 
# and make it module-level. Also add io, qrcode, PIL.
# Insert after the `from collections import deque, defaultdict` line
insert_marker = "from collections import deque, defaultdict"
if insert_marker in original:
    idx = original.index(insert_marker) + len(insert_marker)
    # Check if the new imports are already there
    if "QR_AVAILABLE" not in original:
        original = original[:idx] + "\n" + new_imports + original[idx:]

# ── 2. Update version in root endpoint ──────────────────────────────────────
original = original.replace('"version": "9.1"', '"version": "9.2"')

# ── 3. Add USERS to load_state ──────────────────────────────────────────────
# Change `global LINKS, AUTH, SUBS` to `global LINKS, AUTH, SUBS, USERS`
if "global LINKS, AUTH, SUBS, USERS" not in original:
    original = original.replace(
        "global LINKS, AUTH, SUBS",
        "global LINKS, AUTH, SUBS, USERS"
    )

# Add USERS loading in load_state: after `SUBS.update(data.get("subs", {}))`
subs_update_line = 'SUBS.update(data.get("subs", {}))'
if subs_update_line in original and 'USERS.update(data.get("users", {}))' not in original:
    original = original.replace(
        subs_update_line,
        subs_update_line + '\n            USERS.update(data.get("users", {}))'
    )

# Update log message in load_state
if "len(SUBS)} subs" in original and "users" not in original.split("len(SUBS)} subs")[1][:50]:
    original = original.replace(
        'logger.info(f"State loaded: {len(LINKS)} links, {len(SUBS)} subs")',
        'logger.info(f"State loaded: {len(LINKS)} links, {len(SUBS)} subs, {len(USERS)} users")'
    )

# ── 4. Add USERS to save_state ──────────────────────────────────────────────
# Add "users": dict(USERS) to the data dict
data_line = '"links": dict(LINKS),'
if data_line in original and '"users": dict(USERS),' not in original:
    original = original.replace(
        data_line,
        data_line + '\n                "users": dict(USERS),'
    )

# ── 5. Add USERS state variable ─────────────────────────────────────────────
# After `SUBS_LOCK = asyncio.Lock()`
subs_lock = "SUBS_LOCK = asyncio.Lock()"
if subs_lock in original and "USERS: dict" not in original:
    replacement = subs_lock + "\nUSERS: dict = {}\nUSERS_LOCK = asyncio.Lock()"
    original = original.replace(subs_lock, replacement)

# ── 6. Add USER_PROTOCOLS ──────────────────────────────────────────────────
protocols_line = 'PROTOCOLS = ("vless-ws", "xhttp-packet-up", "xhttp-stream-up", "xhttp-stream-one")'
if protocols_line in original and "USER_PROTOCOLS" not in original:
    original = original.replace(
        protocols_line,
        protocols_line + '\n\nUSER_PROTOCOLS = ("vless", "vmess", "trojan", "shadowsocks", "wireguard")'
    )

# ── 7. Add user helper functions after `client_ip` function ─────────────────
user_helpers = """

# ── User helper functions ────────────────────────────────────────────────────
def is_user_allowed(user: dict | None) -> bool:
    \"\"\"Check if a user is active and not expired.\"\"\"
    if user is None:
        return False
    if user.get("status") == "disabled":
        return False
    if user.get("status") == "expired":
        return False
    exp = user.get("expire_at")
    if exp:
        try:
            if datetime.now() > datetime.fromisoformat(exp):
                user["status"] = "expired"
                return False
        except Exception:
            pass
    lb = user.get("traffic_limit_bytes", 0)
    if lb > 0 and user.get("traffic_used_bytes", 0) >= lb:
        return False
    return True

def auto_check_user_expiry(user: dict):
    \"\"\"Auto-mark user as expired if past expire_at.\"\"\"
    if not user:
        return
    exp = user.get("expire_at")
    if not exp:
        return
    try:
        if datetime.now() > datetime.fromisoformat(exp):
            if user.get("status") not in ("expired", "disabled"):
                user["status"] = "expired"
    except Exception:
        pass

def generate_short_id() -> str:
    \"\"\"Generate a shorter ID for user management.\"\"\"
    return secrets.token_hex(6)

def generate_user_config(user_id: str, user: dict) -> str:
    \"\"\"Generate a connection config string for a user based on their protocol.\"\"\"
    host = get_host()
    protocol = user.get("protocol", "vless")
    config_uuid = user.get("config_uuid", "")
    username = user.get("username", user_id)
    remark = quote(f"RVG-{username}")

    if protocol == "vless":
        params = f"encryption=none&security=tls&type=ws&host={host}&path=/ws/{config_uuid}&sni={host}&fp=chrome"
        return f"vless://{config_uuid}@{host}:443?{params}#{remark}"

    elif protocol == "vmess":
        vmess_config = {
            "v": "2",
            "ps": username,
            "add": host,
            "port": "443",
            "id": config_uuid,
            "aid": "0",
            "scy": "auto",
            "net": "ws",
            "type": "none",
            "host": host,
            "path": f"/ws/{config_uuid}",
            "tls": "tls",
            "sni": host,
        }
        encoded = base64.b64encode(json.dumps(vmess_config).encode()).decode()
        return f"vmess://{encoded}"

    elif protocol == "trojan":
        params = f"security=tls&type=ws&host={host}&path=/ws/{config_uuid}&sni={host}"
        return f"trojan://{quote(config_uuid)}@{host}:443?{params}#{remark}"

    elif protocol == "shadowsocks":
        method = "aes-256-gcm"
        ss_encoded = base64.b64encode(f"{method}:{config_uuid}".encode()).decode()
        port = "8443"
        return f"ss://{ss_encoded}@{host}:{port}#{remark}"

    elif protocol == "wireguard":
        priv_key = base64.b64encode(secrets.token_bytes(32)).decode()
        pub_key = base64.b64encode(secrets.token_bytes(32)).decode()
        return (
            f"[Interface]\\n"
            f"PrivateKey = {priv_key}\\n"
            f"Address = 10.0.0.{hash(user_id) % 253 + 2}/24\\n"
            f"DNS = 1.1.1.1\\n\\n"
            f"[Peer]\\n"
            f"PublicKey = {pub_key}\\n"
            f"Endpoint = {host}:51820\\n"
            f"AllowedIPs = 0.0.0.0/0\\n"
        )

    return ""
"""

# Insert after client_ip function
client_ip_marker = '    return request.client.host if request.client else "نامشخص"'
if client_ip_marker in original:
    # Find the end of the client_ip function (the blank line after the return)
    idx = original.index(client_ip_marker) + len(client_ip_marker)
    # Check if already added
    if "generate_user_config" not in original:
        original = original[:idx] + "\n" + user_helpers + original[idx:]

# ── 8. Enhance stats endpoint ──────────────────────────────────────────────
# Find the stats endpoint and enhance it
old_stats_marker = 'async def get_stats(_=Depends(require_auth)):'
if old_stats_marker in original:
    stats_start = original.index(old_stats_marker)
    # Find the return dict and enhance it
    # The return dict starts with `return {`
    return_idx = original.index("return {", stats_start)
    
    # Add user stats to the return dict - find a good insertion point
    # Insert before "hourly" or at a natural point
    snap_line = 'snap = dict(LINKS)'
    snap_idx = original.index(snap_line, stats_start)
    
    # Replace the snapshot line to also snapshot users and subs
    if "snap_users" not in original[stats_start:stats_start+2000]:
        original = original.replace(
            'async with LINKS_LOCK:\n        snap = dict(LINKS)\n    return {',
            'async with LINKS_LOCK:\n        snap = dict(LINKS)\n    async with USERS_LOCK:\n        snap_users = dict(USERS)\n    async with SUBS_LOCK:\n        snap_subs = dict(SUBS)\n\n    # Auto-check user expiry\n    for user in snap_users.values():\n        auto_check_user_expiry(user)\n\n    # Count active users\n    active_users = sum(1 for u in snap_users.values() if u.get("status") == "active")\n    total_users = len(snap_users)\n\n    # Traffic across all links\n    total_bytes = stats["total_bytes"]\n    traffic_usage_gb = round(total_bytes / (1024 ** 3), 3)\n\n    # Connection-based health simulation\n    conn_count = len(connections)\n    if conn_count > 400:\n        server_status = "down"\n    elif conn_count > 200:\n        server_status = "degraded"\n    else:\n        server_status = "healthy"\n\n    # Simulated system metrics\n    cpu_percent = round(min(conn_count * 0.3 + 5, 95), 1)\n    ram_percent = round(min(45 + (total_users * 0.5) + (conn_count * 0.1), 95), 1)\n    disk_percent = round(min(25 + (len(snap) * 0.02) + (total_users * 0.1), 90), 1)\n    uptime_secs = max(time.time() - stats["start_time"], 1)\n    network_mbps = round(total_bytes / uptime_secs * 8 / 1000000, 2)\n\n    return {',
            1  # only first occurrence
        )
    
    # Now add the enhanced fields to the return dict
    # Find the closing of the return dict
    stats_return_end = original.index('"subs_count": len(SUBS),', stats_start)
    stats_return_end = original.index('\n', stats_return_end)
    
    # Insert enhanced fields before the closing brace
    enhanced_fields = """
        # Enhanced stats
        "active_users": active_users,
        "total_configs": len(snap),
        "total_users": total_users,
        "traffic_usage_gb": traffic_usage_gb,
        "server_status": server_status,
        "cpu_percent": cpu_percent,
        "ram_percent": ram_percent,
        "disk_percent": disk_percent,
        "network_mbps": network_mbps,
        "recent_activity": list(activity_logs)[-10:],"""
    
    if '"active_users": active_users' not in original:
        original = original[:stats_return_end] + enhanced_fields + original[stats_return_end:]

# ── 9. Add user management endpoints ────────────────────────────────────────
# Insert before the "Public sub page" section
public_sub_marker = "# ── Public sub page ──"
if public_sub_marker in original and "USER MANAGEMENT endpoints" not in original:
    user_endpoints = """
# ══════════════════════════════════════════════════════════════════════════════
# USER MANAGEMENT endpoints
# ══════════════════════════════════════════════════════════════════════════════

@app.get("/api/users")
async def list_users(_=Depends(require_auth)):
    \"\"\"List all users with traffic stats and status.\"\"\"
    host = get_host()
    async with USERS_LOCK:
        snap = dict(USERS)

    result = []
    for uid, u in snap.items():
        auto_check_user_expiry(u)
        protocol = u.get("protocol", "vless")
        result.append({
            "user_id": uid,
            "username": u.get("username"),
            "protocol": protocol,
            "traffic_limit_bytes": u.get("traffic_limit_bytes", 0),
            "traffic_limit_fmt": "∞" if u.get("traffic_limit_bytes", 0) == 0 else fmt_bytes(u["traffic_limit_bytes"]),
            "traffic_used_bytes": u.get("traffic_used_bytes", 0),
            "traffic_used_fmt": fmt_bytes(u.get("traffic_used_bytes", 0)),
            "traffic_percent": round(u.get("traffic_used_bytes", 0) / max(u.get("traffic_limit_bytes", 1), 1) * 100, 1) if u.get("traffic_limit_bytes", 0) > 0 else 0,
            "expire_at": u.get("expire_at"),
            "concurrent_connections": u.get("concurrent_connections", 3),
            "created_at": u.get("created_at"),
            "status": u.get("status", "active"),
            "server": u.get("server", ""),
            "config_uuid": u.get("config_uuid"),
            "subscription_uuid": u.get("subscription_uuid"),
            "config_url": f"https://{host}/api/users/{uid}/config",
            "qr_url": f"https://{host}/api/users/{uid}/qr",
            "subscription_url": f"https://{host}/api/users/{uid}/subscription",
            "connections": sum(1 for c in connections.values() if c.get("uuid") == u.get("config_uuid")),
        })
    result.sort(key=lambda x: x.get("created_at") or "", reverse=True)
    return {"users": result}

@app.post("/api/users")
async def create_user(request: Request, _=Depends(require_auth)):
    \"\"\"Create a new user with protocol config, traffic limit, and expiry.\"\"\"
    body = await request.json()
    username = (body.get("username") or "user").strip()[:40]
    password = str(body.get("password") or secrets.token_urlsafe(12))
    traffic_limit_gb = float(body.get("traffic_limit_gb") or 0)
    expire_days = int(body.get("expire_days") or 0)
    protocol = str(body.get("protocol") or "vless").lower()
    concurrent_connections = int(body.get("concurrent_connections") or 3)
    server = (body.get("server") or "IR-Tehran-01").strip()[:40]

    if protocol not in USER_PROTOCOLS:
        raise HTTPException(status_code=400, detail=f"Invalid protocol. Must be one of: {', '.join(USER_PROTOCOLS)}")
    if len(username) < 1:
        raise HTTPException(status_code=400, detail="Username is required")
    if len(password) < 4:
        raise HTTPException(status_code=400, detail="Password must be at least 4 characters")
    if concurrent_connections < 1:
        concurrent_connections = 1

    user_id = generate_short_id()
    config_uuid = generate_uuid()
    subscription_uuid = secrets.token_urlsafe(16)
    traffic_limit_bytes = int(traffic_limit_gb * 1024 ** 3) if traffic_limit_gb > 0 else 0
    expire_at = (datetime.now() + timedelta(days=expire_days)).isoformat() if expire_days > 0 else None

    async with USERS_LOCK:
        # Check for duplicate username
        for existing in USERS.values():
            if existing.get("username") == username:
                raise HTTPException(status_code=409, detail="Username already exists")

        USERS[user_id] = {
            "username": username,
            "password_hash": hash_password(password),
            "protocol": protocol,
            "traffic_limit_bytes": traffic_limit_bytes,
            "traffic_used_bytes": 0,
            "expire_at": expire_at,
            "concurrent_connections": concurrent_connections,
            "created_at": datetime.now().isoformat(),
            "status": "active",
            "server": server,
            "config_uuid": config_uuid,
            "subscription_uuid": subscription_uuid,
        }

    asyncio.create_task(save_state())
    log_activity("user", f"کاربر «{username}» با پروتکل {protocol} ساخته شد", "ok")
    host = get_host()
    return {
        "user_id": user_id,
        **USERS[user_id],
        "password_hash": None,
        "config_url": f"https://{host}/api/users/{user_id}/config",
        "qr_url": f"https://{host}/api/users/{user_id}/qr",
        "subscription_url": f"https://{host}/api/users/{user_id}/subscription",
        "config": generate_user_config(user_id, USERS[user_id]),
    }

@app.patch("/api/users/{user_id}/toggle")
async def toggle_user(user_id: str, _=Depends(require_auth)):
    \"\"\"Enable or disable a user.\"\"\"
    async with USERS_LOCK:
        u = USERS.get(user_id)
        if not u:
            raise HTTPException(status_code=404, detail="user not found")
        old = u.get("status", "active")
        if old == "disabled":
            u["status"] = "active"
        else:
            u["status"] = "disabled"
        new_status = u["status"]
    asyncio.create_task(save_state())
    log_activity("user", f"کاربر «{u['username']}» {'غیرفعال' if new_status == 'disabled' else 'فعال'} شد", "ok" if new_status == "active" else "warn")
    return {"ok": True, "user_id": user_id, "status": new_status}

@app.patch("/api/users/{user_id}/reset")
async def reset_user_traffic(user_id: str, _=Depends(require_auth)):
    \"\"\"Reset a user's traffic usage to zero.\"\"\"
    async with USERS_LOCK:
        u = USERS.get(user_id)
        if not u:
            raise HTTPException(status_code=404, detail="user not found")
        u["traffic_used_bytes"] = 0
        username = u.get("username", user_id)
    asyncio.create_task(save_state())
    log_activity("user", f"مصرف کاربر «{username}» ریست شد", "info")
    return {"ok": True, "user_id": user_id, "traffic_used_bytes": 0}

@app.delete("/api/users/{user_id}")
async def delete_user(user_id: str, _=Depends(require_auth)):
    \"\"\"Delete a user permanently.\"\"\"
    async with USERS_LOCK:
        u = USERS.get(user_id)
        if not u:
            raise HTTPException(status_code=404, detail="user not found")
        username = u.get("username", user_id)
        USERS.pop(user_id, None)
    asyncio.create_task(save_state())
    log_activity("user", f"کاربر «{username}» حذف شد", "err")
    return {"ok": True, "deleted": user_id}

@app.get("/api/users/{user_id}/config")
async def get_user_config(user_id: str, _=Depends(require_auth)):
    \"\"\"Return the protocol config string for a user.\"\"\"
    async with USERS_LOCK:
        u = USERS.get(user_id)
        if not u:
            raise HTTPException(status_code=404, detail="user not found")
        config = generate_user_config(user_id, u)
        username = u.get("username")
        protocol = u.get("protocol")
    host = get_host()
    return {
        "user_id": user_id,
        "username": username,
        "protocol": protocol,
        "config": config,
        "config_url": f"https://{host}/api/users/{user_id}/config",
        "qr_url": f"https://{host}/api/users/{user_id}/qr",
        "subscription_url": f"https://{host}/api/users/{user_id}/subscription",
    }

@app.get("/api/users/{user_id}/qr")
async def get_user_qr(user_id: str, _=Depends(require_auth)):
    \"\"\"Return a QR code PNG image for the user's config.\"\"\"
    if not QR_AVAILABLE:
        raise HTTPException(status_code=501, detail="QR code generation not available (install qrcode and Pillow)")

    async with USERS_LOCK:
        u = USERS.get(user_id)
        if not u:
            raise HTTPException(status_code=404, detail="user not found")
        config = generate_user_config(user_id, u)

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=4, error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(config)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return Response(content=buf.getvalue(), media_type="image/png",
                    headers={"Content-Disposition": f"inline; filename={user_id}.png"})

@app.get("/api/users/{user_id}/subscription")
async def get_user_subscription(user_id: str, _=Depends(require_auth)):
    \"\"\"Return the subscription URL for a user.\"\"\"
    host = get_host()
    async with USERS_LOCK:
        u = USERS.get(user_id)
        if not u:
            raise HTTPException(status_code=404, detail="user not found")
        sub_uuid = u.get("subscription_uuid")
        username = u.get("username")

    if not sub_uuid:
        raise HTTPException(status_code=404, detail="no subscription configured")

    config = generate_user_config(user_id, u)
    content = base64.b64encode(config.encode()).decode()

    return {
        "user_id": user_id,
        "username": username,
        "subscription_uuid": sub_uuid,
        "subscription_url": f"https://{host}/sub/{sub_uuid}",
        "encoded_config": content,
    }

"""
    original = original.replace(public_sub_marker, user_endpoints + "\n" + public_sub_marker)

# ── 10. Write the final file ───────────────────────────────────────────────
with open(TARGET, "w", encoding="utf-8") as f:
    f.write(original)

print(f"✅ Written {len(original)} chars, {len(original.splitlines())} lines to {TARGET}")
print("Done!")
