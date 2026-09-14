import pytest
import torch

from watchmatch.search import rank_catalog


def test_rank_catalog_returns_best_matches_first():
    query_embedding = torch.tensor([1.0, 0.0])
    catalog = [
        {
            "filename": "far.jpg",
            "style_group": "test",
            "embedding": torch.tensor([-1.0, 0.0]),
        },
        {
            "filename": "middle.jpg",
            "style_group": "test",
            "embedding": torch.tensor([0.0, 1.0]),
        },
        {
            "filename": "near.jpg",
            "style_group": "test",
            "embedding": torch.tensor([1.0, 0.0]),
        },
    ]

    results = rank_catalog(query_embedding, catalog, limit=2)

    assert [result["filename"] for result in results] == ["near.jpg", "middle.jpg"]
    assert results[0]["score"] == pytest.approx(1.0)
    assert results[1]["score"] == pytest.approx(0.0)


def test_rank_catalog_rejects_a_non_positive_limit():
    with pytest.raises(ValueError, match="at least 1"):
        rank_catalog(torch.tensor([1.0]), [], limit=0)
