# Local catalog data

The repository intentionally does not include watch images. Add images that you are allowed to use to `data/raw/` and create `data/metadata.csv` with this shape:

```csv
filename,style_group
example_diver.jpg,diver
example_dress.jpg,dress
```

`filename` must exactly match a file in `data/raw/`. `style_group` is a manual label used only for inspecting retrieval quality; it is not supplied to the ResNet model.
