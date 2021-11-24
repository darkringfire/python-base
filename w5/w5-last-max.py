def main():
    arr = list(map(int, input().split()))
    max_n, max_v = 0, arr[0]
    for n, v in enumerate(arr):
        if v > max_v:
            max_v = v
        if v == max_v:
            max_n = n
    print(max_v, max_n, sep=' ')


main()
