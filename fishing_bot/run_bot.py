from core import vision

from core.bot_actions import (
    repair_tool,
    repair_tool,
    repair_tool,
    repair_tool,
    repair_tool,
    repair_tool,
)


def main() -> None:
    vh = VisionHandler()
    bot = FishingBot(vh)

    while True:
        screenshot = None

        bot.process_screenshot(screenshot)

        if not bot.has_energy:
            exit()

        if not bot.has_durability:
            repair_tool()
            continue

        if bot.has_nibble_icon:
            catch_fish()
            continue
