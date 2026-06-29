from fastapi import APIRouter
from app.config import settings

router = APIRouter(
    prefix="/health",
    tags=["health"],
)

@router.get("/")

async def health():
    """
    Health check endpoint.

    Used by:
    -Docker
    -Kubernetes
    -Monitoring tools

    """
    return {
        "status": "ok",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,

    }