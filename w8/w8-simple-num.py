from math import sqrt

print(
    *filter(
        lambda x: all(map(
            lambda d: x == d or x % d != 0,
            [2] + list(range(3, int(sqrt(x)) + 1, 2))
        )),
        range(2, int(input())+1)
    )
)
