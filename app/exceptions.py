
from fastapi import Request
from fastapi.responses import JSONResponse


class GithubWebhookException(Exception):

    def __init__(self, message: str):
        self.message = message

async def github_exception_handler(
        request: Request,
        exc: GithubWebhookException,
):
    return JSONResponse(
        status_code = 400,
        content = {
            "error":exc.message,
        },
    )