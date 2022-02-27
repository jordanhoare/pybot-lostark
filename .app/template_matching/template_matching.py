import cv2 as cv
import numpy as np

# https://docs.opencv.org/4.5.5/
# OpenCV Images
haystack_img = cv.imread(
    "D:/CompSci/Projects/lostark-bot/data/full-screenshot.png", cv.IMREAD_UNCHANGED
)
needle_img = cv.imread(
    "D:/CompSci/Projects/lostark-bot/data/mining-icon.png", cv.IMREAD_UNCHANGED
)


result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

cv.imshow("Result", result)
cv.waitKey()
