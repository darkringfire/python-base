def main():
    arr = list(map(int, input().split()))
    n, end = 0, len(arr)
    while n < end:
        if arr[n] == 0:
            arr.append(arr.pop(n))
            end -= 1
        else:
            n += 1
    print(*arr)


main()
