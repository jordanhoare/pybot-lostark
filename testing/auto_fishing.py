import os
import sys
import time
from datetime import timedelta
from random import randint
from time import sleep

import cv2 as cv
import numpy as np
import pyautogui
import pygetwindow as gw
import win32gui
from sqlalchemy import false

from .config import get_settings

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.repair_tool import RepairTool
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

no_durability_image = Vision("data/no_durability.jpeg")
start_time = time.time()  # start time of the loop
idle_timer = time.time()
catch_counter = 0
initilised = 0


from pyautogui import click, press


def random_sleep(min_time: int = 0, max_time: int = 1) -> None:
    sleep(randint(0, 1))


def begin_fishing():
    click(750, 750)
    random_sleep()
    press("e")


def change_quickslot():
    print(">>> Switching to Trade Skill Quickslot.")
    random_sleep()
    # select window
    pyautogui.press("b")
    random_sleep(2, 3)
    # select window
    pyautogui.press("e")
    sleep(randint(2, 3))


def low_energy():
    if len(low_energy_rectangles) > 0:
        print(">>> Stopping script due to low energy.")
        return True
    else:
        return False


def idle_check():
    print(">>> Player has been idling for too long")
    print(">>> Restarting loop.")
    sleep(randint(0, 1))
    pyautogui.click(750, 750)
    pyautogui.press("e")
    return False


def catch_fish():
    pyautogui.press("e")
    sleep(randint(7, 8))
    pyautogui.click(752, 751)
    sleep(randint(0, 1))
    pyautogui.press("e")
    idle_timer = time.time()  # start time of the loop


def end_process():
    cv.destroyAllWindows()
    stop_time = time.time()
    run_time = int((stop_time - start_time))
    # print(f">>> Successful attempts: {catch_counter}")
    print(f">>> Script finished after:", "{:0>8}"(str(timedelta(seconds=run_time))))
    print(f"####################################")


def initilise_fishing():
    a = gw.getWindowsWithTitle(window_title)
    a = str(a)
    b = a.split("=", 1)
    b = b[1].split(")", 1)
    hwnd = int(b[0])
    print(f"####################################")
    print(f">>> {window_title} ({hwnd}) window was located.")


while True:
    set_idle_time = time.time()
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # render object detection images
    nibble_rectangles = nibble_image.find(screenshot, 0.8)
    life_skill_activated = life_skill_icon.find(screenshot, 0.90)
    low_energy_rectangles = low_energy_image.find(
        screenshot, 0.8
    )  # settings.ENERGY_THRESHOLD

    floater_rectangles = floater_image.find(screenshot, 0.90)
    no_durability_check = no_durability_image.find(screenshot, 0.70)

    # draw the detection results onto the original image
    # display the processed image
    output_image = nibble_image.draw_rectangles(screenshot, nibble_rectangles)
    output_image = cv.resize(screenshot, (960, 540))
    cv.imshow("Lost Ark:  Fishing automation", output_image)

    # bot actions
    if initilised == 0:
        initilised = 1
        initilise_fishing()
        if len(life_skill_activated) > 0:
            change_quickslot()
        else:
            print(">>> Trade Skill Quickslot is already selected.")
            begin_fishing()
    if len(no_durability_check) > 0:
        RepairTool(window_title)
        begin_fishing()
        if len(no_durability_check) > 0:
            print(">>> Terminating bot - was not able to repair tool.")
            end_process()
            break
    if (set_idle_time - idle_timer) > 90:
        idle_in_seconds = int((set_idle_time - idle_timer))
        print(
            ">>> Restarting bot... Idled for:",
            "{:0>8}".format(str(timedelta(seconds=idle_in_seconds))),
        )
        idle_timer = time.time()
        begin_fishing()
    if len(nibble_rectangles) > 0:
        catch_fish()
        catch_counter = catch_counter + 1
    elif cv.waitKey(1) == ord("=") or low_energy():
        try:
            end_process()
        except Exception as Ex:
            print(Ex)
        break

    elif (
        cv.waitKey(1) == ord("=")
        or low_energy()
        or no_durability_check()
        or no_durability_check()
        or no_durability_check()
    ):
        try:
            end_process()
        except Exception as Ex:
            print(Ex)
        break


# Bot class -> handles all basic check
# # child class
