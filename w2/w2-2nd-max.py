n = int(input())
m = m2 = 0
while n != 0:
    if n != 0:
        if n > m:
            m, m2 = n, m
        elif n > m2:
            m2 = n
    n = int(input())
print(m2)
