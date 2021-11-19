def power(a, n):
    return a * power(a, n-1) if n > 0 else 1


def main():
    a, n = float(input()), int(input())
    print(power(a, n))


main()
