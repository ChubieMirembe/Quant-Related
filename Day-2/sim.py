import random

profit = 0
trials = 10000
count = 0
t = 0.8

for _ in range(trials):
    signal = random.random()
    if signal > t:
        count += 1
        sec_signal = random.random()
        if sec_signal < signal:
            profit += 1
        else: 
            profit -= 1
            
print(profit/count)
