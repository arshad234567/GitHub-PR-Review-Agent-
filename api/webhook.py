from fastapi import APIRouter, Request, status
from app.logging import logger

router = APIRouter(
    prefix="/webhook",
    tags=["GitHub Webhook"],
)

@router.post(
    "/github",
    status_code=status.HTTP_200_OK,
)
