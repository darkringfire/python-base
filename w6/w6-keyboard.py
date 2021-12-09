"""
Тренировочное задание по программированию: Клавиатура

На региональном этапе Всероссийской олимпиады школьников по информатике
в 2009 году предлагалась следующая задача.

Всем известно, что со временем клавиатура изнашивается, и клавиши на ней
начинают залипать. Конечно, некоторое время такую клавиатуру еще можно
использовать, но для нажатий клавиш приходиться использовать большую силу.

При изготовлении клавиатуры изначально для каждой клавиши задается количество
нажатий, которое она должна выдерживать. Если знать эти величины для
используемой клавиатуры, то для определенной последовательности нажатых клавиш
можно определить, какие клавиши в процессе их использования сломаются,
а какие — нет.

Требуется написать программу, определяющую, какие клавиши сломаются в процессе
заданного варианта эксплуатации клавиатуры.

Формат ввода

Первая строка входных данных содержит целое число n (1≤n≤1000) — количество
клавиш на клавиатуре. Вторая строка содержит n целых чисел —с₁, с₂, … , сn,
где сᵢ (1≤cᵢ≤100000) — количество нажатий,выдерживаемых i-ой клавишей. Третья
строка содержит целое число k (1≤k≤100000) — общее количество нажатий клавиш,
и последняя строка содержит k целых чисел pj (1≤pj≤n) — последовательность
нажатых клавиш.

Формат вывода

Программа должна вывести n строк, содержащих информацию об исправности клавиш.
Если i-я клавиша сломалась, то i-ая строка должна содержать слово YES, если же
клавиша работоспособна — слово NO.
"""


def print_bool(b, t='YES', f='NO'):
    print(t) if b else print(f)


def main():
    n = int(input())
    resources = list(map(int, input().split()))
    k = int(input())
    clicks = list(map(int, input().split()))
    for b in clicks:
        resources[b-1] -= 1
    for b in resources:
        print_bool(b < 0)


main()
