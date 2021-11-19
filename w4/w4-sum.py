def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a-1, b) + 1


def main():
    a, b = int(input()), int(input())
    print(sum(a, b))


main()
