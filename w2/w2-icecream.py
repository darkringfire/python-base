k = int(input())

if k % 3 == 0 or \
        (k >= 5 and (k - 5) % 3 == 0) or \
        (k >= 10 and (k - 10) % 3 == 0):
    print('YES')
else:
    print('NO')
