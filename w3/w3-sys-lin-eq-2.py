# ax + by = e
# cx + dy = f

# y = e/b - x*a/b
# y = f/d - x*c/d

a, b = float(input()), float(input())
c, d = float(input()), float(input())
e, f = float(input()), float(input())

d0 = a * d - c * b
dx = e * d - f * b
dy = a * f - c * e

eps = 1e-9

if d0 == 0:
    if dx != 0 or dy != 0:
        # не имеет решения
        print(0)
    elif a == b == 0 and e != 0:
        # не имеет решения
        print(0)
    elif c == d == 0 and f != 0:
        # не имеет решения
        print(0)
    else:
        # множество решений
        if a != 0 and b != 0:
            # y = -a/b x + e/b
            p, q = -a / b, e / b
            print(1, p, q)
        elif c != 0 and d != 0:
            # y = -c/d x + f/d
            p, q = -c / d, f / d
            print(1, p, q)
        elif a == b == c == d == 0:
            # любые x y
            print(5)
        elif b == d == 0:
            if a != 0:
                x = e / a
                print(3, x)
            else:
                x = f / c
                print(3, x)
        else:
            if b != 0:
                y = e / b
                print(4, y)
            else:
                y = f / d
                print(4, y)
else:
    # единственное решение
    x, y = dx / d0, dy / d0
    print(2, x, y)
