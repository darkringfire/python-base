def main():
    arr = list(map(int, input().split()))
    k, c = tuple(map(int, input().split()))

    arr.append(arr[-1])
    for i in range(len(arr)-1, k, -1):
        arr[i] = arr[i-1]
    arr[k] = c
    print(*arr, sep=' ')


main()
