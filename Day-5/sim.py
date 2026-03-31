import random
import math

regime = {
    "bull" : 0.5,
    "bear": 0.5
}

def likelihood(state, obs):
    if state == "bull":
        return 0.65 if obs == "up" else 0.35
    else:
        return 0.35 if obs == "up" else 0.65

daily = ["up", "down"]

for _ in range(30):
    move = random.choice(daily)
    posterior = {}

    # Update the belief about the likelihood of each
    for reg in regime:
        posterior[reg] = regime[reg] * likelihood(reg, move)
    
    total_sum = sum(posterior.values())

    for post in posterior:
        posterior[post] /= total_sum
    
    regime = posterior
    log_odds = math.log(regime["bull"] / regime["bear"])
    print(move, regime, log_odds)
