import cv2

import matplotlib.pyplot as plt # Correct import

# Load Image

image = cv2.imread('FootballPhoto.png')

# Check if the image is loaded properly

if image is None:

    print("Error: Image not found. Check the file path!")

else:

# Convert BGR to RGB and Display

    imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(imagergb)

    plt.title("RGB Image")

    plt.axis('off') # Hide axes

    plt.show() # Show the RGB image

# Convert BGR to Grayscale and Display

    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    plt.imshow(grayimage, cmap="gray") # Add cmap for grayscale display

    plt.title("Grayscale Image")

    plt.axis('off') # Hide axes

    plt.show() # Show the grayscale image