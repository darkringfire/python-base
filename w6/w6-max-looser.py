"""
Максимальный балл не-победителя

Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся
школьники, которые набрали наибольший балл среди всех участников в данном
классе.
Для каждого класса определите максимальный балл, который набрал школьник, не
ставший победителем в данном классе.
Формат вывода
Выведите три целых числа.
"""

from collections import defaultdict


def main():
    debug = False
    cnt = defaultdict(lambda: [0, 0])
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            row = line.split()
            school = int(row[2])
            score = int(row[3])
            if cnt[school][1] < score:
                cnt[school][0], cnt[school][1] = cnt[school][1], score
            elif cnt[school][0] < score and cnt[school][1] != score:
                cnt[school][0] = score
    cnt_sort = sorted(cnt.items())
    if debug:
        print(cnt_sort)
    print(*map(lambda x: x[1][0], cnt_sort))


main()
