import random

trials = 100_000
total_profit = 0
avg_profit = 0

for i in range(trials):
    roll = random.randint(1, 6) + random.randint(1, 6)
    if roll >= 9:
        total_profit += 1
    else:
        total_profit -= 1

avg_profit = total_profit / trials

print("Profit: ", total_profit)
print("Average profit per trial: ", avg_profit)