from fastapi import APIRouter

from .endpoints import subscribers, campaigns

api_router = APIRouter()
api_router.include_router(subscribers.router, tags=["subscribers"], prefix="/subscribers")
api_router.include_router(campaigns.router, tags=["campaigns"], prefix="/campaigns")