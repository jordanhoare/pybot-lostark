from random import randint
from time import sleep

import pyautogui

from ..window_capture.vision import Vision
from ..window_capture.window_capture import WindowCapture


class RepairTool:
    """
    If there is no durability left on your tool:
     > create a new window capture instance in the background
     > navigate to the pet repair window using hotkeys
     > return the window co-ords of the repair_tool_icon & repair_all_button & repair_all_ok
     > repair tools on person then close the pet window

    @ takes: repair_icon_path, window_title
    @ returns:

    """

    # properties
    catch_counter = 0
    repair_all_button_path = "data/repair_all_button.jpeg"
    repair_all_ok_path = "data/repair_all_ok.jpeg"
    repair_icon_path = "data/repair_icon.jpeg"

    def __init__(self, window_title):

        # initialize the capture classes
        self.wincap = WindowCapture(window_title)
        self.repair_tool_icon = Vision(self.repair_icon_path)
        self.repair_all_button = Vision(self.repair_all_button_path)
        self.repair_all_ok_button = Vision(self.repair_all_ok_path)

        # Console log call to repair function
        print(">>> No durability left on your tool. Attempting to repair tools.")
        sleep(randint(0, 1))
        self.repair_tool()

    def get_click_points(self, rectangles):
        # given a list of [x, y, w, h] rectangles returned by find(), convert those into a list of
        # [x, y] positions in the center of those rectangles where we can click on those found items
        points = []

        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            # Save the points
            points.append((center_x, center_y))
        return points

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
            repair_ok_button_rectangles = self.repair_all_ok_button.find(
                screenshot, 0.90
            )

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

            ########################
            # throw an idle timer here incase someone has no Crystaline Aura
            ########################
