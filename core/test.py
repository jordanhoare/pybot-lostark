import os
import sys
import time
from ast import While
from asyncore import loop
from pickle import TRUE
from random import randint
from time import sleep

import cv2 as cv
import numpy as np
import pyautogui
from sqlalchemy import false

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

# initialize the capture classes

window_title = "Lost Ark"
wincap = WindowCapture(window_title)
nibble_icon = Vision("data/nibble_icon.jpeg")
low_energy = Vision("data/low_energy.jpeg")
catch_counter = 0

# bot actions
sleep(randint(0, 1))
pyautogui.click(750, 750)
pyautogui.press("e")
start_time = time.time()  # start time of the loop
idle_timer = time.time()

low_energy_check = False


def le_fish():
    while True:
        """
        all true for it to fish
        """
        fishing()


def fishing():
    print("Init")

    # nibble check
    if len(nibble_rectangles) > 0:
        pyautogui.press("e")
        catch_counter = catch_counter + 1
        sleep(randint(6, 7))
        pyautogui.click(752, 751)
        sleep(randint(0, 1))
        pyautogui.press("e")
        idle_timer = time.time()  # start time of the loop

        print("Nibble Check")
    print("END")


def end_process():
    try:
        cv.destroyAllWindows()
        stop_time = time.time()
        total_time = stop_time - start_time
        print(f">>> Successful fishing attempts: '{catch_counter}' times.")
        print(
            f">>> Script finished after:",
            "{:.3f}".format(1.0 / (start - idle_timer)),
        )
        print(f"####################################")
    except Exception as Ex:
        print(Ex)


def idle_check():
    if (start - idle_timer) < 15:
        return True
    else:
        print("spam e")
        return False


while True:
    start = time.time()
    screenshot = wincap.get_screenshot()
    nibble_rectangles = nibble_icon.find(screenshot, 0.75)
    low_energy_rectangles = low_energy.find(screenshot, 0.92)
    output_image = nibble_icon.draw_rectangles(screenshot, nibble_rectangles)
    # display the processed image

    output_image = cv.resize(output_image, (960, 540))
    cv.imshow("Lost Ark:  Fishing automation", output_image)

    if cv.waitKey(1) == ord("="):
        end_process()
        break
