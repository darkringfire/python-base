from math import sqrt


def MinDivisor(n):
    r = sqrt(n)
    d = 2
    while d <= r:
        if n % d == 0:
            return d
        d += 1
    return n


def IsPrime(n):
    return n == MinDivisor(n)


def print_bool(b, t='YES', f='NO'):
    print(t) if b else print(f)


def main():
    n = int(input())
    print_bool(IsPrime(n))


main()
