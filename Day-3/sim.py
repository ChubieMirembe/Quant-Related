import random

trials = 10000
x_sum = 0
x2_sum = 0
y_sum = 0
y2_sum = 0
xy_sum = 0
cov = 0

for _ in range(trials):
    x = random.random()
    # y is a function of x plus some random noise
    # when noise in increase the correlation will decrease
    y = x + random.random() + random.random() + random.random() + random.random()
    xy_sum += x * y
    x_sum += x
    y_sum += y
    x2_sum += x ** 2
    y2_sum += y ** 2


x_sum /= trials
y_sum /= trials
xy_sum /= trials
x2_sum /= trials
y2_sum /= trials

print("X: ", x_sum) 
print("Y: ", y_sum) 
print("XY: ", xy_sum) 
cov = xy_sum - (x_sum * y_sum)
print("Cov: ", cov)    
VarX = x2_sum - (x_sum ** 2)
VarY = y2_sum - (y_sum ** 2)
print("Var(X): ", VarX)
print("Var(Y): ", VarY)

corr = cov / ((VarX * VarY) ** 0.5)
print("Corr: ", corr)

## When noise is increase the correlation will decrease
# covariance and correlation are used to detect signal in the presence of noise.
#  When noise is increase the correlation will decrease.
#  When noise is decrease the correlation will increase. When noise is zero the
#  correlation will be 1.0. When noise is infinite the correlation will be
#  0.0.