def main():
    arr = list(map(int, input().split()))
    min_pos = None
    for v in arr:
        if v > 0:
            if min_pos is None:
                min_pos = v
            elif v < min_pos:
                min_pos = v
    print(min_pos)


main()
