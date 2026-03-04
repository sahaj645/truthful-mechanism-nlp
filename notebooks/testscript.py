from src.data_loader import load_reviews
from src.embedding import get_embeddings

df = load_reviews("data/reviews.csv", 1000)
emb = get_embeddings(df['review_text'].tolist())

print("Embeddings shape:", emb.shape)