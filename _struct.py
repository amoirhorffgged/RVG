path = r"C:\Users\Administrator\.openclaw-autoclaw\workspace\spider-panel\rvg-gateway\main.py"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

markers = [
    "async def get_stats(_=Depends(require_auth)):",
    "USER MANAGEMENT endpoints",
    "async def list_users(_=Depends(require_auth)):",
    "async def create_user(request: Request, _=Depends(require_auth)):",
    "async def delete_user(user_id: str, _=Depends(require_auth)):",
    "async def get_user_qr(user_id: str, _=Depends(require_auth)):",
    "async def toggle_user(user_id: str, _=Depends(require_auth)):",
    "async def reset_user_traffic(user_id: str, _=Depends(require_auth)):",
    "async def get_user_config(user_id: str, _=Depends(require_auth)):",
    "async def get_user_subscription(user_id: str, _=Depends(require_auth)):",
    "Public sub page",
    "from relay_vless import (",
    "app.add_api_websocket_route",
    "from xhttp_siz10 import",
    "app.include_router(xhttp_router)",
]

for i, line in enumerate(lines, 1):
    stripped = line.strip()
    for m in markers:
        if m in stripped:
            print(f"Line {i}: ...{stripped[:100]}")
            break
