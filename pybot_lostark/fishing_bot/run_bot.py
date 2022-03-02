from fishing_bot import FishingBot
from match_template import MatchTemplate


def main() -> None:
    vh = MatchTemplate()
    bot = FishingBot(vh)

    while True:
        screenshot = None

        bot.process_screenshot(screenshot)

        if not bot.has_durability:
            continue
