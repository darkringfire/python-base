from math import sqrt

x = int(input())
n = 0
sum_x2 = sum_x = 0
while x != 0:
    n += 1
    sum_x2 += x ** 2
    sum_x += x
    x = int(input())
sigma = sqrt((sum_x2 - sum_x**2/n)/(n-1))
print(sigma)
