import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def sentiment_alignment(sentiment_pred, rating):
    # Normalize rating to [0,1]
    rating_norm = (rating - 1) / 4
    return 1 - abs(sentiment_pred - rating_norm)

def consensus_similarity(review_embedding, product_embedding):
    sim = cosine_similarity(
        review_embedding.reshape(1, -1),
        product_embedding.reshape(1, -1)
    )[0][0]
    return (sim + 1) / 2  # normalize to [0,1]

def compute_truth_score(sentiment_score, rating,
                        review_embedding, product_embedding):
    s_align = sentiment_alignment(sentiment_score, rating)
    s_cons = consensus_similarity(review_embedding, product_embedding)
    return 0.5 * s_align + 0.5 * s_cons