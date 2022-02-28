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
fishing_icon = Vision("data/fishing_icon.jpeg")

while True:
    start_time = time.time()  # start time of the loop
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # do object detection
    rectangles = fishing_icon.find(screenshot, 0.75)

    # draw the detection results onto the original image
    output_image = fishing_icon.draw_rectangles(screenshot, rectangles)

    # display the processed image
    output_image = cv.resize(output_image, (960, 540))
    cv.imshow("Lost Ark:  Fishing automation", output_image)

    # take bot actions
    if len(rectangles) > 0:
        pyautogui.press("e")
        sleep(randint(6, 7))
        pyautogui.press("e")
        sleep(1)

    # press '=' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord("="):
        try:
            cv.destroyAllWindows()
            print(">>> Average FPS:", "{:.3f}".format(1.0 / (time.time() - start_time)))
            print(">>> Instance closed.")
            print(f"####################################")
        except Exception as Ex:
            print(Ex)
        break
