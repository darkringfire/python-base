def min4(x1, x2, x3, x4):
    return min(min(x1, x2), min(x3, x4))


a, b, c, d = int(input()), int(input()), int(input()), int(input())

print(min4(a, b, c, d))
