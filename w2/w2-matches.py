l1, r1 = int(input()), int(input())
l2, r2 = int(input()), int(input())
l3, r3 = int(input()), int(input())

d1 = r1 - l1
d2 = r2 - l2
d3 = r3 - l3
s12 = 0
s13 = 0
s23 = 0

if r1 < l2:
    s12 = l2 - r1
if r2 < l1:
    s12 = l1 - r2

if r1 < l3:
    s13 = l3 - r1
if r3 < l1:
    s13 = l1 - r3

if r2 < l3:
    s23 = l3 - r2
if r3 < l2:
    s23 = l2 - r3


if s12 == s13 == 0 or s12 == s23 == 0 or s13 == s23 == 0:
    print(0)
elif d1 >= s23:
    print(1)
elif d2 >= s13:
    print(2)
elif d3 >= s12:
    print(3)
else:
    print(-1)
