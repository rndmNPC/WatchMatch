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