# n = int(input())
for n in range(3):
    print(n, end=' ')
    f = 0
    f0, f1 = 0, 1
    while n > 0:
        n -= 1
        f, f0, f1 = f0 + f1, f1, f0 + f1

    print(f)
