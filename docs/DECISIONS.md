# Decisions

Record decisions in the following format.

## YYYY-MM-DD - Decision title

**Context:** What problem or choice appeared?

**Options:** Which realistic alternatives were considered?

**Decision:** What was selected?

**Reason:** Why was this option appropriate now?

**Consequence:** What becomes easier, harder or intentionally postponed?

## 2026-09-05 - Start with ResNet50 before CLIP

**Context:** The final project should compare convolutional and vision-language representations.

**Options:** Start with CLIP, start with ResNet50, or implement both immediately.

**Decision:** Build a ResNet50 retrieval baseline first and add CLIP only after it works and is evaluated.

**Reason:** ResNet makes the image tensor, preprocessing, feature extraction and baseline comparison easier to understand. Starting both models would hide gaps behind additional complexity.

**Consequence:** The first visible result is simpler, but the later CLIP comparison becomes meaningful and measurable.

## 2026-09-07 - Function prepare image

**context** : we need to decide what format the resnet 50 need s as input and to trasnformthem accordingly

Input: path to a image 
Output: Pillow bild in right dimensions and transformation (maybe already numpy array)
Target size: 224 x 224
Resize strategy: resize and cut
Handling of L/RGBA images:

> Superseded by the decision from 2026-09-09.

## 2026-09-09 - Image preparation and ResNet preprocessing

**Context:** Raw catalog images can have different sizes, aspect ratios and color modes. ResNet50 expects a specific RGB tensor format.

**Options:** Stretch images, center-crop images, preserve the aspect ratio with white padding, or let Torchvision handle the model preprocessing.

**Decision:** `prepare_image` keeps the aspect ratio, centers the image on a white background and converts RGBA images to RGB. The actual ResNet preprocessing is done with `weights.transforms()`.

**Reason:** White padding avoids distortion and keeps the complete watch visible. `weights.transforms()` matches the pretrained ResNet50 weights.

**Consequence:** `prepare_image` handles raw input safely, while Torchvision handles the model-specific resize, crop and normalization.
