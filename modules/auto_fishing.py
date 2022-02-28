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
wincap = WindowCapture()
nibble_icon = Vision("data/nibble_icon.jpeg")
fish_icon = Vision("data/fish_icon.jpeg")
catch_counter = 0

while True:
    start_time = time.time()  # start time of the loop
    screenshot = wincap.get_screenshot()  # get an updated image of the game
    nibble_rectangles = nibble_icon.find(screenshot, 0.75)  # do object detection
    fish_rectangles = fish_icon.find(screenshot, 0.65)  # do object detection
    output_image = nibble_icon.draw_rectangles(
        screenshot, nibble_rectangles
    )  # draw the detection results onto the original image

    # display the processed image
    output_image = cv.resize(output_image, (960, 540))
    cv.imshow("Lost Ark:  Fishing automation", output_image)

    # bot actions
    if len(nibble_rectangles) > 0:
        pyautogui.click(750, 750)
        pyautogui.press("e")
        catch_counter = catch_counter + 1
        sleep(randint(5, 6))
        pyautogui.click(750, 750)
        pyautogui.moveTo(750, 750)
        sleep(randint(0, 1))
        pyautogui.press("e")

    # press '=' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord("="):
        try:
            cv.destroyAllWindows()
            print(f">>> Successfully fished '{catch_counter}' times.")
            print(
                f">>> Average FPS:", "{:.3f}".format(1.0 / (time.time() - start_time))
            )
            print(f"####################################")
        except Exception as Ex:
            print(Ex)
        break
