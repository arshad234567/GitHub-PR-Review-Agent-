from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "GitHub PR Review Agent"
    APP_VERSION: str = "1.0.0"

    GITHUB_APP_ID: str
    GITHUB_CLIENT_ID: str
    GITHUB_WEBHOOK_SECRET: str
    GITHUB_PRIVATE_KEY_PATH: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

@lru_cache
def get_settings():
    return Settings()
settings = get_settings()

