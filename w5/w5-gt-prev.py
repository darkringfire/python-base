def main():
    arr = map(int, input().split())
    prev = None
    out = []
    for v in arr:
        if prev is not None and v > prev:
            out.append(v)
        prev = v
    print(*out, sep=' ')


main()
