import cv2
from PIL import ImageGrab
import time
import pyautogui
import numpy as np
import keyboard


def auto_pot():
    #Resolution
    res = 4/3

    #Capture boxes
    health = ImageGrab.grab(bbox=(780 * res, 549 * res, 819 * res, 557 * res))

    #Saves img
    health.save("health_bar.png")

    #capture = cv2.imread("cap.png", 1)
    health_bar = cv2.imread("health_bar.png")

    avg_color_row = np.average(health_bar, axis=0)
    avg_color = np.average(avg_color_row, axis=0)
    print(avg_color)
    if avg_color[2] > 50:
        pyautogui.press("f")
        time.sleep(0.3)


def chest_steal():
    if keyboard.is_pressed("c"):
        last_pos = pyautogui.position()

        for item in range(4):
            pyautogui.leftClick(2155 + item * 110, 1265)
            pyautogui.leftClick(2155 + item * 110, 1265)

        pyautogui.moveTo(last_pos)

