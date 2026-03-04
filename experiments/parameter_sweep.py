import numpy as np
import matplotlib.pyplot as plt
from src.simulation import simulate

alphas = [0.4, 0.5, 0.6, 0.7]
results_honest = []
results_manip = []

for a in alphas:

    honest_rewards = []
    manip_rewards = []

    for _ in range(20):

        honest, manip = simulate(
            n_rounds=500
        )

        honest_rewards.append(honest.cumulative_reward)
        manip_rewards.append(manip.cumulative_reward)

    results_honest.append(np.mean(honest_rewards))
    results_manip.append(np.mean(manip_rewards))


plt.plot(alphas, results_honest, label="Honest")
plt.plot(alphas, results_manip, label="Manipulator")

plt.xlabel("Alpha (Truth Weight)")
plt.ylabel("Average Reward")
plt.title("Parameter Sensitivity Analysis")
plt.legend()
plt.show()