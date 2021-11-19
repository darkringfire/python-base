from math import sqrt


def MinDivisor(n):
    r = sqrt(n)
    d = 2
    while d <= r:
        if n % d == 0:
            return d
        d += 1
    return n


def main():
    n = int(input())
    print(MinDivisor(n))


main()
