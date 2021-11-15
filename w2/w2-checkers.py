x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 + x2) % 2 == (y1 + y2) % 2 and y2 > y1 and \
        y1 - y2 <= x2 - x1 <= y2 - y1:
    print('YES')
else:
    print('NO')
