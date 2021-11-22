def main():
    n = int(input())
    print(' '.join(map(str, range(10**n - 1, 10**(n-1)-1, -2))))


main()
