# WatchMatch learning plan

This plan continues after the first version of `load_image_info`. Each session is designed for roughly 60 minutes. Write the implementation yourself; use AI first for explanations, hints and review.

## Session 1 - Make the image loader reliable

### Learning goal

Understand how to specify behavior with tests and how Python communicates errors.

### Before coding

Answer briefly in `LEARNING_LOG.md`:

1. What should `load_image_info` return for a valid image?
2. What should happen for a missing path?
3. Why should a reusable function normally not print its result?

### Tasks

- Rename the function to `load_image_info` so its name matches the documented interface.
- Remove the manual image call from module scope, or protect it with `if __name__ == "__main__":`.
- Create `tests/test_images.py`.
- Write a test that creates a temporary RGB PNG with known dimensions.
- Assert the complete returned dictionary, not just one field.
- Write a second test describing the intended missing-file behavior.
- Only then adjust the implementation until both tests pass.

### Useful concepts to look up

- pytest's `tmp_path` fixture
- `Image.new(...)` and `Image.save(...)`
- `assert`
- `pytest.raises(...)`

### Self-check

- Can I explain why the test image should be created inside the temporary directory?
- Can I explain the difference between returning `None` and raising an exception?
- Does importing `watchmatch.images` avoid opening my wallpaper or printing anything?

### Definition of done

- Two tests pass.
- The production function contains no `print` statement.
- The function and tests can be explained line by line.
- The result is committed to Git.

## Session 2 - Normalize images for a model

### Learning goal

Understand why machine-learning models require consistent image size and color channels.

### Design exercise

Before writing code, decide the contract for a new function named `prepare_image`:

- What inputs should it accept?
- Should it modify the source file?
- What type should it return?
- What should its target size be?
- What should happen to grayscale and RGBA images?

Record the decisions in `docs/DECISIONS.md`.

### Tasks

- Write one test using an RGB image whose dimensions do not match the target size.
- Write one test using either a grayscale (`L`) or transparent (`RGBA`) image.
- Implement resizing and conversion to RGB with Pillow.
- Confirm that the source image on disk remains unchanged.

### Questions to investigate

- What information can be lost when converting RGBA to RGB?
- What distortion occurs when width and height are resized independently?
- What alternatives preserve aspect ratio?

### Definition of done

- The output has the chosen dimensions and mode `RGB`.
- At least two tests pass.
- The resize strategy and its limitation are documented.

## Session 3 - From Pillow to NumPy

### Learning goal

Understand the representation of an image as numbers before introducing PyTorch.

### Tasks

- Add NumPy as a project dependency.
- Convert a prepared Pillow image into a NumPy array.
- Inspect and record its `shape`, `dtype`, minimum and maximum.
- Write a small function that converts pixel values from `0..255` to `0..1`.
- Write tests for the output shape, data type and value range.
- Repeat the inspection with a known 2-by-3 RGB image that you construct yourself.

### Questions to answer in the learning log

1. Why is a Pillow RGB image commonly shaped `(height, width, channels)` in NumPy?
2. Why can width and height appear reversed compared with `image.size`?
3. Why should normalization produce a floating-point array?
4. What could go wrong with integer division or an unexpected grayscale image?

### Definition of done

- Array shape and value range are tested.
- You can identify the height, width and color-channel axes without guessing.
- No neural-network library has been added yet.

## Session 4 - Consolidation and a tiny command-line inspection tool

### Learning goal

Combine small functions without mixing data processing and presentation.

### Tasks

- Create a small command-line entry point that accepts an image path.
- Reuse `load_image_info` instead of duplicating its logic.
- Print the metadata as formatted JSON.
- Return a non-zero exit status for invalid input.
- Add one test for the successful command and one for invalid input.
- Review naming, type hints and docstrings only after the behavior works.

### Self-review

- Which code is reusable application logic, and which code is only user interface?
- Where does conversion to JSON belong?
- Can another Python function still consume the metadata dictionary directly?

### Definition of done

- The command works with an arbitrary local image path.
- Core functions return Python values and do not print.
- Tests pass and the README contains one example command.

## Working rhythm for every session

1. Spend 5 minutes writing the expected behavior in your own words.
2. Spend 10 minutes writing or updating tests.
3. Spend 30 minutes implementing and debugging.
4. Spend 10 minutes explaining the result without assistance.
5. Spend 5 minutes updating `LEARNING_LOG.md` and committing the work.

If blocked for more than 15 minutes, record the exact error, what you expected and what you already tried before asking for a hint.
