def main():
    arr = input().split()
    positives = []
    for i in arr:
        if int(i) > 0:
            positives.append(i)
    print(len(positives))


main()
