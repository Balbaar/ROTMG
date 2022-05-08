import cv2
from PIL import ImageGrab
import time
import pyautogui

while True:
    #Capture boxes
    cap = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    health = ImageGrab.grab(bbox=(748, 545, 810, 555))

    #Wait time
    time.sleep(0.2)

    #Saves img
    cap.save("cap.png")
    health.save("health_bar.png")

    capture = cv2.imread("cap.png", 1)
    health_bar = cv2.imread("health.png", 0)
    example = cv2.imread("health_ex.png")



    capture = cv2.rectangle(capture, pt1=(748, 545), pt2=(810, 555), color=(255, 0, 0), thickness=2)
    cv2.imshow("ROTMG script", capture)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
