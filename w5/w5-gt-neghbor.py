def main():
    arr = list(map(int, input().split()))
    cnt = 0
    for n in range(1, len(arr)-1):
        if arr[n-1] < arr[n] > arr[n+1]:
            cnt += 1
    print(cnt)


main()
