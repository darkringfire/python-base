def main():
    arr = input().split()
    evens = []
    for i in arr:
        if int(i) % 2 == 0:
            evens.append(i)
    print(' '.join(evens))


main()
