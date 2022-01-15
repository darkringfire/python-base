"""
Банковские счета

Некоторый банк хочет внедрить систему управления счетами клиентов,
поддерживающую следующие операции:

Пополнение счета клиента.
Снятие денег со счета.
Запрос остатка средств на счете.
Перевод денег между счетами клиентов.
Начисление процентов всем клиентам.

Вам необходимо реализовать такую систему. Клиенты банка идентифицируются
именами (уникальная строка, не содержащая пробелов). Первоначально у банка нет
ни одного клиента. Как только для клиента проводится операция пополнения,
снятия или перевода денег, ему заводится счет с нулевым балансом. Все
дальнейшие операции проводятся только с этим счетом. Сумма на счету может быть
как положительной, так и отрицательной, при этом всегда является целым числом.

Формат ввода
Входной файл содержит последовательность операций. Возможны следующие операции:

DEPOSIT name sum - зачислить сумму sum на счет клиента name. Если у клиента нет
счета, то счет создается.

WITHDRAW name sum - снять сумму sum со счета клиента name. Если у клиента нет
счета, то счет создается.

BALANCE name - узнать остаток средств на счету клиента name.

TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1 на счет
клиента name2. Если у какого-либо клиента нет счета, то ему создается счет.

INCOME p - начислить всем клиентам, у которых открыты счета, p% от суммы счета.
Проценты начисляются только клиентам с положительным остатком на счету, если у
клиента остаток отрицательный, то его счет не меняется. После начисления
процентов сумма на счету остается целой, то есть начисляется только целое число
денежных единиц. Дробная часть начисленных процентов отбрасывается.

Формат вывода

Для каждого запроса BALANCE программа должна вывести остаток на счету данного
клиента. Если же у клиента с запрашиваемым именем не открыт счет в банке,
выведите ERROR.
"""
from collections import defaultdict


def main():
    clients = defaultdict(int)
    with open('input.txt', 'r', encoding='utf8') as f:
        for line in f:
            row = line.split()
            if row[0] == 'DEPOSIT':
                clients[row[1]] += int(row[2])
            elif row[0] == 'WITHDRAW':
                clients[row[1]] -= int(row[2])
            elif row[0] == 'BALANCE':
                if row[1] in clients:
                    print(clients[row[1]])
                else:
                    print('ERROR')
            elif row[0] == 'TRANSFER':
                clients[row[1]] -= int(row[3])
                clients[row[2]] += int(row[3])
            elif row[0] == 'INCOME':
                for c in clients.keys():
                    if clients[c] > 0:
                        clients[c] += (clients[c] * int(row[1])) // 100


main()
