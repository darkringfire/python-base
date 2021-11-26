def main():
    arr = list(map(int, input().split()))
    for n in range(len(arr) // 2):
        arr[n*2], arr[n*2+1] = arr[n*2+1], arr[n*2]
    print(*arr, sep=' ')


main()
