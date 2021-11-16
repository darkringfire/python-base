x1, y1, z1 = int(input()), int(input()), int(input())
x2, y2, z2 = int(input()), int(input()), int(input())

n1 = (x1 // x2) * (y1 // y2) * (z1 // z2)
n2 = (x1 // x2) * (y1 // z2) * (z1 // y2)
n3 = (x1 // y2) * (y1 // x2) * (z1 // z2)
n4 = (x1 // y2) * (y1 // z2) * (z1 // x2)
n5 = (x1 // z2) * (y1 // x2) * (z1 // y2)
n6 = (x1 // z2) * (y1 // y2) * (z1 // x2)

if n1 < n2:
    n1, n2 = n2, n1
if n1 < n3:
    n1, n3 = n3, n1
if n1 < n4:
    n1, n4 = n4, n1
if n1 < n5:
    n1, n5 = n5, n1
if n1 < n6:
    n1, n6 = n6, n1
print(n1)
