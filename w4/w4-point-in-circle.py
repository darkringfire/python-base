from math import sqrt


def print_yes_no(b):
    if b:
        print('YES')
    else:
        print('NO')


def length(p1x, p1y, p2x, p2y):
    return sqrt((p1x - p2x) ** 2 + (p1y - p2y) ** 2)


def is_in_circ(px, py, cx, cy, cr):
    return length(px, py, cx, cy) <= cr


x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())

print_yes_no(is_in_circ(x, y, xc, yc, r))
