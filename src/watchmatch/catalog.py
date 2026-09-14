import csv
from pathlib import Path

from PIL import Image

from watchmatch.embeddings import embed_image


def build_catalog(
    metadata_path: Path,
    image_directory: Path,
    model,
    preprocess,
) -> list[dict]:
    catalog = []

    with metadata_path.open(newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            image_path = image_directory / row["filename"]

            with Image.open(image_path) as image:
                embedding = embed_image(
                    image.convert("RGB"),
                    model,
                    preprocess,
                )

            catalog.append(
                {
                    "filename": row["filename"],
                    "style_group": row["style_group"].strip(),
                    "embedding": embedding,
                }
            )

    return catalog
