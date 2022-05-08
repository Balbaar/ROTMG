import cv2
from PIL import ImageGrab
import time
import pyautogui
import numpy as np


while True:
    #Capture boxes
    cap = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    health = ImageGrab.grab(bbox=(748, 545, 810, 555))

    #Saves img
    cap.save("cap.png")
    health.save("health_bar.png")

    capture = cv2.imread("cap.png", 1)
    health_bar = cv2.imread("health_bar.png")
    example = cv2.imread("health_ex.png")

    avg_color_row = np.average(health_bar, axis=0)
    avg_color = np.average(avg_color_row, axis=0)
    print(avg_color)
    if 35 > avg_color[0] > 25:
        pyautogui.press("f")
        time.sleep(0.3)

    capture = cv2.rectangle(capture, pt1=(748, 545), pt2=(810, 555), color=(255, 0, 0), thickness=2)
    #cv2.imshow("ROTMG script", capture)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
