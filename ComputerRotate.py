import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Footballphoto.png')
imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h, w) = image.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

rotatedrgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotatedrgb)
plt.title("Rotated Image")
plt.axis('off') # Hide axes
plt.show()

brightnessmatrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightnessmatrix)

brighterrgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighterrgb)
plt.title("Brighter Image")
plt.show()