import cv2
import numpy as np

canvas = np.ones((600, 600, 3), dtype=np.uint8) * 255

drawing = False
ix, iy = -1, -1
color = (0, 0, 255)

def draw(event, x, y, flags, param):
    global ix, iy, drawing, color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(canvas, (ix, iy), (x, y), color, thickness=3)
            ix, iy = x, y
        

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(canvas, (ix, iy), (x, y), color, thickness=3)

cv2.namedWindow("Doodle Board")
cv2.setMouseCallback("Doodle Board", draw)

while True:
    cv2.imshow("Doodle Board", canvas)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        color = (0, 0, 255)
    if key == ord('g'):
        color = (0, 255, 0)
    if key == ord('b'):
        color = (255, 0, 0)
    if key == ord('c'):
        canvas[:] = 255
    if key == ord('q'):
        break

cv2.destroyAllWindows()