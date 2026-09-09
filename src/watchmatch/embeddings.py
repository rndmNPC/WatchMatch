import torch
from torch import nn
from math import sqrt
from torchvision.models import ResNet50_Weights, resnet50
from PIL import Image

def load_embedding_model():
    weights = ResNet50_Weights.DEFAULT
    preprocess = weights.transforms()

    model = resnet50(weights=weights)
    model.fc = nn.Identity()
    model.eval()

    return model, preprocess

def embed_image(
    image: Image.Image,
    model,
    preprocess
) -> torch.Tensor:
    
    image_tensor = preprocess(image)
    batch = image_tensor.unsqueeze(0)

    with torch.inference_mode():
        batch_embeddings = model(batch)

    return batch_embeddings.squeeze(0)

def cosine_similarity(    
    vector_a: torch.Tensor,
    vector_b: torch.Tensor,
    )-> float:

    zahler = 0
    maga = 0
    magb = 0
    if len(vector_b) != len(vector_a):
        raise ValueError("Vectors do not have the same length!")
    
    for i in range(len(vector_a)):
        zahler = zahler + vector_a[i]*vector_b[i]
        maga = maga + vector_a[i]**2
        magb = magb + vector_b[i]**2
    maga = sqrt(maga)
    magb = sqrt(magb)

    return (zahler / (maga * magb)).item()



if __name__ == "__main__":
    model, preprocess = load_embedding_model()
    print(model.fc)
    test = Image.new("RGB", (1000,700), "black")
    res = embed_image(test, model, preprocess)
    print(res.shape)
    print(res[:5])
