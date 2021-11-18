from math import sqrt


def print_yes_no(b):
    if b:
        print('YES')
    else:
        print('NO')


def length(p1x, p1y, p2x, p2y):
    return sqrt((p1x - p2x) ** 2 + (p1y - p2y) ** 2)


def IsPointInArea(x, y):
    return (y >= -x and y >= x*2+2 and length(x, y, -1, 1) <= 2) or \
           (y <= -x and y <= x*2+2 and length(x, y, -1, 1) >= 2)


def main():
    x, y = float(input()), float(input())
    print_yes_no(IsPointInArea(x, y))


main()
