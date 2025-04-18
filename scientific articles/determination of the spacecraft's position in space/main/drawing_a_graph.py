import matplotlib.pyplot as plt


def drawing_a_graph(time, x_cord, y_cord, cosa):
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



    ax1.tick_params(axis='y', labelcolor='olivedrab')
    plt.title('Сравнения результатов эксперимента с эталонными значениями', color='black')

    ax1.legend(loc='center left')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Значение cosa', color='purple')

    ax2.plot(time, cosa, color='violet', marker='o', label='Расчетное значение cosa')

    ax2.tick_params(axis='y', labelcolor='purple')


    plt.grid(color='black', linestyle='--')
    plt.legend(loc='center right')
    plt.show()