n = int(input())
m = n
while n != 0:
    if n > m and n != 0:
        m = n
    n = int(input())
print(m)
