import os
import sys
from random import randint
from time import sleep

import cv2 as cv
import pyautogui

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.vision import Vision
from core.window_capture import WindowCapture


class RepairTool:
    """
    If there is no durability left on your tool:
     > create a new window capture instance in the background
     > navigate to the pet repair window using hotkeys
     > return the window co-ords of the repair_tool_icon & repair all button
     > repair tools on person then close the pet window

    @ takes: repair_icon_path, window_title
    @ returns:

    """

    # properties
    catch_counter = 0

    def __init__(self, repair_icon_path, window_title):

        # initialize the capture classes
        self.wincap = WindowCapture(window_title)
        self.repair_tool_icon = Vision(repair_icon_path)

        # Console log call to repair function
        print(f">>> No durability left on your tool. Attempting to repair tools.")
        sleep(randint(0, 1))
        self.repair_tool()

    def repair_tool(self):

        # Open up pet repair window
        pyautogui.keyDown("alt")
        pyautogui.press("p")
        pyautogui.keyUp("alt")
        sleep(randint(4, 5))

        while True:
            screenshot = (
                self.wincap.get_screenshot()
            )  # get an updated image of the game

            # render object detection images
            repair_rectangles = self.repair_tool_icon.find(screenshot, 0.85)

            # repair_rectangles check
            if len(repair_rectangles) > 0:

                # For debugging
                # self.result = ">>> Found repair tool icon"
                # print(self.result)
                sleep(randint(2, 3))

                # repair tools
                targets = Vision.get_click_points(repair_rectangles)
                target = self.wincap.get_screen_position(targets[0])
                pyautogui.moveTo(x=target[0], y=target[1])
                sleep(randint(0, 1))
                pyautogui.click
                sleep(randint(0, 1))

                # close pet window
                print(f">>> Closing repair window and restarting bot.")
                sleep(randint(2, 3))
                pyautogui.keyDown("alt")
                pyautogui.press("p")
                pyautogui.keyUp("alt")
                sleep(randint(2, 3))
                break

    # def get_click_points(self, rectangles):
    #     """
    #     given a list of [x, y, w, h] rectangles returned by find(), convert those into a list of
    #     [x, y] positions in the center of those rectangles where we can click on those found items
    #     """

    #     points = []

    #     # Loop over all the rectangles
    #     for (x, y, w, h) in rectangles:
    #         # Determine the center position
    #         center_x = x + int(w / 2)
    #         center_y = y + int(h / 2)
    #         # Save the points
    #         points.append((center_x, center_y))

    #     return points
