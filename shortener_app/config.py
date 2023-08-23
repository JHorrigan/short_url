# shortener_app/config.py

from functools import lru_cache

# Pydantic uses type annotation to validate data & manage settings
from pydantic import BaseSettings

class Settings(BaseSettings):

    # Fallback settings to be overidden
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    # Load settings from .env through pydantic
    class Config:
        env_file = ".env"

@lru_cache # Cache settings with LRU (Least Recently Used) strategy
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings # Return an instance of the settings class