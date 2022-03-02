from functools import lru_cache

from pydantic import BaseSettings

# life_skill_activated = life_skill_icon.find(screenshot, 0.90)


class Template(BaseSettings):
    NIBBLE_NEEDLE: str = "data/low_energy_image.jpeg"
    NIBBLE_THRESHOLD: int = 0.80
    DURABILITY_NEEDLE: str = "data/low_energy_image.jpeg"
    DURABILITY_THRESHOLD: int = 0.80


@lru_cache
def get_settings():
    return Template()
