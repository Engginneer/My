from random import randint, uniform
from pandas import read_excel
from math import pi, cos


def generation_table():
    base_table_cosa = [[round(cos(y * pi / 180) * cos(x * pi / 180), 3)
                       if round(cos(y * pi / 180) * cos(x * pi / 180), 3) > 0 else 0 for y in range(0, 181)]
                       for x in range(0, 181)]
    return base_table_cosa


def synthetic_data(power: float, voltage: float):
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
            power_list.append(round(float(i.split('\n')[0]), 4))
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
    power_fact = 0.09  # Фактическая мощность имеющейся БФ(константа, известна на стадии изготовления)
    if volt_or_none == None:
        cosa = curr_or_pow / power_fact
    else:
        power_moment = curr_or_pow * volt_or_none
        cosa = power_moment / power_fact
    if cosa > 1:
        cosa = 1
    return round(cosa, 3)


def find_degree(value_cosa, start_x, start_y):  # Функция находит максимально схожее
    # теоретическое значение с получившимся
    # и выдаёт предполагаемые значения углов по осям X и Y
    target_diff = 0.9
    base_cos = generation_table()
    if value_cosa == 0:
        result_x = 'батарея солнечная в тени'
        result_y = 'батарея солнечная в тени'
        return result_x, result_y
    else:
        min_diff = 1
        count = 0
        while min_diff < target_diff or count < 2:
            count += 1
            result_x = 0
            result_y = 0
            for x in range(start_x - count, start_x + count + 1):
                for y in range(start_y - count, start_y + count + 1):
                    if abs(value_cosa - base_cos[x][y]) <= min_diff:
                        min_diff = abs(value_cosa - base_cos[x][y])
                        result_y = x
                        result_x = y
        return result_x, result_y


if __name__ == '__main__':
    main_system = False  # Имитация отказа основной системы
    cosa_list = list()
    x_cord_list = list()
    y_cord_list = list()
    start_x = 0
    start_y = 0
    if main_system == False:
        TMI = unpacking_tmi_iu('TMI2.txt')
        for i in range(len(TMI[0])):
            cosa_list.append(find_cosa(TMI[0][i], TMI[1][i]))
        print(cosa_list)
        for i in range(len(TMI[0])):
            if i == 0:
                x_cord, y_cord = find_degree(cosa_list[i], start_x, start_y)
                x_cord_list.append(x_cord)
                y_cord_list.append(y_cord)
            else:
                x_cord, y_cord = find_degree(cosa_list[i], x_cord_list[i - 1], y_cord_list[i - 1])
                x_cord_list.append(x_cord)
                y_cord_list.append(y_cord)
        for i in range(len(x_cord_list)):
            print(f'отрезок времени - {i}, значение cosa - {cosa_list[i]}, угол по оси "Х"- {x_cord_list[i]} градусов,'
                  f' угол по оси "Y" - {y_cord_list[i]} градусов')
