def min_shift(arr, n, ns):
    if ns[0] is None:
        ns[0] = n
    elif arr[n] <= arr[ns[0]]:
        ns[1] = ns[0]
        ns[0] = n
    elif ns[1] is None or arr[n] <= arr[ns[1]]:
        ns[1] = n


def max_shift(arr, n, ns):
    if ns[0] is None:
        ns[0] = n
    elif arr[n] >= arr[ns[0]]:
        ns[1] = ns[0]
        ns[0] = n
    elif ns[1] is None or arr[n] >= arr[ns[1]]:
        ns[1] = n


def main():
    arr = list(map(int, input().split()))
    min_neg = [None, None]
    max_neg = [None, None]
    min_pos = [None, None]
    max_pos = [None, None]

    for n in range(len(arr)):
        if arr[n] < 0:
            min_shift(arr, n, min_neg)
            max_shift(arr, n, max_neg)
        else:
            min_shift(arr, n, min_pos)
            max_shift(arr, n, max_pos)

    max_mul_ns = [0, 1]
    max_mul = arr[max_mul_ns[0]] * arr[max_mul_ns[1]]
    # pos
    if max_pos[1] is not None:
        mul = arr[max_pos[0]] * arr[max_pos[1]]
        if mul > max_mul:
            max_mul_ns = max_pos
            max_mul = mul
    if min_neg[1] is not None:
        mul = arr[min_neg[0]] * arr[min_neg[1]]
        if mul > max_mul:
            max_mul_ns = min_neg
            max_mul = mul
    # neg
    if min_pos[0] is not None and max_neg[0] is not None:
        mul = arr[min_pos[0]] * arr[max_neg[0]]
        if mul > max_mul:
            max_mul_ns = arr[min_pos[0]], arr[max_neg[0]]
            # max_mul = mul
    if arr[max_mul_ns[0]] > arr[max_mul_ns[1]]:
        max_mul_ns = max_mul_ns[::-1]
    print(arr[max_mul_ns[0]], arr[max_mul_ns[1]])


main()
