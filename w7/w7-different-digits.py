"""
Количество различных чисел

Дан список чисел, который может содержать до 100000 чисел.Определите,
сколько в нем встречается различных чисел.

Формат ввода
Вводится список целых чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.
"""


def main():
    num_set = set(input().split())
    print(len(num_set))


main()
