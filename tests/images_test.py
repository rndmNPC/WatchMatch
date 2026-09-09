from PIL import Image
from watchmatch.images import load_info_image, prepare_image
import pytest

def test_info_image(tmp_path):
    # Kreire Testdaten
    image_path = tmp_path / "test.png"
    Image.new("RGB", (150, 70)).save(image_path)

    result = load_info_image(image_path)

    assert result["width"] == 150
    assert result["height"] == 70
    assert result["color_mode"] == "RGB"
    assert result["image_format"] == "PNG"


def test_load_info_image_raises_for_missing_file(tmp_path):
    missing_path = tmp_path / "missing.png"

    with pytest.raises(FileNotFoundError):
        load_info_image(missing_path)


def test_transform_image_scaling(tmp_path): 
    image_path = tmp_path / "test.png"
    Image.new("RGB", (100,50)).save(image_path)

    with Image.open(image_path) as img:
        result = prepare_image(img, (224,224))

    assert result.size == (224,224)
    assert result.mode == "RGB"

def test_transform_image_background(tmp_path):
    image_path = tmp_path / "test.png"
    Image.new("RGB", (100, 50), "red").save(image_path)

    with Image.open(image_path) as img:
        result = prepare_image(img, (224,224))

    assert result.getpixel((0, 0)) == (255, 255, 255)
    assert result.getpixel((112, 112)) == (255, 0, 0)

def test_transform_image_RGBA(tmp_path):
    image_path = tmp_path / "test.png"
    Image.new("RGBA", (100,50), (0,0,0,0)).save(image_path)

    with Image.open(image_path) as img:
        result = prepare_image(img,(224,224))

    assert result.getpixel((112,112)) == (255, 255, 255) 