def my_abs(x):
    if x < 0:
        return -x
    return x


def diff(a, b):
    return my_abs(a - b)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())

    closest = arr[0]
    for v in arr:
        if diff(v, x) < diff(closest, x):
            closest = v
    print(closest)


main()
