from math import trunc

p, x, y = float(input()), int(input()), int(input())
s = trunc((x * 100 + y) * (100 + p) / 100)
print(s // 100, s % 100)
