"""
Встречалось ли число раньше

Во входной строке записана последовательность чисел через пробел. Для каждого
числа выведите слово YES (в отдельной строке), если это число ранее
встречалось в последовательности или NO, если не встречалось.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.
"""


def print_bool(b, t='YES', f='NO'):
    print(t) if b else print(f)


nums = input().split()
was = set()
for n in nums:
    print_bool(n in was)
    was.add(n)
