def in_rev():
    n = int(input())
    if n != 0:
        in_rev()
    print(n)


def main():
    in_rev()


main()
