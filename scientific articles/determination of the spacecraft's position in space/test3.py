from random import randint, uniform
from pandas import read_excel
from math import pi, cos, ceil
from decimal import *


def generation_table():
    base_table_cosa = [[Decimal(cos(y * pi / 180) * cos(x * pi / 180)).quantize(Decimal('1.0000'))
                        for y in range(0, 91, 5)] for x in range(0, 91, 5)]
    return base_table_cosa


def find_degree(value_cosa):  # Функция находит максимально схожее теоретическое значение с получившимся
    # и выдаёт предполагаемые значения углов по осям X и Y
    if value_cosa == 0:
        result_x = 'батарея солнечная в тени'
        result_y = 'батарея солнечная в тени'
        return result_x, result_y
    else:
        base_cos = generation_table()
        min_diff = 0.01
        result_x = []
        result_y = []
        for x in range(0, 19):
            for y in range(0, 19):
                if abs(value_cosa - float(base_cos[x][y])) <= min_diff:
                    min_diff = abs(value_cosa - float(base_cos[x][y]))
                    result_y.append(x * 5)
                    result_x.append(y * 5)
        return result_x[-1], result_y[-1]


print(find_degree(0.136))
print(find_degree(0.520))

# Если брать по 5 градусов кратность, то он находит нормаьно (последние два числа в каждом списке нужные), когда беру по одному, он начинает мозги ебать сильно