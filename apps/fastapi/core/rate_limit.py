import os
from fastapi import Request
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import redis.asyncio as redis

RATE = int(os.getenv("RATE_LIMIT", "100"))  # requests per minute

async def init_rate_limiter():
    pool = redis.ConnectionPool.from_url("redis://redis:6379/2", encoding="utf-8")
    await FastAPILimiter.init(redis.Redis(connection_pool=pool))

# dependency generator: use in routers
def limit(n: int = RATE, sec: int = 60):
    """
    Returns a dependency that enforces `n` requests per `sec` seconds
    for the current user or IP.
    """
    return RateLimiter(times=n, seconds=sec, identifier=lambda r: _key(r))

def _key(request: Request) -> str:
    # auth’d users -> user_id; otherwise fall back to IP
    uid = request.state.user_id if hasattr(request.state, "user_id") else None
    return str(uid) if uid else request.client.host