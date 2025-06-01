from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.rate_limit import init_rate_limiter
from .core.config import settings
from .api.v1.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url="/openapi.json",
)

@app.on_event("startup")
async def startup():
    await init_rate_limiter()

# CORS (adjust origins in .env)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")