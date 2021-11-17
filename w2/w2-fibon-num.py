a = int(input())
f0, f1 = 0, 1
n = 0
while f0 < a:
    n += 1
    f0, f1 = f1, f0 + f1
if f0 == a:
    print(n)
else:
    print(-1)
