from fastapi import APIRouter

from .endpoints import subscribers, campaigns, auth

api_router = APIRouter()

# public
api_router.include_router(auth.router, tags=["auth"], prefix="/auth")

# secured (example: only owner/admin can manage subscribers & campaigns)
api_router.include_router(
    subscribers.router,
    tags=["subscribers"],
    prefix="/subscribers",
)
api_router.include_router(
    campaigns.router,
    tags=["campaigns"],
    prefix="/campaigns",
)