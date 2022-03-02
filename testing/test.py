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

    def process_screenshot(self, screenshot):
        self._durability = self.match.find(screenshot, settings.DURABILITY_THRESHOLD)

    @property
    def has_durability(self) -> bool:
        if self._durability:
            return True
        else:
            return False


FishingBot()
