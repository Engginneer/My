import matplotlib.pyplot as plt


def drawing_a_graph(time, x_cord, x_cord_1, y_cord, y_cord_1, cosa, cosa_1):
    x = list()
    for i in range(len(x_cord)):
        if isinstance(x_cord[i], str):
            x.append(None)
        else:
            x.append(x_cord[i])
    y = list()
    for i in range(len(y_cord)):
        if isinstance(y_cord[i], str):
            y.append(None)
        else:
            y.append(y_cord[i])

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Участок времени (номер измерения)')
    ax1.set_ylabel('Значение угла, °', color='olivedrab')





    ax1.plot(time, x, color='yellowgreen', marker=(5, 1), label='Расчетные значения угла по оси Х')
    ax1.plot(time, y, color='yellowgreen', marker=(9, 2), label='Расчетные значения угла по оси Y')
    ax1.plot(time, x_cord_1, color='olivedrab', marker=(5, 0), label='Эталонные значения угла по оси Х')
    ax1.plot(time, y_cord_1, color='olivedrab', marker=(4, 0), label='Эталонные значения угла по оси Y')



    ax1.tick_params(axis='y', labelcolor='olivedrab')
    plt.title('Сравнения результатов эксперимента с эталонными значениями', color='black')

    ax1.legend(loc='center left')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Значение cosa', color='purple')

    ax2.plot(time, cosa, color='violet', marker='o', label='Расчетное значение cosa')
    ax2.plot(time, cosa_1, color='purple', marker='v', label='Эталонное значение cosa')
    ax2.tick_params(axis='y', labelcolor='purple')


    plt.grid(color='black', linestyle='--')
    plt.legend(loc='center right')
    plt.show()


time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 'батарея солнечная в тени']
y = [0, 14, 21, 33, 49, 66, 78, 86, 90, 'батарея солнечная в тени']
cos_a = [1, 0.962, 0.929, 0.83, 0.656, 0.404, 0.202, 0.061, 0.006, 0.0]
cos_a1 = [1.0, 0.985, 0.94, 0.866, 0.766, 0.643, 0.5, 0.342, 0.174, 0.0]

x1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

drawing_a_graph(time, x, x1, y, y1, cos_a, cos_a1)
