"""
Пересадки

На Новом проспекте для разгрузки было решено пустить два новых автобусных
маршрута на разных участках проспекта.  Известны конечные остановки каждого
из автобусов. Определите количество остановок, на которых можно пересесть с
одного автобуса на другой.

Формат ввода
Вводятся четыре числа, не превосходящие 100, задающие номера конечных
остановок. Сначала для первого, потом второго автобуса (см. примеры и рисунок).

Формат вывода
Ваша программа должна выводить одно число – искомое количество остановок.

Примечания
      1-й автобус
     |----------|
1--2--3--4--5--6
  |-------|
   2-й автобус
Пояснения Первый пример (см. рисунок): первый автобус ходит с 3-й остановки
по 6-ю и обратно, а второй с 2-й по 4-ю и обратно. Пересесть с одного
автобуса на другой можно на 3-й и 4-й остановках. Их две. Второй пример:
автобусы не имеют общих остановок.
"""


def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        stops = list(map(int, f.readline().split()))
        left = max(min(*stops[:2]), min(*stops[-2:]))
        right = min(max(*stops[:2]), max(*stops[-2:]))
        print(max(0, right-left+1))


main()