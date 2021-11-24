def main():
    arr = list(map(int, input().split()))
    prev = None
    for v in arr:
        if prev is not None and v * prev > 0:
            print(prev, v, sep=' ')
            break
        prev = v


main()
