def main():
    n = int(input())
    s = 0
    for x in range(1, n+1):
        s += x**2
    print(s)


main()
