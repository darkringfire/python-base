def main():
    arr = list(map(int, input().split()))
    min_n = max_n = 0
    for n in range(1, len(arr)):
        if arr[n] > arr[max_n]:
            max_n = n
        if arr[n] < arr[min_n]:
            min_n = n
    arr[min_n], arr[max_n] = arr[max_n], arr[min_n]
    print(*arr)


main()
