from random import randint
from time import sleep, time

import cv2 as cv
import numpy as np
import pyautogui
from vision import Vision
from windowcapture import WindowCapture

########## USE TO FIND WINDOW TITLE
### WindowCapture.list_window_names()
### exit()
##########

# properties
window_title = "LOST ARK (64-bit, DX11) v.2.0.2.1"
icon = cv.imread("fishing/.icon.jpeg", cv.IMREAD_UNCHANGED)

# initialize the WindowCapture class
wincap = WindowCapture(window_title)

# initialize the Vision class
fishing_icon = Vision("data/fishing_icon.png")

loop_time = time()
while True:

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # do object detectione
    rectangles = fishing_icon.find(screenshot, 0.75)

    # draw the detection results onto the original image
    output_image = fishing_icon.draw_rectangles(screenshot, rectangles)

    # display the processed image
    # cv.imshow("Matches", output_image)

    # take bot actions
    if len(rectangles) > 0:
        pyautogui.press("e")
        sleep(randint(6, 7))
        pyautogui.press("e")
        sleep(1)

    # # # debug the loop rate
    # print("FPS {}".format(1 / (time() - loop_time)))
    # loop_time = time()

    # press '=' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord("="):
        cv.destroyAllWindows()
        break

print("Finished.")
