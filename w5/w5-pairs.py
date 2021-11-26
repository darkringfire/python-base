def main():
    arr = list(map(int, input().split()))
    pairs = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                pairs += 1
    print(pairs)


main()
