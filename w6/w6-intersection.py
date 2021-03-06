"""
Тренировочное задание по программированию: Пересечение множеств

Даны два списка, упорядоченных по возрастанию (каждый список состоит
из различных элементов).

Найдите пересечение множеств элементов этих списков, то есть те числа,
которые являются элементами обоих списков. Алгоритм должен иметь сложность
O(len(A)+len(B)).

Решение оформите в виде функции Intersection(A, B). Функция должна возвращать
список пересечения данных списков в порядке возрастания элементов.
Модифицировать исходные списки запрещается.

Формат ввода
Программа получает на вход два возрастающих списка, каждый в отдельной строке.

Формат вывода
Программа должна вывести последовательность возрастающих чисел, являющихся
элементами обоих списков.
"""


def intersection(a, b):
    c = []
    ia = ib = 0
    a_len, b_len = len(a), len(b)
    while ia < a_len or ib < b_len:
        if ia == a_len or ib == b_len:
            ia = a_len
            ib = b_len
        elif a[ia] < b[ib]:
            ia += 1
        elif a[ia] > b[ib]:
            ib += 1
        else:
            c.append(a[ia])
            ia += 1
            ib += 1
    return c


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = intersection(a, b)
    print(*c)


main()
