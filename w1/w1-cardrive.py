"""
Тренировочное задание по программированию: Автопробег

За день машина проезжает N километров. Сколько дней нужно, чтобы проехать
маршрут длиной M километров?

Формат ввода
Программа получает на вход числа N и M (целые, положительные).

Формат вывода
Выведите ответ на задачу.
"""

n, m = int(input()), int(input())
print((m + n - 1) // n)
