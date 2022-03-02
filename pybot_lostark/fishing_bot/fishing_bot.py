from config import get_settings
from match_template import MatchTemplate

settings = get_settings()


class FishingBot:
    def __init__(self, match_template: MatchTemplate):
        self.match = match_template.find()

    def process_screenshot(self):
        self._durability = 1

    @property
    def has_durability(self):  # -> bool
        if self._durability:
            print("true")
            return True
        else:
            print("false")
            return False
