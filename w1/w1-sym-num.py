"""
Тренировочное задание по программированию: Симметричное число*

Дано четырехзначное число. Определите, является ли его десятичная запись
симметричной. Если число симметричное, то выведите 1, иначе выведите любое
другое целое число. Число может иметь меньше четырех знаков, тогда нужно
считать, что его десятичная запись дополняется слева нулями.

Формат ввода
Вводится единственное число.

Формат вывода
Выведите ответ на задачу.

Примечание
Десятичная запись числа симметрична, если при прочтении слева направо и справа
налево получается одно и то же число.
"""

n = int(input())
nh, nl = n // 100, n % 100

dif = nh - (nl // 10 + nl % 10 * 10)
print(dif + 1)
