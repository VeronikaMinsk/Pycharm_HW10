# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# HW4-1 Напишите функцию для транспонирования матрицы
class MatrixTransposer:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def transpose(self):
        transposed = [[0] * self.rows for _ in range(self.cols)]

        for i in range(self.rows):
            for j in range(self.cols):
                transposed[j][i] = self.matrix[i][j]

        return transposed

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix_transposer = MatrixTransposer(matrix)
transposed_matrix = matrix_transposer.transpose()

print('\nИсходная матрица:')
for row in matrix:
    print(row)

print('\nТранспонированная матрица:')
for row in transposed_matrix:
    print(row)
