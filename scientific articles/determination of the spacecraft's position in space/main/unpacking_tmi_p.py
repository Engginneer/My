def unpacking_tmi_p(name_file: str):  # Функция распаковывает телеметрию, в которой сразу есть мощность
    power_list = []
    with open(name_file, 'r', encoding='utf8') as data_TMI:
        for i in data_TMI:
            power_list.append(round(float(i.split('\n')[0]), 4))
    return power_list
