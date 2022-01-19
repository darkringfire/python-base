from functools import reduce

print(
    reduce(
        lambda m, n: m * int(n)**5,
        open('input.txt').read().split(),
        1
    )
)
