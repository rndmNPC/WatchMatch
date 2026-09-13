import csv
from pathlib import Path
from PIL import Image
from watchmatch.embeddings import embed_image, load_embedding_model


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

if __name__ == "__main__":
    model, preprocess = load_embedding_model()
    res = build_catalog(Path("data/metadata.csv"),Path("data/raw"), model, preprocess)
    print(len(res))
    print(res[0]["filename"])
    print(res[0]["embedding"].shape)