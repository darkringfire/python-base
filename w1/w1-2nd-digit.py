"""
Тренировочное задание по программированию: Вторая справа цифра

Дано натуральное число. Найдите цифру, стоящую в разряде десятков
в его десятичной записи (вторую справа цифру или 0, если число меньше 10).

Замечание
Предполагается решение этой задачи без использования строковых методов.
Пожалуйста, пользуйтесь арифметикой.

Формат ввода
Вводится единственное число.

Формат вывода
Выведите ответ на задачу.
"""

print(int(input()) // 10 % 10)
