# TODO здесь писать код
from copy import deepcopy


class Matrix:
    def __init__(self, strings, columns):
        self.data = list()
        self.strings = strings
        self.columns = columns

    def __str__(self):
        data_in_str = ''
        for i in self.data:
            data_in_str += str(i)
            data_in_str += '\n'
        return data_in_str

    def add(self, other):
        new_matrix = deepcopy(self.data)
        for i, value_string in enumerate(new_matrix):
            for j, value_column in enumerate(value_string):
                new_matrix[i][j] += other.data[i][j]
        return new_matrix

    def subtract(self, other):
        new_matrix = deepcopy(self.data)
        for i, value_string in enumerate(new_matrix):
            for j, value_column in enumerate(value_string):
                new_matrix[i][j] -= other.data[i][j]
        return new_matrix

    def multiply(self, other):
        new_matrix = [[0 for i in range(len(self.data))] for j in range(len(self.data))]
        temp_str = min(self.strings, other.strings)
        temp_col = min(self.strings, other.columns)

        for i in range(temp_str):
            for j in range(temp_col):
                temp_value_1 = 0
                for num in range(self.columns):
                    temp_value_1 += self.data[i][num] * other.data[num][j]
                new_matrix[i][j] = temp_value_1
        return new_matrix

    def transpose(self):
        new_matrix = [[0 for i in range(self.strings)] for j in range(self.columns)]
        for i in range(self.columns):
            for j in range(self.strings):
                new_matrix[i][j] = self.data[j][i]
        return new_matrix




# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))
#
m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]
#
print()
print("Матрица 1:")
print(m1)

print("Матрица 3:")
print(m3)
print()

print("Умножение матриц:")
print(m1.multiply(m3))

print("Матрица 1:")
print(m1)

print("Транспонирование матрицы 1:")
print(m1.transpose())
