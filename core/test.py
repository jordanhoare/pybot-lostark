from asyncore import loop
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


def getStatus():
    answer = input("What is the box ID? ")
    if answer == 999:
        return True
    elif type(answer) == int:
        boxId = answer + 1
        print(boxId)


while True:
    if getStatus():
        start = time.time()  # start time of the loop
        screenshot = wincap.get_screenshot()  # get an updated image of the game
        nibble_rectangles = nibble_icon.find(screenshot, 0.75)  # do object detection
        low_energy_rectangles = low_energy.find(screenshot, 0.98)  # do object detection
        output_image = nibble_icon.draw_rectangles(
            screenshot, nibble_rectangles
        )  # draw the detection results onto the original image

        # display the processed image
        output_image = cv.resize(output_image, (960, 540))
        cv.imshow("Lost Ark:  Fishing automation", output_image)

        # bot actions
        if len(nibble_rectangles) > 0:
            pyautogui.press("e")
            catch_counter = catch_counter + 1
            sleep(randint(6, 7))
            pyautogui.click(752, 751)
            sleep(randint(0, 1))
            pyautogui.press("e")
            idle_timer = time.time()  # start time of the loop

        # bot actions
        if len(low_energy_rectangles) > 0:
            print("low energy")

        print("Ended")
    elif cv.waitKey(1) == ord("="):
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
    break


# display the processed image
output_image = cv.resize(output_image, (960, 540))
cv.imshow("Lost Ark:  Fishing automation", output_image)

# bot actions
if len(nibble_rectangles) > 0:
    pyautogui.press("e")
    catch_counter = catch_counter + 1
    sleep(randint(6, 7))
    pyautogui.click(752, 751)
    sleep(randint(0, 1))
    pyautogui.press("e")
    idle_timer = time.time()  # start time of the loop

# bot actions
if len(low_energy_rectangles) > 0:
    print(f">>> Stopping script due to low energy.")

# idle check
if (start - idle_timer) > 14:
    print("The time of the run:", (start - idle_timer))
    print(
        f">>> Script skipped casting for:",
        "{:.3f}".format(1.0 / (start - idle_timer)),
    )
    pyautogui.click(752, 751)
    pyautogui.press("e")


def fishing():
    start = time.time()  # start time of the loop
    screenshot = wincap.get_screenshot()  # get an updated image of the game
    nibble_rectangles = nibble_icon.find(screenshot, 0.75)  # do object detection
    low_energy_rectangles = low_energy.find(screenshot, 0.98)  # do object detection
    output_image = nibble_icon.draw_rectangles(
        screenshot, nibble_rectangles
    )  # draw the detection results onto the original image
    if len(nibble_rectangles) > 0:
        # bot actions
        pyautogui.press("e")
        catch_counter = catch_counter + 1
        sleep(randint(6, 7))
        pyautogui.click(752, 751)
        sleep(randint(0, 1))
        pyautogui.press("e")
        idle_timer = time.time()
    elif len(low_energy_rectangles) > 0:
        print(f">>> Stopping script due to low energy.")
        return True
    elif type(answer) == int:
        boxId = answer + 1
        print(boxId)


loop = True

while loop:
    if fishing():
        print("true")
    elif cv.waitKey(1) == ord("="):
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
        break
