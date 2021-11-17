from math import sqrt

a, b, c = float(input()), float(input()), float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print(3)
        else:
            print(0)
    else:
        print(1, -c/b)
else:
    d = b**2 - 4*a*c
    if d == 0:
        print(1, -b/2/a)
    elif d > 0:
        x1, x2 = (-b-sqrt(d))/2/a, (-b+sqrt(d))/2/a
        if x1 > x2:
            x1, x2 = x2, x1
        print(2, x1, x2)
    else:
        print(0)
