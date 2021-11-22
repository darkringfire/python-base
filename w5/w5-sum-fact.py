def main():
    n = int(input())
    s = 0
    f = 1
    for x in range(1, n+1):
        f *= x
        s += f
    print(s)


main()
