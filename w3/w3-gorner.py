n, x = int(input()), float(input())
res = 0
while n >= 0:
    n -= 1
    a = float(input())
    res = res * x + a
print(res)
