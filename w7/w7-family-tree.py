"""
Родословная: подсчет уровней

В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно
один родитель. Каждом элементу дерева сопоставляется целое неотрицательное
число, называемое высотой. У родоначальника высота равна 0, у любого другого
элемента высота на 1 больше, чем у его родителя. Вам дано генеалогическое
древо, определите высоту всех его элементов.

Формат ввода

Программа получает на вход число элементов в генеалогическом древе N. Далее
следует N-1 строка, задающие родителя для каждого элемента древа, кроме
родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

Формат вывода

Программа должна вывести список всех элементов древа в лексикографическом
порядке. После вывода имени каждого элемента необходимо вывести его высоту.

Примечания

Эта задача имеет решение сложности O(n), но вам достаточно написать решение
сложности O(n²) (не считая сложности обращения к элементам словаря). Пример
ниже соответствует приведенному древу рода Романовых.
"""


def main():
    tree = dict()
    first = set()
    with open('input.txt', 'r', encoding='utf8') as f:
        n = int(f.readline())
        for _ in range(n-1):
            name, parent = f.readline().split()
            if parent not in tree:
                tree[parent] = {'parent': None, 'children': {name}, 'level': 0}
                first.add(parent)
            else:
                tree[parent]['children'].add(name)
            if name not in tree:
                tree[name] = {'children': set(), 'level': 0}
            tree[name]['parent'] = parent
            first.discard(name)

    children = first
    level = 0
    while len(children) > 0:
        new_children = set()
        for n in children:
            tree[n]['level'] = level
            new_children |= tree[n]['children']
        children = new_children
        level += 1

    for n, v in sorted(tree.items()):
        print(n, v['level'])


main()
