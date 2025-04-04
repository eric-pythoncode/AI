import ComputerRGB

# Load the image
image = ComputerRGB.imread('FootballPhoto.png')

# Resize the window to a specific size without resizing the image
ComputerRGB.namedWindow('Loaded Image', ComputerRGB.WINDOW_NORMAL) # Create a resizable window
ComputerRGB.resizeWindow('Loaded Image', 800, 500) # Set the window size to 800x500 (width x height)

# Display the image in the resized window
ComputerRGB.imshow('Loaded Image', image)

ComputerRGB.waitKey(0) # Wait for a key press
ComputerRGB.destroyAllWindows() # Close the window

# Print image properties
print(f"Image Dimensions: {image.shape}") # Height, Width, Channels (in pixels)