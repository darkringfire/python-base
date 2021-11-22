def main():
    n = int(input())
    r = range(n)
    print('+___ ' * n)
    for f in r:
        print('|', f+1, ' /', sep='', end=' ')
    print()
    print('|__\\ ' * n)
    print('|    ' * n)


main()
