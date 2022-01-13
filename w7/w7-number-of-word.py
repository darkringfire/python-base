"""
Номер появления слова

Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных подряд идущих символов.
Слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в
этом тексте ранее.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.
"""


def main():
    with open('input.txt', 'r', encoding='utf8') as f:
        words = {}
        for w in f.read().split():
            words[w] = words.get(w, -1) + 1
            print(words[w], end=' ')


main()