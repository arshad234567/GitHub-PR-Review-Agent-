import hashlib
import hmac

from fastapi import HTTPException, Request, status
from app.config import settings

class GitHubWebhookVerifier:
    """
    Verifies that incoming webhook requests
    actually originate from GitHub.
    """
    @staticmethod
    async def verify(request: Request, body: bytes) -> None:
        signature = request.headers.get("X-Hub-Signature-256")

        if signature is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing GitHub signature.",
            )

        expected_signature = (
            "sha256="
            + hmac.new(
                settings.GITHUB_WEBHOOK_SECRET.encode(),
                body,
                hashlib.sha256,
            ).hexdigest()
        )

        if not hmac.compare_digest(signature, expected_signature):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid GitHub webhook signature.",
            )