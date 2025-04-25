import cv2
import numpy as np

def applyfilter (image, filtertype):
    filteredimage = image.copy()

    if filtertype == "red_tint":
        filteredimage[:, :, 1] = 0 #green 0
        filteredimage[:, :, 0] = 0 #blue 0
    if filtertype == "green_tint":
        filteredimage[:, :, 0] = 0 #green 0
        filteredimage[:, :, 2] = 0 #blue 0
    if filtertype == "blue_tint":
        filteredimage[:, :, 1] = 0 #green 0
        filteredimage[:, :, 2] = 0 #blue 0
    if filtertype == "sobel":
        grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(grayimage, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(grayimage, cv2.CV_64F, 0, 1, ksize=3)
        combinedsobel = cv2.bitwise_or(sobelx.astype('uint8'), sobely.astype('uint8'))
        filteredimage = cv2.cvtColor(combinedsobel, cv2.COLOR_GRAY2BGR)
    elif filtertype == "canny":
        grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(grayimage, 100, 200)
        filteredimage = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

    return filteredimage

imagepath = 'FootballPhoto.png'
image = cv2.imread(imagepath)
if image is None:
    print("Error: Image not found")
else:
    filtertype = "original"

    print("Press the following to apply filters:")
    print("R - Red tint")
    print("G - Green tint")
    print("B - Blue tint")
    print("S - Sobel Edge Detection")
    print("C - Canny Image Detection")
    print("Q - Quit")

    while True:
        filteredimage = applyfilter(image, filtertype)

        cv2.imshow("Filtered Image", filteredimage)

        key = cv2.waitKey(0) & 0xFF

        if key == ord("r"):
            filtertype = "red_tint"
        if key == ord("g"):
            filtertype = "green_tint"
        if key == ord("b"):
            filtertype = "blue_tint"
        if key == ord("s"):
            filtertype = "sobel"
        if key == ord("c"):
            filtertype = "canny"
        if key == ord("q"):
            print("Exiting . . .")
            break
        else:
            print("Invalid key! Use R, G, B, S, C, or Q")
cv2.destroyAllWindows()