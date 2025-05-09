import cv2
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# Volume setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

cap = cv2.VideoCapture(0)

def get_hand_center(contour):
    M = cv2.moments(contour)
    if M["m00"] == 0:
        return None
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    return cx, cy

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    roi = frame[100:400, 100:400]
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Skin color range (can be adjusted for different lighting)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_cnt = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(max_cnt)

        if area > 1000:
            cx, cy = get_hand_center(max_cnt)

            # Map vertical movement to volume (0-100%)
            vol = np.interp(cy, [100, 400], [100, 0])
            volume.SetMasterVolumeLevelScalar(vol / 100, None)

            # Map horizontal movement to brightness (0-100%)
            bright = np.interp(cx, [100, 400], [0, 100])
            sbc.set_brightness(int(bright))

            cv2.drawContours(roi, [max_cnt], -1, (0, 255, 0), 2)
            cv2.circle(roi, (cx, cy), 8, (255, 0, 0), -1)
            cv2.putText(frame, f'Volume: {int(vol)}%', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            cv2.putText(frame, f'Brightness: {int(bright)}%', (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.rectangle(frame, (100, 100), (400, 400), (255, 0, 0), 2)
    cv2.imshow("Hand Gesture Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
