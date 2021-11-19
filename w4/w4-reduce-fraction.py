def gcd(a, b):
    m = a % b
    if m == 0:
        return b
    else:
        return gcd(b, m)


def ReduceFraction(n, m):
    return n // gcd(n, m), m // gcd(n, m)


def main():
    n, m = int(input()), int(input())
    print(*ReduceFraction(n, m))


main()
