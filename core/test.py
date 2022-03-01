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
repair_icon_path = "data/repair_icon.jpeg"
nibble_image = Vision("data/nibble_image.jpeg")
low_energy_image = Vision("data/low_energy_image.jpeg")
life_skill_icon = Vision("data/life_skill_check.jpeg")
floater_image = Vision("data/floater_image.jpeg")

no_durability_image = Vision("data/no_durability.jpeg")
start_time = time.time()  # start time of the loop
idle_timer = time.time()
catch_counter = 0
initilised = 0



print(RepairTool(repair_icon_path, window_title))
