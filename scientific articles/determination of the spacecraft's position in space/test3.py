from random import randint, uniform
from pandas import read_excel
from math import pi, cos


def generation_table():
    base_table_cosa = [[round(cos(y * pi / 180) * cos(x * pi / 180), 3) for y in range(0, 91)] for x in range(0, 91)]
    return base_table_cosa


def find_degree(value_cosa):  # Функция находит максимально схожее теоретическое значение с получившимся
    # и выдаёт предполагаемые значения углов по осям X и Y
    if value_cosa == 0:
        result_x = 'батарея солнечная в тени'
        result_y = 'батарея солнечная в тени'
        return result_x, result_y
    else:
        base_cos = generation_table()
        min_diff = 1
        result_x = 0
        result_y = 0
        for x in range(0, 91):
            for y in range(0, 91):
                if abs(value_cosa - base_cos[x][y]) < min_diff:
                    min_diff = abs(value_cosa - base_cos[x][y])
                    result_y = x
                    result_x = y
        return result_x, result_y


print(find_degree(0.816))
