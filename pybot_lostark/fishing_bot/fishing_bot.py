from calendar import c
from re import A
from typing import Optional

from pyrsistent import b

from .config import get_settings

settings = get_settings()

settings.ENERGY_THRESHOLD

class FishingBot:
    def __init__(self, vision_handler: VisionHandler):
        self.vision_handler = vision_handler

    def process_screenshot(screenshot)
        self.A = self.vision_handler.get_durability(screenshot)
        self.b = self.vision_handler.get_durability(screenshot)
        self.c = self.vision_handler.get_durability(screenshot)
        self.dict = self.vision_handler.get_durability(screenshot)
        self.durability = self.vision_handler.get_durability(screenshot)
    
    @property
    def has_durability() -> bool:
        if self.durability:
            return True
        else:
            return False

    @property
    def has_energy() -> bool:
        if self.a:
            return True
        else:
            return False

    @property
    def has_nibble() -> bool:
        if self.b:
            return True
        else:
            return False










    if len(no_durability_check) > 0:
        RepairTool(window_title)
        begin_fishing()
        if len(no_durability_check) > 0:
            print(">>> Terminating bot - was not able to repair tool.")
            end_process()
            break
