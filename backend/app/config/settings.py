from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Application configuration loaded from environment variables or .env."""

    app_name: str = "PrepifyAI Backend"
    environment: str = "local"
    debug: bool = True
    api_version: str = "v1"

    database_url: str = "postgresql+psycopg://user:password@localhost:5432/prepify"
    vector_db_provider: str = "faiss"
    jwt_secret_key: str = "change-me"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = AppSettings()
