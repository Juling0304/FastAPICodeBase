from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GPT_API_KEY: str
    CLAUDE_API_KEY: str
    API_PORT: int
    APP_ENV: str

    REDIS_HOST_NAME: str
    REDIS_PORT: int
    # model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


origins: list[str] = ["*"]
BASE_PATH: Path = Path().resolve()
