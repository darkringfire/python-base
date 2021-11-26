def main():
    arr = list(map(int, input().split()))
    print(*arr[::-1], sep=' ')


main()
