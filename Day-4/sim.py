import random

runs = 1000000
total_returns = 0

for _ in range(runs):
    if random.random() < 0.6:

        ret = random.normalvariate(1, 1)
    else:
        ret = random.normalvariate(-2, 1)

    total_returns += ret
print("Returns: $", total_returns/runs)