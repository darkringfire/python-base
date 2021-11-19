def xor(a1, a2):
    return a1 != a2


def print_bool(b, t='YES', f='NO'):
    if b:
        print(t)
    else:
        print(f)


x, y = int(input()), int(input())

print_bool(xor(x, y), '1', '0')
