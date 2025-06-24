from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

def generateimagecaption(imagepath):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    try:
        rawimage = Image.open(imagepath).convert("RGB")
    except FileNotFoundError:
        print("Error: Image file not found")
    except Exception as e:
        return f"Error opening image: {e}"
    
    inputs = processor(rawimage, return_tensors="pt")

    out = model.generate(**inputs)

    caption = processor.decode(out[0], skip_special_tokens=True)

    return caption

if __name__ == "__main__":
    imagefile = "FootballPhoto.png"
    caption = generateimagecaption(imagefile)
    print(f"Generated caption to the image: {caption}")
