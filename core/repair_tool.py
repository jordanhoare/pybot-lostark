import os
import sys
import time
from datetime import timedelta
from random import randint
from time import sleep

import cv2 as cv
import numpy as np
import pyautogui

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.vision import Vision
from core.window_capture import WindowCapture

######
######
######
######
######
######
######
######
######
######
######

# initialize the capture classes and counters
window_title = "Lost Ark"
wincap = WindowCapture(window_title)
nibble_image = Vision("data/nibble_image.jpeg")
low_energy_image = Vision("data/low_energy_image.jpeg")
life_skill_icon = Vision("data/life_skill_check.jpeg")
floater_image = Vision("data/floater_image.jpeg")
repair_tool_icon = Vision("data/repair_icon.jpeg")
no_durability_image = Vision("data/no_durability.jpeg")
start_time = time.time()  # start time of the loop
idle_timer = time.time()
catch_counter = 0


def repair_tool():
    print(f">>> No durability left on your tool.")
    sleep(randint(0, 1))

    # Open up pet repair window
    pyautogui.keyDown("alt")
    pyautogui.press("p")
    pyautogui.keyUp("alt")
    sleep(randint(4, 5))

    while True:
        screenshot = wincap.get_screenshot()  # get an updated image of the game

        # render object detection images
        repair_rectangles = repair_tool_icon.find(screenshot, 0.85)

        # nibble check
        if len(repair_rectangles) > 0:
            print(f">>> Found repair tool icon")
            sleep(randint(2, 3))
            return True
        else:
            print(f">>> Was not able to repair tool.")
            sleep(randint(2, 3))
            return False
