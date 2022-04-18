import json

from bot_actions import repair_tool
from fishing_bot import FishingBot
from match_template import MatchTemplate
from window_capture.window_capture import WindowCapture


def main():

    with open("pybot_lostark/fishing_bot/config.json", "r") as LoadsJson:
        config = json.load(LoadsJson)

    wc = WindowCapture(config["WINDOW_TITLE"])
    bot = FishingBot

    while True:
        screenshot = wc.get_screenshot()
        bot.process_screenshot(screenshot)

        if not bot.has_durability:
            repair_tool()


# window_title = "Lost Ark"
# wc = WindowCapture(window_title)
# screenshot = wc.get_screenshot()
# nibble_rectangles = nibble_image.find(screenshot, 0.8)
