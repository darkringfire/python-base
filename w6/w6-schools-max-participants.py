"""
Школы с наибольшим числом участников олимпиады

В олимпиаде по информатике принимало участие N человек. Определите школы, из
которых в олимпиаде принимало участие больше всего участников. В этой задаче
необходимо считывать данные построчно, не сохраняя в памяти данные обо всех
участниках, а только подсчитывая число участников для каждой школы.

Формат ввода

Информация о результатах олимпиады записана в файле, каждая из строк которого
имеет вид:

фамилия имя школа балл

Фамилия и имя — текстовые строки, не содержащие пробелов. Школа — целое число
от 1 до 99. Балл — целое число от 0 до 100.

Формат вывода

Выведите номера этих школ в порядке возрастания.
"""
from collections import defaultdict


def main():
    debug = True
    cnt = defaultdict(lambda: 0)
    max_participants = 0
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            row = line.split()
            school = int(row[2])
            if debug:
                print(school)
            cnt[school] += 1
            if cnt[school] > max_participants:
                max_participants = cnt[school]
    sorted_counters = sorted(
        cnt.items(),
        key=lambda k: (-k[1], k[0])
    )
    if debug:
        print(cnt)
        print(sorted_counters)
        print(max_participants)


main()
