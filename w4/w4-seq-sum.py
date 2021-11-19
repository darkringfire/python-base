def in_sum():
    n = int(input())
    if n == 0:
        return 0
    else:
        return n + in_sum()


def main():
    print(in_sum())


main()
