belief = {
    "fair": 0.6,
    "biased" : 0.4
}

def likelihood(state, obs):
    if state == "fair":
        return 0.5 if obs == "head" else 0.5
    else:
        return 0.8 if obs == "head" else 0.2
    
tosses = ["head", "head", "tail", "head", "tail", "tail", "tail", "head", "head", "tail"]

for toss in tosses:
    update = {}

    for state in belief:
        update[state] = belief[state] * likelihood(state, toss)

    total = sum(update.values())
    for state in update:
        update[state] /= total

    belief = update
    print(toss, belief)