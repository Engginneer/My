def unpacking_tmi_iu(name_file: str):  # функция распаковывает телеметрию, в которой ток и напряжение
    current_list = []
    voltage_list = []
    DT_X = []
    DT_Y = []
    with open(name_file, 'r', encoding='utf8') as data_TMI:
        for i in data_TMI:
            current_list.append(round(float(i.split(' ')[0]) / 1000, 4))
            voltage_list.append(round(float(i.split(' ')[1]), 4))
            DT_X.append(round(float(i.split(' ')[2]), 4))
            DT_Y.append(round(float(i.split(' ')[3]), 4))
    return current_list, voltage_list, DT_X, DT_Y
