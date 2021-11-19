def sqrs(n, d=0):
    if n > 0:
        d += 1
        if d > 4:
            return d
        r = int(n ** .5)
        cur_d = d
        a = n - r ** 2
        d = sqrs(a, cur_d)
        while r > 0 and d > 4:
            r -= 1
            a = n - r ** 2
            d = sqrs(a, cur_d)
        if d <= 4:
            print(r, end=' ')

    return d


def main():
    n = int(input())
    sqrs(n)


main()
