from watchmatch.embeddings import cosine_similarity

def rank_catalog(
    query_embedding,
    catalog,
    limit = 5,
):
    results = []

    # Compare the query embedding with every precomputed catalog embedding.
    for item in catalog:
        score = cosine_similarity(
            query_embedding,
            item["embedding"],
        )
        results.append(
            {
                "filename": item["filename"],
                "style_group": item["style_group"],
                "score": score,
            }
        )

    # Higher cosine scores mean greater visual similarity.
    sorted_results = sorted(
        results,
        key=lambda result: result["score"],
        reverse=True,
    )

    # Return only the requested number of best matches.
    return sorted_results[:limit]
