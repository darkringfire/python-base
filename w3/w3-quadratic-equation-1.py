from math import sqrt

a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4*a*c
if d == 0:
    print(-b/2/a)
elif d > 0:
    x1, x2 = (-b-sqrt(d))/2/a, (-b+sqrt(d))/2/a
    if x1 > x2:
        x1, x2 = x2, x1
    print(x1, x2)
