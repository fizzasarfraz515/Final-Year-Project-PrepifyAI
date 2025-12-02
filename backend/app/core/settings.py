from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Application configuration loaded from environment variables or .env."""

    app_name: str = "PrepifyAI Backend"
    environment: str = "local"
    debug: bool = True

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = AppSettings()
