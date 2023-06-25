"""Application config."""
from functools import lru_cache

from pydantic import BaseSettings, Field


class Config(BaseSettings):
    """Application config."""

    service: str = 'server'
    version: str = Field(default='0.0.1')
    env: str = 'dev'


@lru_cache
def get_config() -> Config:
    """
    Return application config.

    :return: Application config
    """
    return Config()
