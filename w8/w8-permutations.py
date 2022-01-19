from itertools import permutations

print(
    *map(
        lambda x: ''.join(
            map(str, x)
        ),
        permutations(range(1, int(input())+1))
    ),
    sep='\n'
)
