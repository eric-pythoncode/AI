import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
prev_y = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerskin = np.array([0, 30, 60], dtype=np.uint8)
    upperskin = np.array([20, 150, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lowerskin, upperskin)
    mask = cv2.dilate(mask, None, iterations=2)
    mask = cv2.GaussianBlur(mask, (5, 5), 100)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        maxcontour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(maxcontour) > 2000:
            x, y, w, h = cv2.boundingRect(maxcontour)
            centery = y + h // 2

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (x + w // 2, centery), 5, (0, 255, 0), -1)

            if prev_y is not None:
                dv = centery - prev_y
                if abs(dv) > 10:
                    pyautogui.scroll(-dv)

            prev_y = centery

    cv2.imshow('Hand Scroll', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
