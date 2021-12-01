def print_bool(b, t='YES', f='NO'):
    print(t) if b else print(f)


def main():
    queens = []
    for i in range(8):
        queens.append(tuple(map(int, input().split())))
    beat = False

    for i in range(len(queens) - 1):
        xi, yi = queens[i][0], queens[i][1]
        for j in range(i+1, len(queens)):
            xj, yj = queens[j][0], queens[j][1]
            if xi + yi == xj + yj or xi - yi == xj - yj:
                beat = True
            elif xi == xj or yi == yj:
                beat = True

    print_bool(beat)


main()
