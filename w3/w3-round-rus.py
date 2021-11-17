from math import trunc, ceil

x = float(input())
if x - trunc(x) == .5:
    print(ceil(x))
else:
    print(round(x))
