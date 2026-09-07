# WatchMatch

Visual similarity search for watches, built as an end-to-end computer-vision learning and portfolio project.

## Product idea

A user uploads a watch photo. WatchMatch returns visually similar watches from a small catalog and explains the strongest visual similarities, such as case shape, dial color, strap material and overall style.

The first technical question is deliberately measurable:

> How well do pretrained ResNet50 embeddings retrieve visually similar watches, and does CLIP improve the ranking?

## Why this project exists

- Learn Python, image processing, PyTorch and model evaluation through a real product.
- Build the core implementation independently instead of presenting AI-generated code as personal implementation.
- Demonstrate a complete path from dataset and baseline to API, user interface, deployment and user feedback.
- Produce honest CV metrics instead of merely listing technologies.

## MVP definition

Version 1 is complete when it can:

1. load and validate catalog images,
2. create embeddings using a pretrained ResNet50,
3. store embeddings and metadata locally,
4. accept a query image,
5. rank catalog images using cosine similarity,
6. show the five closest results,
7. evaluate retrieval quality on a labeled test set,
8. run through a simple browser interface.

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
├── LEARNING_LOG.md       # daily understanding and debugging notes
└── README.md
```

## Learning agreement

1. Trung Hieu writes every core function first.
2. Before requesting code, document an own attempt or a precise blocker.
3. AI assistance starts with explanations, questions, hints or review.
4. Every feature includes at least one independently designed test.
5. Every commit must be explainable without opening an AI conversation.
6. Numbers enter the CV only after they have actually been measured.

## Day 1 - first 60 minutes

### Goal

Write and test the first small image-loading function. No neural network yet.

### Tasks

1. Create and activate a Python 3.12 virtual environment.
2. Install only `pillow` and `pytest`.
3. Create `src/watchmatch/images.py` yourself.
4. Define what `load_image_info(path)` should return: width, height, color mode and image format.
5. Before implementing it, write two test cases:
   - a valid temporary RGB image returns the expected information;
   - a missing file raises a clear error.
6. Implement the smallest code that makes the tests pass.
7. Explain why width and height can be confused between Pillow, NumPy and PyTorch.
8. Commit the result with a specific message.

### Definition of done

- `pytest` passes.
- The function contains no copied unexplained code.
- The implementation and both tests can be explained line by line.
- A Git commit exists.

## Next learning sessions

The guided exercises for the next four sessions are in [`docs/LESSONS.md`](docs/LESSONS.md). They cover testing and error handling, image normalization, NumPy fundamentals and a small command-line tool without giving away the implementations.

## Intended portfolio result

After completion, a truthful CV bullet could follow this pattern:

> Built and deployed a visual watch-search product comparing ResNet50 and CLIP embeddings across **N** labeled images; achieved **X Recall@5** and reduced median query latency to **Y ms** using Python, PyTorch, FastAPI and React.

All placeholders remain empty until evaluation has been completed.
