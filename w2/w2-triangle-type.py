a, b, c = int(input()), int(input()), int(input())

if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b

if a + b > c:
    ab2 = a ** 2 + b ** 2
    c2 = c ** 2
    if ab2 == c2:
        print('rectangular')
    elif ab2 > c2:
        print('acute')
    else:
        print('obtuse')
else:
    print('impossible')
