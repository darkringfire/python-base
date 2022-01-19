from itertools import accumulate

print(
    *accumulate(
        map(int, open('input.txt').read().split()),
        lambda s, x: s+x
    )
)
