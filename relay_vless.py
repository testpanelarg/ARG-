# relay_vless.py - نسخه پایدار با پشتیبانی از IP خروجی

import asyncio
import socket
import logging
from datetime import datetime
from typing import Optional

logger = logging.getLogger("ARG-Gateway")

RELAY_BUF = 64 * 1024  # 64KB

# ========== کش موقت برای IP های کاربران ==========
_user_ip_cache = {}
CACHE_TTL = 60  # 60 ثانیه

# ========== تابع دریافت IP خروجی کاربر (بدون Circular Import) ==========
def get_user_outbound_ip_sync(uuid: str) -> Optional[str]:
    """دریافت IP خروجی اختصاصی کاربر - نسخه همزمان"""
    try:
        # تلاش برای خواندن مستقیم از فایل دیتابیس
        import json
        from pathlib import Path
        
        data_file = Path("/data/arg_state.json")
        if data_file.exists():
            with open(data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                links = data.get("links", {})
                if uuid in links:
                    return links[uuid].get("outbound_ip", "").strip()
    except Exception as e:
        logger.debug(f"Could not read outbound IP: {e}")
    
    return ""

# ========== تابع ایجاد سوکت با IP خروجی ==========
def create_socket_with_source_ip(host: str, port: int, source_ip: str = None) -> Optional[socket.socket]:
    """ایجاد سوکت TCP با IP خروجی مشخص"""
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.settimeout(15)
        
        if source_ip and source_ip.strip():
            try:
                sock.bind((source_ip.strip(), 0))
                logger.info(f"🔗 Socket bound to source IP: {source_ip}")
            except Exception as e:
                logger.warning(f"⚠️ Failed to bind to {source_ip}: {e}")
                # اگر بایند نشد، از IP پیش‌فرض استفاده کن
                pass
        
        sock.connect((host, port))
        sock.settimeout(None)  # بعد از اتصال، تایم‌اوت رو بردار
        return sock
    except Exception as e:
        if sock:
            try:
                sock.close()
            except:
                pass
        logger.error(f"❌ Socket creation failed: {e}")
        return None

# ========== تابع اصلی Relay با مدیریت خطا ==========
async def relay_ws_to_tcp(websocket, sock: socket.socket, uuid: str):
    """Relay از WebSocket به TCP"""
    try:
        while True:
            try:
                data = await asyncio.wait_for(websocket.receive_bytes(), timeout=30.0)
                if not data:
                    break
                try:
                    sock.sendall(data)
                except (socket.error, BrokenPipeError, ConnectionResetError) as e:
                    logger.debug(f"TCP send error: {e}")
                    break
            except asyncio.TimeoutError:
                # تایم‌اوت - ادامه بده
                continue
            except Exception as e:
                logger.debug(f"WS receive error: {e}")
                break
    except Exception as e:
        logger.debug(f"WS->TCP relay stopped: {e}")
    finally:
        try:
            sock.close()
        except:
            pass

async def relay_tcp_to_ws(websocket, sock: socket.socket, uuid: str):
    """Relay از TCP به WebSocket"""
    loop = asyncio.get_event_loop()
    try:
        while True:
            try:
                data = await asyncio.wait_for(
                    loop.sock_recv(sock, RELAY_BUF),
                    timeout=30.0
                )
                if not data:
                    break
                try:
                    await websocket.send_bytes(data)
                except Exception as e:
                    logger.debug(f"WS send error: {e}")
                    break
            except asyncio.TimeoutError:
                continue
            except (socket.error, ConnectionResetError) as e:
                logger.debug(f"TCP recv error: {e}")
                break
    except Exception as e:
        logger.debug(f"TCP->WS relay stopped: {e}")
    finally:
        try:
            sock.close()
        except:
            pass

# ========== تابع بررسی و استفاده کاربر ==========
async def check_and_use(uuid: str) -> bool:
    """بررسی اعتبار کاربر و افزایش مصرف"""
    try:
        from main import LINKS, LINKS_LOCK, is_link_allowed
        async with LINKS_LOCK:
            link = LINKS.get(uuid)
            if not link:
                return False
            if not is_link_allowed(link):
                return False
            # افزایش مصرف (تقریبی)
            link["used_bytes"] = link.get("used_bytes", 0) + 1024
            return True
    except Exception as e:
        logger.error(f"check_and_use error: {e}")
        return False

# ========== WebSocket Tunnel اصلی ==========
async def websocket_tunnel(websocket, uuid: str):
    """WebSocket tunnel با پشتیبانی از IP خروجی"""
    from main import connections, LINKS, LINKS_LOCK, log_activity, is_link_allowed
    
    client_addr = websocket.client.host if websocket.client else "unknown"
    logger.info(f"🔗 New WS connection: {uuid} from {client_addr}")
    
    # دریافت IP خروجی کاربر
    outbound_ip = get_user_outbound_ip_sync(uuid)
    if outbound_ip:
        logger.info(f"🌐 User {uuid} using outbound IP: {outbound_ip}")
    
    # === مرحله 1: بررسی اعتبار ===
    try:
        async with LINKS_LOCK:
            link = LINKS.get(uuid)
            if not link:
                await websocket.close(code=1008, reason="User not found")
                return
            
            if not is_link_allowed(link):
                await websocket.close(code=1008, reason="User inactive or expired")
                return
    except Exception as e:
        logger.error(f"Auth check error: {e}")
        await websocket.close(code=1011, reason="Internal error")
        return
    
    # === مرحله 2: آماده‌سازی ===
    sock = None
    target_host = "8.8.8.8"  # این رو با سرور Xray خودت جایگزین کن
    target_port = 53
    
    try:
        # ایجاد سوکت با IP خروجی
        sock = create_socket_with_source_ip(target_host, target_port, outbound_ip)
        if not sock:
            await websocket.close(code=1011, reason="Connection failed")
            return
        
        # ذخیره اتصال
        connections[uuid] = {
            "ip": client_addr,
            "uuid": uuid,
            "connected_at": datetime.now().isoformat(),
            "transport": "vless-ws",
            "bytes": 0,
        }
        
        log_activity("ws", f"User {uuid} connected from {client_addr}" + 
                    (f" with outbound IP {outbound_ip}" if outbound_ip else ""), "ok")
        
        # === مرحله 3: شروع Relay ===
        await asyncio.gather(
            relay_ws_to_tcp(websocket, sock, uuid),
            relay_tcp_to_ws(websocket, sock, uuid),
        )
        
    except asyncio.CancelledError:
        logger.info(f"Task cancelled: {uuid}")
    except Exception as e:
        logger.error(f"❌ WS error: {e}")
    finally:
        # پاکسازی
        connections.pop(uuid, None)
        if sock:
            try:
                sock.close()
            except:
                pass
        try:
            await websocket.close(code=1000)
        except:
            pass
        
        log_activity("ws", f"User {uuid} disconnected from {client_addr}", "info")
