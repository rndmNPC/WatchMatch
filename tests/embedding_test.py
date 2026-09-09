import pytest
import torch
from watchmatch.embeddings import cosine_similarity

def test_cosine_similarity():
    vector_1 = torch.tensor([1.0, 0.0])
    vector_2 = torch.tensor([0.0, 1.0])
    vector_3 = torch.tensor([-1.0, 0.0])
    vector_4 = torch.tensor([0.0, 0.0, 0.0])

    assert cosine_similarity(vector_1, vector_1) == pytest.approx(1.0)
    assert cosine_similarity(vector_1, vector_2) == pytest.approx(0.0)
    assert cosine_similarity(vector_1, vector_3) == pytest.approx(-1.0)

    with pytest.raises(ValueError):
        cosine_similarity(vector_1, vector_4)
