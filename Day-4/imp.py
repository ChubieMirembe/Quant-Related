import random

trials = 10000

success = 0
for _ in range(trials):
    val = random.random()
    
    if val <= 0.7:
        if random.random() < 0.3:
            success += 1
    else:
        if random.random() < 0.8:
            success += 1

print("Probability: ", (success/trials))