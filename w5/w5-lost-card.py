def count_cards(n):
    c = n
    for i in range(1, n):
        c += i - int(input())
    return c


def main():
    n = int(input())
    print(count_cards(n))


main()
