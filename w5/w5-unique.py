def main():
    arr = list(map(int, input().split()))
    indexes = list(range(len(arr)))
    n = 0
    while n < len(indexes):
        val = arr[indexes[n]]
        rem = False
        i = n+1
        while i < len(indexes):
            if val == arr[indexes[i]]:
                indexes.pop(i)
                rem = True
            else:
                i += 1
        if rem:
            indexes.pop(n)
        else:
            n += 1

    unique = []
    for i in indexes:
        unique.append(arr[i])
    print(*unique)


main()
