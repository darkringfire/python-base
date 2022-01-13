"""
Самое частое слово

Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если
таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
"""
from collections import defaultdict


def main():
    words = defaultdict(int)
    with open('input.txt', 'r', encoding='utf8') as f:
        for w in f.read().split():
            words[w] += 1
    print(sorted(words.items(), key=lambda i: (-i[1], i[0]))[0][0])


main()
