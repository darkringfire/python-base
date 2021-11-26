def main():
    arr = input().split()
    t = arr[-1]
    for n in range(len(arr)-1, 0, -1):
        arr[n] = arr[n-1]
    arr[0] = t

    print(*arr)


main()
