from PIL import Image
from watchmatch.images import load_info_image

def test_info_image(tmp_path):
    # Kreire Testdaten
    image_path = tmp_path / "test.png"
    Image.new("RGB", (150, 70)).save(image_path)

    result = load_info_image(image_path)

    assert result["width"] == 150
    assert result["height"] == 70
    assert result["color_mode"] == "RGB"
    assert result["image_format"] == "PNG"
