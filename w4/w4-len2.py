from math import sqrt


def length(p1x, p1y, p2x, p2y):
    return sqrt((p1x - p2x) ** 2 + (p1y - p2y) ** 2)


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())

print(length(x1, y1, x2, y2))
