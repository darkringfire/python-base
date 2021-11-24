def IsAscending(arr):
    asc = True
    n = 1
    while n < len(arr):
        asc = asc and arr[n] > arr[n-1]
        n += 1
    return asc


def print_bool(b, t='YES', f='NO'):
    print(t) if b else print(f)


def main():
    arr = list(map(int, input().split()))
    print_bool(IsAscending(arr))


main()
