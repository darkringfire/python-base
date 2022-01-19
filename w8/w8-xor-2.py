print(
    *map(
        lambda x: sum(x) % 2,
        zip(
            *map(
                lambda x: list(
                    map(int, input().split())),
                range(int(input()))
            )
        )
    )
)
