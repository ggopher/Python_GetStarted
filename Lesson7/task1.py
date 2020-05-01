"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


matrix = [[1, 2, 4, 6, 4], [3, 4, 5, 6, 8], [1, 9, 7, 2, 5]]
matrix2 = [[3, 2, 5, 5, 8], [3, 6, 8, 0, 3], [1, 2, 4, 6, 8]]
matrix3 = matrix

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix


    def __str__(self):
        result = ''
        for itm in self.matrix:
            result += ' '.join(map(str, itm)) + '\n'
        return result

    def __add__(self, other):       #переопределение оператора сложения
        result = self.matrix
        i = 0
        for line in matrix:
            ii = 0
            for itm in line:
                result[i][ii] = itm + other[i][ii]
                ii += 1
            i += 1
        return Matrix(result)




mtr = Matrix(matrix)

res = mtr + matrix2

print(res)


# print(mtr)      #Вывод матрицы построчно



matr = [1, 2, 4, 6, 4]