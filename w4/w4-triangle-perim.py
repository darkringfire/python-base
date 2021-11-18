from math import sqrt


def length(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def t_perimeter(x1, y1, x2, y2, x3, y3):
    res = length(x1, y1, x2, y2)
    res += length(x1, y1, x3, y3)
    res += length(x2, y2, x3, y3)
    return res


p1x, p1y = int(input()), int(input())
p2x, p2y = int(input()), int(input())
p3x, p3y = int(input()), int(input())

print(t_perimeter(p1x, p1y, p2x, p2y, p3x, p3y))
