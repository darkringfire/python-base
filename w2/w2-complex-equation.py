a, b, c, d = int(input()), int(input()), int(input()), int(input())


if a == b == 0:
    print('INF')
elif a == 0:
    print('NO')
else:
    x1 = -b // a
    m1 = -b % a
    if m1 == 0:
        if c * x1 + d != 0:
            print(x1)
        else:
            print('NO')
    else:
        print('NO')
