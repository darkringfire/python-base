def is_in1(a):
    return -1 <= a <= 1


def print_yes_no(b):
    if b:
        print('YES')
    else:
        print('NO')


x, y = float(input()), float(input())

print_yes_no(is_in1(x) and is_in1(y))
