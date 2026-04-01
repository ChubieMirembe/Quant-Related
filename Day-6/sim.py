import random

trials = 100000
days = 100
p = 0.55
total_wins = 0

for _ in range(trials):
    winning_days = 0

    for _ in range(days):
        if random.random() < p:
            winning_days += 1
    
    if winning_days >= 60:
        total_wins += 1

print(total_wins / trials)
