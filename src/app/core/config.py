"""
Application configuration.
"""

from functools import lru_cache
from typing import Any, Dict


class Settings:
    """Application settings."""

    APP_NAME: str = "app"
    DEBUG: bool = False
    
    # Add your configuration settings here
    
    def dict(self) -> Dict[str, Any]:
        """Return settings as a dictionary."""
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


@lru_cache()
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings() 