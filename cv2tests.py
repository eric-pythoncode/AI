import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities.IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from math import hypot
import screeen_brightness_control as sbc

mphands = mp.solutions.hands
hands = mphands.Hands(mindetectionconfidence-.7, mintrackingconfidence=.7)
mpdraw = mp.solutions.drawingutils

try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndPointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndPointVolume)
    volumerange = volume.GetVolumeRange()
    minvol = volumerange[0]
    maxvol = volumerange[1]
except Exception as e:
    print(f"Error initializing Pycaw: {e}")
    exit()

cap = cv2.VideoCapture(0)
if not cap.IsOpened():
    print("Error: could not access the webcam")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame from webcam")
        break

    img = cv2.flip(img, 1)
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgrgb)

    if results.multihandlandmarks and results.multihandedness:
        for i, handlandmarks in enumerate(results.multihandlandmarks):
            handlabel = results.mutlihandedness[i].classification[0].label

            mpdraw.drawlandmarks(img, handlandmarks, mphands.HAND_CONNECTIONS)
            