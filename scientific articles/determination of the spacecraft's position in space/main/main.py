from unpacking_tmi_iu import unpacking_tmi_iu
from find_cosa import find_cosa
from find_degree import find_degree
from drawing_a_graph import drawing_a_graph

if __name__ == '__main__':
    main_system = False  # Имитация отказа основной системы
    cosa_list = list()
    x_cord_list = list()
    y_cord_list = list()
    DT_X_list = list()
    DT_Y_list = list()
    start_x = 0
    start_y = 0
    if main_system == False:
        TMI = unpacking_tmi_iu('TMI2.txt') # распаковываем телеметрию
        for i in range(len(TMI[0])):
            cosa_list.append(find_cosa(TMI[0][i], TMI[1][i]))
            DT_X_list.append(TMI[2][i])
            DT_Y_list.append(TMI[3][i])

        for i in range(len(TMI[0])):
            if i == 0:
                x_cord, y_cord = find_degree(cosa_list[i], start_x, start_y, DT_X_list[i], DT_Y_list[i])
                x_cord_list.append(x_cord)
                y_cord_list.append(y_cord)
            else:
                x_cord, y_cord = find_degree(cosa_list[i], x_cord_list[i - 1], y_cord_list[i - 1],
                                             DT_X_list[i], DT_Y_list[i])
                x_cord_list.append(x_cord)
                y_cord_list.append(y_cord)
        for i in range(len(x_cord_list)):
            if cosa_list[i] <= 0:
                print(f'отрезок времени - {i} - батарея солнечная в тени')
            else:
                print(f'отрезок времени - {i}, значение cosa - {cosa_list[i]}, угол по оси "Х"- {x_cord_list[i]} '
                      f'градусов, угол по оси "Y" - {y_cord_list[i]} градусов')

    time_points = list(range(len(x_cord_list)))
    drawing_a_graph(time_points, x_cord_list, y_cord_list, cosa_list)

