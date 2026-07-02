import time
from pathlib import Path

import jwt
from github import Github, GithubIntegration

from app.config import settings

class GitHubClient:
    """
    Handles GitHub App authentication and
    provides an authenticated GitHub client.
    """

    def __init__(self):
        self.app_id = int(settings.GITHUB_APP_ID)
        private_key_path = Path(settings.GITHUB_PRIVATE_KEY_PATH)
        self.private_key = private_key_path.read_text()

    def generate_jwt(self) -> str:
        """
        Generate a JWT for GitHub App authentication.
        """

        now = int(time.time())
        payload = {
            "iat": now - 60,
            "exp": now + (10 * 60),
            "iss": self.app_id,
        }
        return jwt.encode(
            payload,
            self.private_key,
            algorithm="RS256",
        )

    def get_installation_client(self, installation_id: int) -> Github:
        """
        Returns an authenticated GitHub client
        for a repository installation.
        """

        integration = GithubIntegration(
            auth=self.generate_jwt()
        )

        access_token = integration.get_access_token(
            installation_id
        )

        return Github(access_token.token)