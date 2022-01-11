"""
Пример решения сложной задачи на словари

Рассмотрим такую задачу: словарь задан в виде набора строк, в каждой строке
записано слово на английском языке, затем следует символ '-', затем, через
запятую, перечислены возможные переводы слова на латынь.

Требуется составить латино-английский словарь и вывести его в том же виде.
Все слова должны быть упорядочены по алфавиту. Возможные переводы одного
слова должны быть также упорядочены по алфавиту.
"""


from collections import defaultdict


def main():
    lat_en = defaultdict(lambda: set())
    with open('input.txt', 'r', encoding='utf-8') as f:
        n = int(f.readline())
        for _ in range(n):
            en, lats = tuple(f.readline().strip().split(' - '))
            for lat in lats.split(', '):
                lat_en[lat].add(en)
    print(len(lat_en))
    for lat, en in sorted(lat_en.items()):
        print(lat, ', '.join(sorted(en)), sep=' - ')


main()
