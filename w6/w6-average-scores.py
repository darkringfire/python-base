"""
Тренировочное задание по программированию: Средний балл по классам

В олимпиаде по информатике принимало участие несколько человек.
Определите и выведите средние баллы участников олимпиады в 9 классе, в 10
классе, в 11 классе.

Входные данные
Информация о результатах олимпиады записана в файле, каждая строка которого
имеет вид:
фамилия имя класс балл.
Фамилия и имя — текстовые строки, не содержащие пробелов. Класс - одно из трех
чисел 9, 10, 11. Балл - целое число от 0 до 100.

В этой задаче файл необходимо считывать построчно, не сохраняя содержимое
файла в памяти целиком.

Выходные данные
Выведите три числа: средние баллы по 9 классу, по 10 классу, по 11 классу.
Входной файл в кодировке utf-8
(используйте open('input.txt', 'r', encoding='utf-8')).
"""


class Participant:
    def __init__(self, row):
        """

        :type row: str
        """
        vals = row.split()
        self.l_name, self.f_name = vals[0:2]
        self.group, self.score = tuple(map(int, vals[2:4]))


def main():
    scores = {}
    with open('input.txt', 'r', encoding='utf-8') as f:
        for row in f:
            p = Participant(row)
            group_score = scores.get(p.group, [0, 0])
            group_score[0] += 1
            group_score[1] += p.score
            scores[p.group] = group_score
    avg_score = list(map(lambda s: s[1][1]/s[1][0], sorted(scores.items())))
    print(*avg_score)


main()
