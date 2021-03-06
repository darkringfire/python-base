"""
Задание по программированию: Слияние списков

Даны два целочисленных списка A и B, упорядоченных по неубыванию.
Объедините их в один упорядоченный список С (то есть он должен содержать
len(A)+len(B) элементов). Решение оформите в виде функции merge(A, B),
возвращающей новый список. Алгоритм должен иметь сложность O(len(A)+len(B)).
Модифицировать исходные списки запрещается. Использовать функцию sorted
и метод sort запрещается.

Формат ввода
Программа получает на вход два неубывающих списка, каждый в отдельной строке.

Формат вывода
Программа должна вывести последовательность неубывающих чисел, полученных
объединением двух данных списков.
"""


def merge(a, b):
    c = []
    ia = ib = 0
    a_len, b_len = len(a), len(b)
    while ia < a_len or ib < b_len:
        if ia == a_len:
            c.extend(b[ib:])
            ib = b_len
        elif ib == b_len:
            c.extend(a[ia:])
            ia = a_len
        elif a[ia] < b[ib]:
            c.append(a[ia])
            ia += 1
        else:
            c.append(b[ib])
            ib += 1
    return c


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = merge(a, b)
    print(*c)


main()
