# relay_vless.py - با پشتیبانی از IP خروجی اختصاصی هر کاربر

import asyncio
import json
import socket
import struct
import logging
from datetime import datetime
from typing import Optional, Tuple
from fastapi import WebSocket, WebSocketDispose
import httpx
import os

logger = logging.getLogger("ARG-Gateway")

RELAY_BUF = 64 * 1024  # 64KB

# ========== تابع دریافت IP خروجی کاربر ==========
async def get_user_outbound_ip(uuid: str) -> Optional[str]:
    """دریافت IP خروجی اختصاصی کاربر از دیتابیس"""
    from main import LINKS, LINKS_LOCK
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
        if link:
            return link.get("outbound_ip", "").strip()
    return ""

# ========== تابع ایجاد سوکت با IP خروجی ==========
def create_socket_with_source_ip(host: str, port: int, source_ip: str = None) -> socket.socket:
    """ایجاد سوکت TCP با IP خروجی مشخص"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    sock.settimeout(10)
    
    if source_ip:
        try:
            sock.bind((source_ip, 0))  # بایند به IP خروجی اختصاصی
            logger.info(f"🔗 Socket bound to source IP: {source_ip}")
        except Exception as e:
            logger.warning(f"⚠️ Failed to bind to {source_ip}: {e}")
    
    sock.connect((host, port))
    return sock

# ========== تابع اصلی Relay ==========
def parse_vless_header(data: bytes) -> Tuple[bytes, bytes]:
    """پارسر هدر VLESS - ساده شده"""
    try:
        # VLESS header: version(1) + user_len(1) + user_id(16) + ...
        if len(data) < 18:
            return data, b""
        
        version = data[0]
        user_len = data[1]
        if len(data) < 2 + user_len + 16:
            return data, b""
        
        user_id = data[2:2+user_len]
        # بقیه هدر رو نادیده میگیریم و برمیگردونیم
        remaining = data[2+user_len+16:]
        return user_id, remaining
    except Exception:
        return b"", data

async def check_and_use(uuid: str, client_ip: str) -> bool:
    """بررسی اعتبار و افزایش مصرف کاربر"""
    from main import LINKS, LINKS_LOCK, is_link_allowed, log_activity
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
        if not link:
            return False
        if not is_link_allowed(link):
            return False
        # افزایش مصرف
        link["used_bytes"] = link.get("used_bytes", 0) + 1024  # تقریبی
        return True

async def relay_ws_to_tcp(websocket: WebSocket, sock: socket.socket, uuid: str):
    """Relay از WebSocket به TCP با IP خروجی"""
    try:
        while True:
            data = await websocket.receive_bytes()
            if not data:
                break
            try:
                sock.sendall(data)
                # به‌روزرسانی مصرف
                from main import LINKS, LINKS_LOCK
                async with LINKS_LOCK:
                    if uuid in LINKS:
                        LINKS[uuid]["used_bytes"] = LINKS[uuid].get("used_bytes", 0) + len(data)
            except Exception as e:
                logger.warning(f"TCP send error: {e}")
                break
    except Exception as e:
        logger.debug(f"WS->TCP relay stopped: {e}")

async def relay_tcp_to_ws(websocket: WebSocket, sock: socket.socket, uuid: str):
    """Relay از TCP به WebSocket"""
    sock.setblocking(False)
    loop = asyncio.get_event_loop()
    try:
        while True:
            data = await loop.sock_recv(sock, RELAY_BUF)
            if not data:
                break
            try:
                await websocket.send_bytes(data)
                # به‌روزرسانی مصرف
                from main import LINKS, LINKS_LOCK
                async with LINKS_LOCK:
                    if uuid in LINKS:
                        LINKS[uuid]["used_bytes"] = LINKS[uuid].get("used_bytes", 0) + len(data)
            except Exception as e:
                logger.warning(f"WS send error: {e}")
                break
    except Exception as e:
        logger.debug(f"TCP->WS relay stopped: {e}")

# ========== WebSocket Tunnel اصلی با IP خروجی ==========
async def websocket_tunnel(websocket: WebSocket, uuid: str):
    """WebSocket tunnel با پشتیبانی از IP خروجی اختصاصی"""
    from main import connections, LINKS, LINKS_LOCK, log_activity, client_ip, is_link_allowed
    
    await websocket.accept()
    client_addr = websocket.client.host if websocket.client else "unknown"
    logger.info(f"🔗 New WS connection: {uuid} from {client_addr}")
    
    # ========== دریافت IP خروجی اختصاصی کاربر ==========
    outbound_ip = await get_user_outbound_ip(uuid)
    if outbound_ip:
        logger.info(f"🌐 User {uuid} using outbound IP: {outbound_ip}")
    else:
        logger.info(f"🌐 User {uuid} using default IP")
    
    try:
        # بررسی اعتبار کاربر
        async with LINKS_LOCK:
            link = LINKS.get(uuid)
            if not link:
                await websocket.close(code=1008, reason="User not found")
                return
            
            if not is_link_allowed(link):
                await websocket.close(code=1008, reason="User inactive or expired")
                return
            
            # ذخیره اتصال
            connections[uuid] = {
                "ip": client_addr,
                "uuid": uuid,
                "connected_at": datetime.now().isoformat(),
                "transport": "vless-ws",
                "bytes": 0,
            }
        
        # ========== اتصال به سرور مقصد با IP خروجی اختصاصی ==========
        # اینجا باید به سرور اصلی Xray یا مستقیماً به اینترنت وصل بشه
        # برای نمونه به Google DNS متصل میشیم (8.8.8.8:53)
        # در نسخه واقعی باید به Xray یا سرور هدف متصل بشه
        
        target_host = os.environ.get("TARGET_HOST", "8.8.8.8")
        target_port = int(os.environ.get("TARGET_PORT", 53))
        
        try:
            # ایجاد سوکت با IP خروجی اختصاصی
            sock = create_socket_with_source_ip(target_host, target_port, outbound_ip)
        except Exception as e:
            logger.error(f"❌ Failed to connect to target: {e}")
            await websocket.close(code=1011, reason="Connection failed")
            return
        
        log_activity("ws", f"User {uuid} connected from {client_addr}" + 
                    (f" with outbound IP {outbound_ip}" if outbound_ip else ""), "ok")
        
        # شروع Relay
        try:
            await asyncio.gather(
                relay_ws_to_tcp(websocket, sock, uuid),
                relay_tcp_to_ws(websocket, sock, uuid),
            )
        except Exception as e:
            logger.warning(f"Relay error: {e}")
        finally:
            sock.close()
            
    except WebSocketDispose:
        logger.info(f"👋 WS disconnected: {uuid}")
    except Exception as e:
        logger.error(f"❌ WS error: {e}")
    finally:
        # پاکسازی اتصال
        from main import connections
        connections.pop(uuid, None)
        
        # ثبت خروج
        log_activity("ws", f"User {uuid} disconnected from {client_addr}", "info")

# ========== تابع کمکی برای تست IP خروجی ==========
async def test_outbound_ip(ip: str) -> bool:
    """تست اینکه آیا IP خروجی قابل استفاده هست یا نه"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.bind((ip, 0))
        sock.connect(("8.8.8.8", 53))
        sock.close()
        return True
    except Exception:
        return False
