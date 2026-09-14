"""Command-line demo for retrieving visually similar catalog watches."""

import argparse
from pathlib import Path

from PIL import Image

from watchmatch.catalog import build_catalog
from watchmatch.embeddings import embed_image, load_embedding_model
from watchmatch.search import rank_catalog


def format_results(results: list[dict]) -> str:
    """Format ranked matches as a compact terminal table."""
    header = f"{'Rank':<6}{'Score':<9}{'Style':<15}File"
    rows = [header, "-" * len(header)]

    for rank, result in enumerate(results, start=1):
        rows.append(
            f"{rank:<6}{result['score']:<9.3f}{result['style_group']:<15}"
            f"{result['filename']}"
        )

    return "\n".join(rows)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find visually similar watches in a local catalog."
    )
    parser.add_argument("query", type=Path, help="Image to search for")
    parser.add_argument(
        "--metadata",
        type=Path,
        default=Path("data/metadata.csv"),
        help="CSV file with filename and style_group columns",
    )
    parser.add_argument(
        "--images",
        type=Path,
        default=Path("data/raw"),
        help="Directory containing the catalog images",
    )
    parser.add_argument("--limit", type=int, default=5, help="Number of matches")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    if not args.query.is_file():
        raise FileNotFoundError(f"Query image not found: {args.query}")

    model, preprocess = load_embedding_model()
    catalog = build_catalog(args.metadata, args.images, model, preprocess)

    with Image.open(args.query) as query_image:
        query_embedding = embed_image(query_image.convert("RGB"), model, preprocess)

    results = rank_catalog(query_embedding, catalog, limit=args.limit + 1)
    results = [result for result in results if result["filename"] != args.query.name]

    print(format_results(results[: args.limit]))


if __name__ == "__main__":
    main()
