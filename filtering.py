import cv2
import numpy as np
import matplotlib.pylab as plt

def displayimage(title, image):
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='grey')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()


def iterativeimagedetected(imagepath):
    image = cv2.imread(imagepath)
    if image is None:
        print("Erorr: Image not found")
        return
    
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    displayimage("Original gray scale image ", grayimage)
    
    print("Select one operation")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice 1 - 6")
        if choice == "1":
            sobelx = cv2.Sobel(grayimage, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(grayimage, cv2.CV_64F, 0, 1, ksize=3)
            combinedsobel = cv2.bitwise_or(sobelx.astype(np.uint81), sobely.astype(np.uint8))
            displayimage("Sobel Image detection", combinedsobel)

        elif choice == "2":
            print("Adjusting thresholds for canny (default: 100 and 200)")
            lowerthresh = int(input("Enter lower threshold"))
            upperthresh = int(input("Enter upper threshold"))
            edges = cv2.Canny(grayimage, lowerthresh, upperthresh)
            displayimage("Canny Image Detection", edges)

        elif choice == "3":
            laplacian = cv2.Laplacian(grayimage, cv2.CV_64F)
            displayimage("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))

        elif choice == "4":
            print("Adjust kernel size for Gaussian blur")
            kernelsize = int(input("Enter kernel size (odd number, eg: 5)"))
            blurred = cv2.GaussianBlur(image, (kernelsize, kernelsize), 0)
            displayimage("Gaussian Smoothed Image", blurred)

        elif choice == "5":
            print("Adjust kernel size for Median filtering (must be odd - default: 5)")
            kernelsize = int(input("Enter kernel size (odd number)"))
            medianfiltered = cv2.medianBlur(image, kernelsize)
            displayimage("Median Filtered Image", medianfiltered)

        elif choice == "6":
            print("Exiting ")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 6")
        
iterativeimagedetected('Footballphoto.png')