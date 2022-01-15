"""
Частотный анализ

Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую
строку. Слова должны быть отсортированы по убыванию их количества появления в
тексте, а при одинаковой частоте появления — в лексикографическом порядке.

Указание.
После того, как вы создадите словарь всех слов, вам захочется отсортировать
его по частоте встречаемости слова. Желаемого можно добиться, если создать
список, элементами которого будут кортежи из двух элементов: частота
встречаемости слова и само слово.
Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка
будет сортировать список кортежей, при этом кортежи сравниваются по первому
элементу, а если они равны — то по второму. Это почти то, что требуется в
задаче.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.
"""
from collections import defaultdict


def main():
    words = defaultdict(int)
    with open('input.txt', 'r', encoding='utf8') as f:
        for w in f.read().split():
            words[w] += 1
    for w, _ in sorted(words.items(), key=lambda x: (-x[1], x[0])):
        print(w)


main()