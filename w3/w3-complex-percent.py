from math import trunc

p, x, y, k = float(input()), int(input()), int(input()), int(input())
s = x * 100 + y
while k > 0:
    k -= 1
    s = trunc(s * (100 + p) / 100)
print(s // 100, s % 100)
