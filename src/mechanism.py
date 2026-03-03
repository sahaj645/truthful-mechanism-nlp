import numpy as np

class Reviewer:
    def __init__(self, reviewer_id, strategy="honest"):
        self.reviewer_id = reviewer_id
        self.strategy = strategy
        self.reputation = 0.0
        self.cumulative_reward = 0.0

    def update_reputation(self, reward):
        self.cumulative_reward += reward
        self.reputation += reward


def compute_reward(truth_score, agreement_score,
                   alpha=0.6, beta=0.3, gamma=0.1,
                   manipulation_intensity=0.0):

    reward = (
        alpha * truth_score +
        beta * agreement_score -
        gamma * manipulation_intensity
    )

    return reward