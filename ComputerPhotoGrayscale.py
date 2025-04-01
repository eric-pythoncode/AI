import cv2

image = cv2.imread("FootballPhoto.png")

grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resizedimage = cv2.resize(grayimage, (224, 224))

cv2.imshow("Processed Image", resizedimage)

key = cv2.waitKey(0)

if key == ord("s"):
    cv2.imwrite('grayscaleresizedimage.jpg', resizedimage)
    print("Image saved as a grayscaleresizedjpg")
else:
    print("Image not saved")

cv2.destroyAllWindows()

print(f"Processed image dimensions: {resizedimage.shape}")
