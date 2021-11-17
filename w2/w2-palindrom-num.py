k = int(input())

n = 0
x = 0
while x < k:
    x += 1
    p1 = x
    p2 = 0
    while p1 > 0:
        p2 = p2 * 10 + p1 % 10
        p1 //= 10
    if p2 == x:
        n += 1
print(n)
