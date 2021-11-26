def main():
    arr = list(map(int, input().split()))
    min_odd = None
    for v in arr:
        if v % 2 == 1:
            if min_odd is None:
                min_odd = v
            elif v < min_odd:
                min_odd = v
    print(min_odd)


main()
