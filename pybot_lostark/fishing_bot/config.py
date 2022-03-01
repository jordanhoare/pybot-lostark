from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENERGY_THRESHOLD: int = 0.9


@lru_cache
def get_settings():
    return Settings()
