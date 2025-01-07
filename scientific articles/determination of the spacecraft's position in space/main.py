from random import randint, uniform
from pandas import read_excel


def unpacking_tmi_iu(name_file: str):  # функция распаковывает телеметрию из txt и находит мощность
    current_list = []
    voltage_list = []
    cosa_list = []
    with open(name_file, 'r', encoding='utf8') as data_TMI:  # Распаковываем телеметрию СЭП
        # считаем значения мощности по каждой точке, после чего находим значение cosa
        for i in data_TMI:
            current_list.append(round(float(i.split(' ')[0]) / 1000, 4))
            voltage_list.append(round(float(i.split(' ')[1]), 4))
        for i in range(len(current_list)):
            cosa_list.append(round(find_cosa(current_list[i], voltage_list[i]), 4))


def find_cosa(curr, volt) -> float:  # Функция находит значение cosa
    # (где а - угол между нормалью к БС и направлением на Солнце)
    power_fact = 0.09  # Фактическая мощность имеющейся БФ(константа, известна на стадии изготовления)
    power_moment = curr * volt
    cosa = power_moment / power_fact
    return cosa


def find_degree(power):  # Функция находит максимально схожее теоретическое значение с получившимся
    # и выдаёт предполагаемые значения углов по осям X и Y
    base_cos = read_excel('base_cos.xlsx')
    min_diff = 1
    result_x = 0
    result_y = 0
    for x in range(0, 91, 5):
        for y in range(1, 19):
            if abs(power - base_cos[x][y]) < min_diff:
                min_diff = abs(power - base_cos[x][y])
                result_y = x
                result_x = y * 5
    return result_x, result_y


if __name__ == '__main__':
    main_system = False  # Имитация отказа основной системы

    if main_system == False:
        print(1)

# Нужно написать функцию для распаковки ТМИ, где уже есть мощность
# Написать функцию, которая случайно рисует синтезированные данные по мощности
# запустить код на синтезированных данных
# изобразить график, где будет две кривые, одна X, вторая Y, в зависимости от мощности или времени, надо подумать