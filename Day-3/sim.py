import random

trials = 10000
x_sum = 0
x2_sum = 0
y_sum = 0
y2_sum = 0
xy_sum = 0
cov = 0

bins = {0.2: 0, 0.4: 0, 0.6: 0, 0.8: 0, 1.0: 0}
bins_count = {0.2: 0, 0.4: 0, 0.6: 0, 0.8: 0, 1.0: 0}

for _ in range(trials):
    x = random.random()
    # y is a function of x plus some random noise
    # when noise in increase the correlation will decrease
    y = x + random.random() + random.random() + random.random()
    xy_sum += x * y
    x_sum += x
    y_sum += y
    x2_sum += x ** 2
    y2_sum += y ** 2
    
    if(x <= 0.2):
        bins[0.2] += y
        bins_count[0.2] += 1
    elif(x <= 0.4):
        bins[0.4] += y
        bins_count[0.4] += 1
    elif(x <= 0.6):
        bins[0.6] += y
        bins_count[0.6] += 1
    elif(x <= 0.8):
        bins[0.8] += y
        bins_count[0.8] += 1
    elif(x <= 1.0):
        bins[1.0] += y
        bins_count[1.0] += 1


x_sum /= trials
y_sum /= trials
xy_sum /= trials
x2_sum /= trials
y2_sum /= trials
VarX = x2_sum - (x_sum ** 2)
VarY = y2_sum - (y_sum ** 2)
cov = xy_sum - (x_sum * y_sum)
corr = cov / ((VarX * VarY) ** 0.5)

for _ in bins:
    bins[_] = bins[_] / bins_count[_]
    print(_, " ", bins[_])
## When noise is increase the correlation will decrease
# covariance and correlation are used to detect signal in the presence of noise.
#  When noise is increase the correlation will decrease.
#  When noise is decrease the correlation will increase. When noise is zero the
#  correlation will be 1.0. When noise is infinite the correlation will be
#  0.0.
