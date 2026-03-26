#Simulating P(both cards red | at least one card is red) using Python

import random

trials = 1000000
deck = ['R']*26 + ['B']*26
valid = 0
count = 0

for _ in range(trials):
    cards = random.sample(deck, 2)
    if 'R' in cards:
        count += 1
        if cards[0] == 'R' and cards[1] == 'R':
            valid += 1

probability = valid / count
print(f"P(both cards red | at least one card is red) = {probability:.4f}")


