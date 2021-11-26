def main():
    arr = list(map(int, input().split()))
    for i in range(len(arr) // 2):
        arr[i], arr[-i-1] = arr[-i-1], arr[i]
    print(*arr, sep=' ')


main()
