def main():
    arr = list(map(int, input().split()))
    max_n, max_v = 0, arr[0]
    for n in range(1, len(arr)):
        if arr[n] > max_v:
            max_v = arr[n]
            max_n = n
    print(max_v, max_n, sep=' ')


main()
