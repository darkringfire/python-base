def print_yes_no(b):
    if b:
        print('YES')
    else:
        print('NO')


def is_in_sqr2(x, y):
    return x-1 <= y <= x+1 and -x-1 <= y <= -x+1


px, py = float(input()), float(input())

print_yes_no(is_in_sqr2(px, py))
