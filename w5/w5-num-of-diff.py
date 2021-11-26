def main():
    arr = list(map(int, input().split()))
    cnt = 0
    prev = None
    for v in arr:
        if v != prev:
            cnt += 1
        prev = v
    print(cnt)


main()
