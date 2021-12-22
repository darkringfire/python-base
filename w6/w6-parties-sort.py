"""
Упорядочить список партий по числу голосов

Формат входных данных аналогичен предыдущей задаче. Выведите список всех
партий, участвовавших в выборах, отсортировав его в порядке убывания
количества голосов избирателей, а при равном количестве голосов - в
лексикографическом порядке.
"""


def main():
    parties = {}
    with open('input.txt', 'r', encoding='utf-8') as f:
        _ = f.readline()
        while True:
            row = f.readline().strip()
            if row != 'VOTES:':
                parties[row] = 0
            else:
                break
        for row in f:
            parties[row.strip()] += 1
    parties_sort = sorted(parties.items(), key=lambda p: (-p[1], p[0]))
    for p in parties_sort:
        print(p[0])


main()
