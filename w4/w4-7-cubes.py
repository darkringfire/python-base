def cubes(n, d=0):
    if n > 0:
        d += 1
        if d > 7:
            return d
        r = int(n ** (1/3))
        cur_d = d
        a = n - r ** 3
        d = cubes(a, cur_d)
        while r > 0 and d > 7:
            r -= 1
            a = n - r ** 3
            d = cubes(a, cur_d)
        if d <= 7:
            print(r**3, end=' ')

    return d


def main():
    n = int(input())
    if cubes(n) > 7:
        print(0)


main()
