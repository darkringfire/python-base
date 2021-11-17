n = int(input())

prev = n
seq_n = prev_dif = prev_max_n = space = min_space = 0
while n != 0:
    seq_n += 1
    # print(seq_n, n)
    dif = n - prev
    if prev_dif > 0 > dif:
        max_n = seq_n - 1
        if prev_max_n > 0:
            space = max_n - prev_max_n
        prev_max_n = max_n
        # print('max_n', seq_n - 1, 'space', space)

    if (min_space == 0) != (space < min_space):
        min_space = space
    prev = n
    prev_dif = dif
    n = int(input())
print(min_space)
