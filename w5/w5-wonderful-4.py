def is_palindrome4(x):
    xh, xl = x // 100, x % 100
    xl = xl // 10 + xl % 10 * 10
    return xl == xh


def main():
    a, b = int(input()), int(input())
    if a > b:
        a, b = b, a
    for x in range(a, b+1):
        if is_palindrome4(x):
            print(x)


main()
