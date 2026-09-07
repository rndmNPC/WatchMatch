from PIL import Image
from watchmatch.images import load_info_image
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