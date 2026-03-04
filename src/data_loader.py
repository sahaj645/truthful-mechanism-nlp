import pandas as pd

def load_reviews(path, sample_size=50000):
    df = pd.read_csv(path)
    df = df[['review_text', 'rating']]
    df = df.dropna()
    df = df.sample(min(sample_size, len(df)), random_state=42)
    df.reset_index(drop=True, inplace=True)
    return df