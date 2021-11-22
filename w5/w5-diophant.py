def is_diophant(x, a, b, c, d, e):
    return x != e and a * x**3 + b * x**2 + c * x + d == 0


def main():
    coef = []
    for i in range(5):
        coef.append(int(input()))

    seq = []
    for x in range(0, 1001):
        if is_diophant(x, *coef):
            seq.append(x)
    print(len(seq))


main()
