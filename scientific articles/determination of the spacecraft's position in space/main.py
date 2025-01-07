from random import randint, uniform


def find_cos(curr, volt) -> float:
    power_fact = 0.09  # Фактическая мощность имеющейся БФ (константа, известна на стадии изготовления)
    power_moment = curr * volt
    cosa = power_moment / power_fact
    return cosa


if __name__ == '__main__':
    main_system = False  # Имитация отказа основной системы

    if main_system == False:
        Current = []
        Voltage = []
        with open('data.txt', 'r', encoding='utf8') as data_TMI:  # Распаковываем телеметрию СЭП
            for i in data_TMI:
                Current.append(float(i.split(' ')[0]))
                Voltage.append(float(i.split(' ')[1]))
            print(Current)
            print(Voltage)
