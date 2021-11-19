def print_sqr(was=False):
    n = int(input())
    if n != 0:
        was = was or print_sqr()
        if int(n ** .5) ** 2 == n:
            print(n, end=' ')
            return True
    return was


def main():
    if not print_sqr():
        print(0)


main()
