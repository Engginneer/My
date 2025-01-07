from random import randint, uniform
from pandas import read_excel


def find_cos(curr, volt) -> float:
    power_fact = 0.09  # Фактическая мощность имеющейся БФ
    # (константа, известна на стадии изготовления)
    power_moment = curr * volt
    cosa = power_moment / power_fact
    return cosa


if __name__ == '__main__':
    main_system = False  # Имитация отказа основной системы

    if main_system == False:
        Current_list = []
        Voltage_list = []
        cosa_list = []
        with open('data.txt', 'r', encoding='utf8') as data_TMI:  # Распаковываем телеметрию СЭП
            for i in data_TMI:
                Current_list.append(round(float(i.split(' ')[0])/1000, 4))
                Voltage_list.append(round(float(i.split(' ')[1]), 4))
            print(Current_list)
            print(Voltage_list)
            for i in range(len(Current_list)):
                cosa_list.append(round(find_cos(Current_list[i], Voltage_list[i]), 4))
            print(cosa_list)

        base_cos = read_excel('base_cos.xlsx')
        angle = 0.964
        for i in range(0, 91, 5):
            for i in base_cos[5]:
                # здесь нужно сравнивать косинус полученный с таблией и выбирать самый ближайший, чтобы определить угол.



