n = int(input())
f0, f1 = 0, 1
while n > 0:
    n -= 1
    f0, f1 = f1, f0 + f1

print(f0)
