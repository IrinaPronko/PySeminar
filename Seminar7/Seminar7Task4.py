# Программа перегрузки и сложения двух матриц
import numpy as np


class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0 for i in range(col)] for j in range(row)]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self, matr=None):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


row = int(input('Введите количество строк в массивах - '))
col = int(input('Введите количество столбцов в массивах - '))
matr1 = np.random.randint(10, 99, size=(row, col))
print('Вывод первого массива:')
print(matr1)
matr2 = np.random.randint(10, 99, size=(row, col))
print('Вывод второго массива:')
print(matr2)
my_matrix = Matrix(matr1, matr2)
print('Вывод результата сложения двух массивов:')
print(my_matrix.__add__())
exit()
