import cv2
import matplotlib.pyplot as plt

imagepath = 'FootballPhoto.png'
image = cv2.imread(imagepath)

imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _ = imagergb.shape

rect1width, rect1height = 150, 150
topleft1 = (20, 20)
bottomright1 = (topleft1[0] + rect1width, topleft1[1] + rect1height)
cv2.rectangle(imagergb, topleft1, bottomright1, (0, 255, 255), 3)

rect2width, rect2height = 200, 150
topleft2 = (width - rect2width - 20, height - rect2height - 20)
bottomright2 = (topleft2[0] + rect2width, topleft2[1] + rect2height)
cv2.rectangle(imagergb, topleft2, bottomright2, (255, 0, 255), 3)

center1x = topleft1[0] + rect1width // 2
center1y = topleft1[1] + rect1height // 2
center2x = topleft2[0] + rect2width // 2
center2y = topleft2[1] + rect2height // 2

cv2.circle(imagergb, (center1x, center1y), 15, (0, 255, 0), -1)
cv2.circle(imagergb, (center2x, center2y), 15, (0, 0, 255), -1)

cv2.line(imagergb, (center1x, center1y), (center2x, center2y), (0, 255, 0), 3)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(imagergb, "Region 1", (topleft1[0], topleft1[1] - 10), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(imagergb, "Region 2", (topleft2[0], topleft2[1] - 10), font, 0.7, (255, 0, 255), 2, cv2.LINE_AA)
cv2.putText(imagergb, "Center 1", (center1x - 40, center1y + 40), font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(imagergb, "Center 2", (center2x - 40, center2y + 40), font, 0.6, (0, 0, 255), 2, cv2.LINE_AA)

arrowstart = (width - 50, 20)
arrowend = (width - 50, height - 20)

cv2.arrowedLine(imagergb, arrowstart, arrowend, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(imagergb, arrowend, arrowstart, (255, 255, 0), 3, tipLength=0.05)

heightlabelposition = (arrowstart[0] - 150, (arrowstart[1] + arrowend[1]) // 2)
cv2.putText(imagergb, f"Height: {height}px", heightlabelposition, font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)

plt.figure(figsize=(12, 8))
plt.imshow(imagergb)
plt.title("Annotated image with Regions, Centers, and Bi-Directional height arrow.")
plt.axis('off')
plt.show()