import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
import time
from pytesseract import pytesseract as pt

pt.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

while True:
    cap = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    health = ImageGrab.grab(bbox=(1650, 450, 1820, 500))
    time.sleep(0.2)
    health.save("health.png", 0)
    cap.save("cap.png")

    capture = cv2.imread("cap.png", 1)

    health = cv2.imread("health.png")
    health = cv2.resize(health, (0, 0), fx=7, fy=7)
    health_number = pytesseract.image_to_string(health)

    print(health_number)

    capture = cv2.rectangle(capture, pt1=(1650, 450), pt2=(1820, 500), color=(255, 0, 0), thickness=5)
    cv2.imshow("ROTMG script", capture)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
