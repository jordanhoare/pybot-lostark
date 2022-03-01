import datetime
import os
import sys
import time
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
no_durability_image = Vision("data/no_durability.jpeg")
start_time = time.time()  # start time of the loop
idle_timer = time.time()
catch_counter = 0


def Check_LifeSkill():
    print(f">>> Switching to Trade Skill Quickslot.")
    sleep(randint(0, 1))
    pyautogui.click(750, 750)
    pyautogui.press("b")
    sleep(randint(2, 3))
    pyautogui.click(750, 750)
    pyautogui.press("e")
    sleep(randint(2, 3))


def EnergyCondition():
    if len(low_energy_rectangles) > 0:
        print(f">>> Stopping script due to low energy.")
        return True
    else:
        return False


def idle_check():
    print(f">>> Player has been idling for too long")
    print(f">>> Restarting loop.")
    sleep(randint(0, 1))
    pyautogui.click(750, 750)
    pyautogui.press("e")
    return False


def catch_fish():
    pyautogui.press("e")
    sleep(randint(6, 7))
    pyautogui.click(752, 751)
    sleep(randint(0, 1))
    pyautogui.press("e")
    idle_timer = time.time()  # start time of the loop


def end_process():
    cv.destroyAllWindows()
    stop_time = time.time()
    run_time = "{:.3f}".format((stop_time - start_time))
    print(f">>> Successful fishing attempts: {catch_counter}.")
    print(f">>> Script finished after:", str(datetime.timedelta(seconds=run_time)))
    print(f"####################################")


while True:
    screenshot = wincap.get_screenshot()  # get an updated image of the game

    # render object detection images
    nibble_rectangles = nibble_image.find(screenshot, 0.75)
    life_skill_activated = life_skill_icon.find(screenshot, 0.88)
    low_energy_rectangles = low_energy_image.find(screenshot, 0.96)
    floater_rectangles = floater_image.find(screenshot, 0.90)
    no_durability_check = no_durability_image.find(screenshot, 0.90)

    # draw the detection results onto the original image
    output_image = nibble_image.draw_rectangles(screenshot, nibble_rectangles)

    # display the processed image
    output_image = cv.resize(output_image, (960, 540))
    cv.imshow("Lost Ark:  Fishing automation", output_image)

    # nibble check
    if len(nibble_rectangles) > 0:
        catch_fish()
        catch_counter = catch_counter + 1
    elif len(life_skill_activated) < 1:
        Check_LifeSkill()
    elif len(no_durability_check) > 0:
        print(f">>> No durability left on your tool.")
        try:
            end_process()
        except Exception as Ex:
            print(Ex)
        break
    elif cv.waitKey(1) == ord("=") or EnergyCondition():
        try:
            end_process()
        except Exception as Ex:
            print(Ex)
        break
