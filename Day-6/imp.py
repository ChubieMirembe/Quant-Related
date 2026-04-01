import random

trials = 100000
n = 10
p = 0.4
# This will store how often each outcome occurs
dist = {i: 0 for i in range(n+1)}

for _ in range(trials):
    success = 0

    for _ in range(n):
        if random.random() < p:
            success += 1
    dist[success] += 1

for k in dist:
    print(k, dist[k] / trials)
