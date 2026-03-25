import random 

freq = {i: 0 for i in range(2, 13)}
trials = 10000000
ev = 0
variance = 0

for i in range(trials):
    roll = random.randint(1, 6) + random.randint(1, 6)
    freq[roll] += 1

for total in sorted(freq):
    prob = freq[total] / trials
    # For each possible total, we calculate the ev contribution
    # by multiplying its occrence by the probability of that total occurring
    ev += total * prob

    # For each possible total, we calculate the variance contribution
    # by multiplying the squared difference from the expected value by 
    # the probability of that total occurring

    variance += (total - ev) ** 2 * prob
print("Expected value of the sum of two dice rolls:", ev)
print("Variance of the sum of two dice rolls:", variance)