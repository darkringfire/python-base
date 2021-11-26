def main():
    arr = list(map(int, input().split()))
    mins = []
    maxs = []
    for val in arr:
        mins.append(val)
        maxs.append(val)
        mins.sort()
        maxs.sort(reverse=True)
        if len(mins) > 2:
            mins = mins[:2]
        if len(maxs) > 3:
            maxs = maxs[:3]
    vals = maxs
    if mins[0] * mins[1] * maxs[0] > maxs[0] * maxs[1] * maxs[2]:
        vals = mins + maxs[:1]
    print(*vals)


main()
