import sys

print(
    *map(
        lambda a: [0, 1][a[0] != a[1]],
        zip(
            sys.stdin.readline().split(),
            sys.stdin.readline().split()
        )
    )
)
