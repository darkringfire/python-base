def main():
    arr = list(map(int, input().split()))
    o_x, o_c = 0, 0
    for i in range(0, len(arr)):
        x = arr[i]
        c = 0
        for j in range(len(arr)):
            if x == arr[j]:
                c += 1
        if c > o_c:
            o_c = c
            o_x = x
    print(o_x)


main()
