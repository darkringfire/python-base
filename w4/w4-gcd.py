def gcd(a, b):
    m = a % b
    if m == 0:
        return b
    else:
        return gcd(b, m)


def main():
    a, b = int(input()), int(input())
    print(gcd(a, b))


main()
