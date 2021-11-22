def count0(n):
    c = 0
    for i in range(n):
        x = int(input())
        if x == 0:
            c += 1
    return c


def main():
    n = int(input())
    print(count0(n))


main()
