import secrets
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    PROJECT_NAME: str = "Email Marketing Platform"
    VERSION: str = "0.1.0"

    # Database
    DATABASE_URL: str = "mysql+pymysql://appuser:app_password@localhost:3306/email_marketing"

    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

settings = Settings()