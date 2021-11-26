def main():
    arr = list(map(int, input().split()))
    k = int(input())
    for i in range(k, len(arr)-1):
        arr[i] = arr[i+1]
    arr.pop()
    print(*arr, sep=' ')


main()
