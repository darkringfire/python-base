print(
    sorted(
        filter(
            lambda x: x % 2 == 1,
            map(
                int,
                open('input.txt', 'r', encoding='utf8').read().split()
            )
        )
    )[0]
)
