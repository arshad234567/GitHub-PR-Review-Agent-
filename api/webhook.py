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

async def github_webhook(request: Request):
    """
    Receives GitHub webhook events.

    Phase 1:
        • Receive webhook
        • Print payload

    Later:
        • Verify webhook signature
        • Authenticate GitHub App
        • Fetch PR
        • Trigger LangGraph workflow
    """

    payload = await request.json()

    logger.info("GitHub webhook received.")

    logger.info(payload)

    return {
        "message": "Webhook received successfully."
    }