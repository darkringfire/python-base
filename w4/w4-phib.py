def phib(n):
    if n > 1:
        return phib(n-1) + phib(n-2)
    else:
        return n


def main():
    n = int(input())
    print(phib(n))


main()
