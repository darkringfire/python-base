def main():
    arr = list(map(int, input().split()))
    x = int(input())
    n = 0
    while n < len(arr) and x <= arr[n]:
        n += 1
    print(n+1)


main()
