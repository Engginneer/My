from random import randint, uniform
from pandas import read_excel
from math import pi, cos


def generation_table():
    base_table_cosa = [[round(cos(y * pi / 180) * cos(x * pi / 180), 3) for y in range(0, 91)] for x in range(0, 91)]
    return base_table_cosa


def synthetic_data(power: int, voltage: float):
    value_pow = randint(0, 1000)
    random_step = round(uniform(-20, 20), 4)
    synthet_list = list()
    synthet_list.append(value_pow)
    for i in range(15):
        if value_pow + random_step > 0:
            value_pow = value_pow + random_step
            synthet_list.append(value_pow)
        else:
            synthet_list.append(0)
    return synthet_list


def unpacking_tmi_p(name_file: str):  # Функция распаковывает телеметрию, в которой сразу есть мощность
    power_list = []
    with open(name_file, 'r', encoding='utf8') as data_TMI:
        for i in data_TMI:
            power_list.append(round(float(i), 4))
    return power_list


def unpacking_tmi_iu(name_file: str):  # функция распаковывает телеметрию, в которой ток и напряжение
    current_list = []
    voltage_list = []
    with open(name_file, 'r', encoding='utf8') as data_TMI:
        for i in data_TMI:
            current_list.append(round(float(i.split(' ')[0]) / 1000, 4))
            voltage_list.append(round(float(i.split(' ')[1]), 4))
    return current_list, voltage_list


def find_cosa(curr_or_pow, volt_or_none=None) -> float:  # Функция находит значение cosa
    # (где а - угол между нормалью к БС и направлением на Солнце)
    power_fact = 1000  # Фактическая мощность имеющейся БФ(константа, известна на стадии изготовления)
    if volt_or_none == None:
        cosa = curr_or_pow / power_fact
    else:
        power_moment = curr_or_pow * volt_or_none
        cosa = power_moment / power_fact
    if cosa > 1:
        cosa = 1
    return round(cosa, 3)


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


if __name__ == '__main__':
    main_system = False  # Имитация отказа основной системы
    cosa_list = list()
    x_cord_list = list()
    y_cord_list = list()
    if main_system == False:
        TMI = synthetic_data(1000, 32)
        for i in TMI:
            cosa_list.append(find_cosa(i))
        for i in range(len(TMI)):
            x_cord, y_cord = find_degree(cosa_list[i])
            x_cord_list.append(x_cord)
            y_cord_list.append(y_cord)
        for i in range(len(x_cord_list)):
            print(f'отрезок времени - {i}, значение cosa - {cosa_list[i]}, угол по оси "Х"- {x_cord_list[i]} градусов,'
                  f' угол по оси "Y" - {y_cord_list[i]} градусов')

# Написать функцию, которая случайно рисует синтетические данные по мощности
# запустить код на синтетических данных
# изобразить график, где будет две кривые, одна X, вторая Y, в зависимости от мощности или времени, надо подумать
