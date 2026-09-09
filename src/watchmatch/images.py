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

#Das Bild wird skaliert und angepasst und erhält einen weißen Hintergrund
def prepare_image(
    image: Image.Image,
    target_size: tuple[int, int],
) -> Image.Image:

    if image.mode == "RGBA":
        image = alpha_to_color(image)
    #Berechnung von Skalierung um zu wissen wie das Bild angepasst werden muss um die höchste Qualität der längsten Seite beizubehalten
    target_width, target_height = target_size
    image_width, image_height = image.size

    scale = min(target_width / image_width,
                target_height / image_height)

    new_width  = round(image_width * scale)
    new_height = round(image_height * scale)

    resized_image = image.resize((new_width, new_height))
    background = Image.new("RGB", target_size, (255,255,255))

    x = (target_width - new_width) // 2
    y = (target_height - new_height) // 2
    background.paste(resized_image, (x,y))

    return background


def alpha_to_color(image, color=(255, 255, 255)):
    white_background = Image.new(
        "RGBA",
        image.size,
        (255, 255, 255, 255),
    )

    combined_image = Image.alpha_composite(
        white_background,
        image,
    )

    return combined_image.convert("RGB")
