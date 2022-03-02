from functools import lru_cache

from pydantic import BaseSettings


class Template(BaseSettings):
    NIBBLE_NEEDLE: str = "data/low_energy_image.jpeg"
    NIBBLE_THRESHOLD: int = 0.80
    DURABILITY_NEEDLE: str = "data/low_energy_image.jpeg"
    DURABILITY_THRESHOLD: int = 0.80


@lru_cache
def get_settings():
    return Template()


settings = get_settings()


class FishingBot:
    def __init__(self):
        self.process_screenshot()

    def process_screenshot(self):
        self.xyz = "content"
        print(self.has_energy)

    @property
    def has_energy(self) -> bool:
        if self.xyz:
            return True
        else:
            return False


FishingBot()
