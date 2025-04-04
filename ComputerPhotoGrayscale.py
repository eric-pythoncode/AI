import ComputerRGB

image = ComputerRGB.imread("FootballPhoto.png")

grayimage = ComputerRGB.cvtColor(image, ComputerRGB.COLOR_BGR2GRAY)

resizedimage = ComputerRGB.resize(grayimage, (224, 224))

ComputerRGB.imshow("Processed Image", resizedimage)

key = ComputerRGB.waitKey(0)

if key == ord("s"):
    ComputerRGB.imwrite('grayscaleresizedimage.jpg', resizedimage)
    print("Image saved as a grayscaleresizedjpg")
else:
    print("Image not saved")

ComputerRGB.destroyAllWindows()

print(f"Processed image dimensions: {resizedimage.shape}")
