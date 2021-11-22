def is_wonderful(x):
    m = 1
    tmp = x
    while tmp > 0:
        m *= tmp % 10
        tmp //= 10
    m *= 2
    return x == m


def main():
    seq = []
    for i in range(10, 100):
        if is_wonderful(i):
            seq.append(i)
    print(*seq)


main()
