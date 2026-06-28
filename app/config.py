from fastapi import FastAPI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Github PR review agent"
    GITHUB_APP_ID: str
    GITHUB_CLIENT_ID: str
    GITHUB_WEBHOOK_SECRET :str
    GITHUB_PRIVATE_KEY_PATH: str

    model_config = SettingConfigDict(env_file=".env",extra ="ignore")

    @lru_cache
    def get_settings():
        return Settings()

    settings = get_settings()
    