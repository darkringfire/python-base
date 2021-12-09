"""
Количество победителей по классам

В условиях предыдущей задачи определите количество школьников, ставших
победителями в каждом классе. Победителями объявляются все, кто набрал
наибольшее число баллов по данному классу. Гарантируется, что в каждом классе
был хотя бы один участник.

Формат вывода

Выведите три числа: количество победителей олимпиады по 9 классу, по 10 классу,
по 11 классу.
"""
from collections import defaultdict


def main():
    participants = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            row = line.split()
            participants.append((row[0], row[1], int(row[2]), int(row[3])))
    winners = defaultdict(lambda: (0, 0))
    for _, _, group, score in participants:
        max_score, count = winners[group]
        if score > max_score:
            winners[group] = (score, 1)
        elif score == max_score:
            winners[group] = (score, count+1)
    win_cnt = list(map(
        lambda w: w[1][1],
        sorted(winners.items())
    ))
    print(*win_cnt)


main()
