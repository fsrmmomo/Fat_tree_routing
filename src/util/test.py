import math

n = 2000
k = 3
p = 0.01
m = - (k*n)/(math.log( (1-p**(1/k)) , math.e))

print(m)
print(m / 1024)