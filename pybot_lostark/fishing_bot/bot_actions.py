from random import randint
from time import sleep

import pyautogui

from ..match_template.match_template import Vision
from ..window_capture.window_capture import WindowCapture


def repair_tool(self):

    # Open up pet repair window
    pyautogui.keyDown("alt")
    pyautogui.press("p")
    pyautogui.keyUp("alt")
    sleep(randint(4, 5))

    while True:
        # get an updated image of the game
        screenshot = self.wincap.get_screenshot()

        # render object detection images
        self.repair_rectangles = self.repair_tool_icon.find(screenshot, 0.85)
        repair_button_rectangles = self.repair_all_button.find(screenshot, 0.90)
        repair_ok_button_rectangles = self.repair_all_ok_button.find(screenshot, 0.90)

        # given a list of [x, y, w, h] rectangles returned by find(), convert those into a list of
        # [x, y] positions in the center of those rectangles where we can click on those found items
        if len(self.repair_rectangles) > 0:
            targets = self.get_click_points(self.repair_rectangles)
            target = self.wincap.get_screen_position(targets[0])
            sleep(randint(0, 1))
            pyautogui.moveTo(x=target[0], y=target[1])
            sleep(randint(1, 2))
            pyautogui.click(clicks=2)
            sleep(randint(1, 2))

        if len(repair_button_rectangles) > 0:
            # repair tools
            targets = self.get_click_points(repair_button_rectangles)
            target = self.wincap.get_screen_position(targets[0])
            sleep(randint(1, 2))
            pyautogui.moveTo(x=target[0], y=target[1])
            sleep(randint(1, 2))
            pyautogui.click(clicks=2)
            sleep(randint(1, 2))

        if len(repair_ok_button_rectangles) > 0:
            # repair tools
            targets = self.get_click_points(repair_ok_button_rectangles)
            target = self.wincap.get_screen_position(targets[0])
            sleep(randint(1, 2))
            pyautogui.moveTo(x=target[0], y=target[1])
            sleep(randint(1, 2))
            pyautogui.click(clicks=2)
            sleep(randint(2, 3))

            # close pet window
            print(">>> Closing repair window and restarting bot.")
            pyautogui.press("esc")
            sleep(randint(0, 1))
            pyautogui.press("esc")
            sleep(randint(0, 1))
            pyautogui.press("esc")
            sleep(randint(0, 3))
            break
