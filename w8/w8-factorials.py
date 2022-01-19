from itertools import accumulate

print(
    1,
    *accumulate(
        range(1, int(input())+1),
        lambda a, x: a*x
    )
)
