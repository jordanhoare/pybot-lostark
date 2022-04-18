import json

from match_template import MatchTemplate


class FishingBot:
    def __init__(self, screenshot, needle_img):

        with open("pybot_lostark/fishing_bot/config.json", "r") as LoadsJson:
            self.config = json.load(LoadsJson)

        self.screenshot = screenshot
        self.mt = MatchTemplate.find(screenshot)
        # nibble_rectangles = nibble_image.find(screenshot, 0.8)

    def process_screenshot(self):
        self._durability = self.mt(self.config["DURABILITY_NEEDLE"])

    @property
    def has_durability(self):  # -> bool:
        if self._durability:
            return True
