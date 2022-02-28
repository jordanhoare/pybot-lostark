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

while True:
    start = time.time()  # start time of the loop
    screenshot = wincap.get_screenshot()  # get an updated image of the game
    nibble_rectangles = nibble_icon.find(screenshot, 0.75)  # do object detection
    low_energy_rectangles = low_energy.find(screenshot, 0.92)  # do object detection
    output_image = nibble_icon.draw_rectangles(
        screenshot, nibble_rectangles
    )  # draw the detection results onto the original image

    # display the processed image
    output_image = cv.resize(output_image, (960, 540))
    cv.imshow("Lost Ark:  Fishing automation", output_image)

    # nibble check
    if len(nibble_rectangles) > 0:
        pyautogui.press("e")
        catch_counter = catch_counter + 1
        sleep(randint(6, 7))
        pyautogui.click(752, 751)
        sleep(randint(0, 1))
        pyautogui.press("e")
        idle_timer = time.time()  # start time of the loop

    # # life skill check
    # if len(low_energy_rectangles) > 0:
    #     print(f">>> Stopping script due to low energy.")
    #     loop = False

    # low-energy check
    if len(low_energy_rectangles) > 0:
        print(f">>> Stopping script due to low energy.")
        low_energy_check = True

    # idle check
    if (start - idle_timer) > 14:
        print("The time of the run:", (start - idle_timer))
        print(
            f">>> Script skipped casting for:",
            "{:.3f}".format(1.0 / (start - idle_timer)),
        )
        pyautogui.click(752, 751)
        pyautogui.press("e")

    # press '=' with the output window focused to exit.

    if cv.waitKey(1) == ord("=") or low_energy_check:
        try:
            cv.destroyAllWindows()
            stop_time = time.time()
            total_time = stop_time - start_time
            print(f">>> Successful fishing attempts: '{catch_counter}'.")
            print(f"####################################")
        except Exception as Ex:
            print(Ex)
        break
