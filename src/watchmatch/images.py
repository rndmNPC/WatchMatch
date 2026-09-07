from PIL import Image
import os


def load_info_image(path):

    if not os.path.exists(path):
        print("No Existing File to read")
    else: 
        with Image.open(path) as img:
            return {
                "width": img.width,
                "height": img.height,
                "color_mode": img.mode,
                "image_format": img.format,
            }
        
    raise FileNotFoundError(f"No file found: {path}")
