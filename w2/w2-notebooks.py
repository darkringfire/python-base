x1, y1, z1 = int(input()), int(input()), int(input())
x2, y2, z2 = int(input()), int(input()), int(input())

n = 0
# x2, y2, z2
n1 = x1 // x2 * y1 // y2 * z1 // z2
if n1 > n:
    n = n1
# y2, x2, z2
n1 = x1 // y2 * y1 // x2 * z1 // z2
if n1 > n:
    n = n1

# x2, z2, y2
n1 = x1 // x2 * y1 // z2 * z1 // y2
if n1 > n:
    n = n1
# z2, x2, y2
n1 = x1 // z2 * y1 // x2 * z1 // y2
if n1 > n:
    n = n1

# y2, z2, x2
n1 = x1 // y2 * y1 // z2 * z1 // x2
if n1 > n:
    n = n1
# z2, y2, x2
n1 = x1 // z2 * y1 // y2 * z1 // x2
if n1 > n:
    n = n1

print(n)
