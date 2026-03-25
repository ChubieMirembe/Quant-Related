import random 

freq = {i: 0 for i in range(2, 13)}
ev = 0;
for i in range(100000):
    roll = random.randint(1, 6) + random.randint(1, 6)
    freq[roll] += 1

for total in sorted(freq):
    prob = freq[total] / 100000
    ev += total * prob

print("Expected value of the sum of two dice rolls:", ev)