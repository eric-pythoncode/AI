from PIL import ImageEnhance, ImageFilter, Image
import requests
from io import BytesIO

def generateimage():
    url = "https://cdn.pixabay.com/photo/2024/02/17/15/59/plum-blossoms-8579641_1280.jpg"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            return Image.open(BytesIO(response.content))
        except function as e:
            print(f"Failed to open image: {e}")
    
    else:
        print(f"Request failed with status code {response.status_code}")
    return None

def enhanceimage(img):
    brightness = ImageEnhance.Brightness(img)
    img = brightness.enhance(1.3)
    
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1.5)

    img = img.filter(ImageFilter.GaussianBlur(radius=2))

    return img

def main():
    originalimg = generateimage()
    if originalimg:
        enhancedimg = enhanceimage(originalimg)

        originalimg.show(title="Original Image")
        enhancedimg.show(title="Enhanced Image")
    else:
        print("Image generation failed. Please check the URL or file source.")

if __name__ == "__main__":
    main()