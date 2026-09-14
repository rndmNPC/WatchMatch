# WatchMatch

Visual similarity search for watches, built as a computer-vision learning and portfolio project.

## Current implementation

WatchMatch provides a working visual-retrieval pipeline:

- load a local watch catalog from CSV,
- create 2048-dimensional visual embeddings with pretrained ResNet-50,
- compare them with cosine similarity, and
- print the five nearest catalog images for a query image.

### Run it locally

The catalog images stay local so that datasets can be selected and licensed independently. Place your images in `data/raw/` and create `data/metadata.csv`; the required CSV shape is documented in [data/README.md](data/README.md).

```bash
uv sync --group dev
PYTHONPATH=src uv run python -m watchmatch.demo data/raw/query.jpg
uv run pytest
```

The first demo run downloads torchvision's pretrained ResNet-50 weights. Use `--limit 5` to change the number of displayed matches.

```text
query image + catalog images
          │
          ▼
pretrained ResNet-50 feature extractor
          │
          ▼
2048-dimensional image embeddings → cosine similarity → top-k matches
```

## Product idea

A user uploads a watch photo. WatchMatch returns visually similar watches from a small catalog and explains the strongest visual similarities, such as case shape, dial color, strap material and overall style.

The first technical question is deliberately measurable:

> How well do pretrained ResNet50 embeddings retrieve visually similar watches, and does CLIP improve the ranking?

## Why this project exists

- Learn Python, image processing, PyTorch and model evaluation through a real product.
- Build a complete visual-search product from dataset design to user feedback.
- Demonstrate a complete path from dataset and baseline to API, user interface, deployment and user feedback.
- Produce measurable portfolio evidence alongside the implementation.

## Product roadmap

The next product version will add:

1. persisted embeddings and metadata,
2. evaluation on a labeled test set,
3. a FastAPI inference service,
4. a browser interface for image upload and results,
5. a CLIP comparison model, and
6. deployment and user feedback loops.

CLIP is a comparison model, not the starting point. Explanations, user accounts, recommendations and commercial catalog integrations are outside the first MVP.

## Planned stack

- Python 3.12
- Pillow and NumPy for image fundamentals
- PyTorch and torchvision for ResNet50
- scikit-learn or a small NumPy implementation for initial similarity search
- FastAPI for the inference API
- React and TypeScript for the interface
- pytest for tests
- Docker and GitHub Actions for reproducibility

## Repository structure

```text
WatchMatch/
├── data/
│   ├── raw/              # local source images, not committed by default
│   └── processed/        # generated metadata and embeddings
├── docs/
│   ├── DECISIONS.md      # technical and product decisions
│   └── ROADMAP.md        # milestones and acceptance criteria
├── src/
│   └── watchmatch/       # application code written by Trung Hieu
├── tests/                # independently designed tests
└── README.md
```

## Intended portfolio result

After completion, a truthful CV bullet could follow this pattern:

> Built and deployed a visual watch-search product comparing ResNet50 and CLIP embeddings across **N** labeled images; achieved **X Recall@5** and reduced median query latency to **Y ms** using Python, PyTorch, FastAPI and React.

All placeholders remain empty until evaluation has been completed.

## License

Released under the [MIT License](LICENSE).
