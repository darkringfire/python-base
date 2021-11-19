def move(n, x, y):
    if n == 1:
        print(1, x, y)
    else:
        t = 6 - x - y
        move(n-1, x, t)
        print(n, x, y)
        move(n-1, t, y)


def main():
    n = int(input())
    move(n, 1, 3)


main()
