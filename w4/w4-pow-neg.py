def power(a, n):
    res = 1
    while n != 0:
        if n < 0:
            res /= a
            n += 1
        else:
            res *= a
            n -= 1
    return res


def main():
    a, n = float(input()), int(input())
    print(power(a, n))


main()
