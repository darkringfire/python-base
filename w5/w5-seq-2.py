def main():
    a, b = int(input()), int(input())
    seq = range(a, b + 1) if a < b else range(a, b - 1, -1)
    print(' '.join(map(str, seq)))


main()
