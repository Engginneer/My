from unpacking_tmi_iu import unpacking_tmi_iu
from find_cosa import find_cosa
from find_degree import find_degree

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
