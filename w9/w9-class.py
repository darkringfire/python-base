"""
Класс

Реализуйте класс Matrix. Он должен содержать:
 Конструктор от списка списков. Гарантируется, что списки состоят из чисел, не
 пусты и все имеют одинаковый размер. Конструктор должен копировать содержимое
 списка списков, т. е. при изменении списков, от которых была сконструирована
 матрица, содержимое матрицы изменяться не должно.

 Метод __str__, переводящий матрицу в строку. При этом элементы внутри одной
 строки должны быть разделены знаками табуляции, а строки — переносами строк.
После каждой строки не должно быть символа табуляции и в конце не должно быть
переноса строки.

 Метод size без аргументов, возвращающий кортеж вида (число строк, число
 столбцов). Пример теста с участием этого метода есть в следующей задаче этой
 недели.

 __add__, принимающий вторую матрицу того же размера и возвращающий сумму
 матриц.

 __mul__, принимающий число типа int или float и возвращающий матрицу,
 умноженную на скаляр.

 __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том
 случае, аргумент находится справа. Для реализации этого метода в коде класса
 достаточно написать __rmul__ = __mul__.

Добавьте в программу из предыдущей задачи класс MatrixError, содержащий внутри
self поля matrix1 и matrix2 — ссылки на матрицы.

В класс Matrix внесите следующие изменения:

 Добавьте в метод __add__ проверку на ошибки в размере входных данных, чтобы
 при попытке сложить матрицы разных размеров было выброшено исключение
 MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым
 аргументом __add__ (просто self), а matrix2 — вторым (второй операнд для
 сложения).

 Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат
 (данный метод модифицирует экземпляр класса Matrix)

 Реализуйте статический метод transposed, принимающий Matrix и возвращающий
 транспонированную матрицу. Пример статического метода.

 Измените метод __mul__ таким образом, чтобы матрицы можно было умножать как на
 скаляры, так и на другие матрицы. В случае, если две матрицы перемножить
 невозможно, то тогда выбросьте ошибку MatrixError. Первая матрице в ошибке —
 это self, вторая — это второй операнд умножения.

Формат ввода
Вводится исходный код тестирующей программы на языке Python.

Формат вывода
Выведите результат её работы в текущем окружении при помощи exec, как это
указано в условии.
"""
from functools import reduce
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1, self.matrix2 = matrix1, matrix2


class Matrix:
    @staticmethod
    def transposed(matrix):
        """

        @type matrix: Matrix
        """
        return Matrix(matrix.arr).transpose()

    def __init__(self, arr):
        """

        @type arr: list[list[int]]
        """
        self.arr = []
        for r in arr:
            self.arr.append(r.copy())

    def __str__(self):
        return '\n'.join(map(lambda r: '\t'.join(map(str, r)), self.arr))

    def size(self):
        return len(self.arr), len(self.arr[0])

    def __add__(self, other):
        """

        @type other: Matrix
        """
        if self.size() != other.size():
            raise MatrixError(self, other)
        return Matrix(
            list(map(
                    lambda a: list(map(sum, zip(*a))),
                    zip(self.arr, other.arr)
            ))
        )

    def __mul__(self, other):
        """

        @type other: int|float|Matrix
        """
        if isinstance(other, (int, float)):
            return Matrix(
                list(map(
                    lambda r: list(map(
                        lambda x: x * other,
                        r
                    )),
                    self.arr
                ))
            )
        elif isinstance(other, Matrix) and self.size()[1] == other.size()[0]:
            return Matrix(
                list(map(
                    lambda row1: list(map(
                        lambda col2: sum(map(
                            lambda r1ijc2ji: reduce(
                                lambda x, y: x * y,
                                r1ijc2ji,
                                1
                            ),
                            zip(row1, col2)
                        )),
                        Matrix(other.arr).transpose().arr
                    )),
                    self.arr
                ))
            )
        else:
            raise MatrixError(self, other)

    __rmul__ = __mul__

    def transpose(self):
        self.arr = list(map(
            list,
            zip(*self.arr)
        ))
        return self

    def solve(self, free):
        """

        @type free: list
        """
        a = list(map(
            lambda r: r[0] + [r[1]],
            zip(self.arr, free)
        ))
        n = len(a)
        try:
            for k in range(1, n):
                for j in range(k, n):
                    m = a[j][k-1] / a[k-1][k-1]
                    for i in range(n+1):
                        a[j][i] -= m * a[k-1][i]
            x = [0 for _ in range(n)]
            for i in range(n-1, -1, -1):
                x[i] = a[i][n] / a[i][i]
                for c in range(n-1, i, -1):
                    x[i] -= a[i][c] * x[c] / a[i][i]
            return x
        except ZeroDivisionError as e:
            raise e


class SquareMatrix(Matrix):
    def __mul__(self, other):
        return SquareMatrix(super().__mul__(other).arr)

    def __pow__(self, p, modulo=None):
        if p in [0, 1]:
            return self
        elif p == 2:
            return self * self
        if p % 2 != 0:
            return self * (self ** (p - 1))
        else:
            return (self * self) ** (p // 2)


exec(stdin.read())
