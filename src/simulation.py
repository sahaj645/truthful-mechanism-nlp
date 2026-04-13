import pandas as pd
import numpy as np

from src.embedding import get_embeddings
from src.truth_score import consensus_similarity
from src.mechanism import Reviewer, compute_reward


def load_fact_base(path: str = "data/fact_base.txt"):
    with open(path, "r", encoding="utf-8") as f:
        facts = [line.strip() for line in f if line.strip()]
    return facts


class PoliticalDiscourseSimulation:
    def __init__(self, n_users: int = 8, n_rounds: int = 15, seed: int = 42):
        self.n_users = n_users
        self.n_rounds = n_rounds
        self.rng = np.random.default_rng(seed)
        self.users = [Reviewer(reviewer_id=f"user_{i+1}") for i in range(n_users)]
        self.results = []

    def _agreement_score(self):
        score = self.rng.normal(0.65, 0.15)
        return float(np.clip(score, 0.0, 1.0))

    def run(
        self,
        claims_path: str = "data/political_claims.csv",
        fact_path: str = "data/fact_base.txt",
    ) -> pd.DataFrame:
        claims_df = pd.read_csv(claims_path)
        facts = load_fact_base(fact_path)

        fact_embeddings = get_embeddings(facts)
        fact_centroid = fact_embeddings.mean(axis=0)

        for round_id in range(1, self.n_rounds + 1):
            sampled_claims = claims_df.sample(
                n=min(self.n_users, len(claims_df)),
                replace=len(claims_df) < self.n_users,
                random_state=round_id,
            ).reset_index(drop=True)

            for idx, user in enumerate(self.users):
                claim_row = sampled_claims.iloc[idx % len(sampled_claims)]
                claim_text = claim_row["claim_text"]
                claim_embedding = get_embeddings([claim_text])[0]

                truth_score = float(
                    consensus_similarity(claim_embedding, fact_centroid)
                )
                agreement = self._agreement_score()

                manipulation = float(max(0.0, 1.0 - claim_row.get("ground_truth", 0.5)))
                reward = float(
                    compute_reward(
                        truth_score=truth_score,
                        agreement_score=agreement,
                        manipulation_intensity=manipulation,
                    )
                )

                user.update_reputation(reward)

                self.results.append(
                    {
                        "round": round_id,
                        "user_id": user.reviewer_id,
                        "claim_text": claim_text,
                        "ground_truth": float(claim_row.get("ground_truth", 0.5)),
                        "truth_score": truth_score,
                        "agreement_score": agreement,
                        "manipulation_intensity": manipulation,
                        "reward": reward,
                        "reputation": float(user.reputation),
                    }
                )

        return pd.DataFrame(self.results)


if __name__ == "__main__":
    sim = PoliticalDiscourseSimulation(n_users=6, n_rounds=10)
    df = sim.run()
    df.to_csv("simulation_results.csv", index=False)
    print(df.head())
