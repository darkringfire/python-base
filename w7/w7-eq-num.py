"""
Количество совпадающих

Даны два списка чисел, которые могут содержать до 100000 чисел каждый.
Посчитайте, сколько чисел содержится одновременно как в первом списке,
так и во втором.

Примечание. Эту задачу на Питоне можно решить в одну строчку.

Формат ввода
Вводятся два списка чисел. Все числа каждого списка находятся
на отдельной строке.

Формат вывода
Выведите ответ на задачу.
"""

print(len(set(input().split()) & set(input().split())))
