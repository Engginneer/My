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

    # plt.xlabel('x - time')
    # plt.ylabel('y - x_cord, y_cord')
    #
    # plt.plot(time, x, label="line 1")
    # plt.plot(time, y, label="line 1")



    fig, ax1 = plt.subplots()

    color = 'tab:orange'
    ax1.set_xlabel('time')
    ax1.set_ylabel('x_cord, y_cord', color=color)
    ax1.plot(time, x, color=color)
    ax1.plot(time, y, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:cyan'
    ax2.set_ylabel('cosa, PБФ', color=color)
    ax2.plot(time, cosa, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.show()

time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 'батарея солнечная в тени']
y = [0, 14, 21, 33, 49, 66, 78, 86, 90, 'батарея солнечная в тени']
cos_a = [1, 0.962, 0.929, 0.83, 0.656, 0.404, 0.202, 0.061, 0.006, 0.0]

drawing_a_graph(time, x, y, cos_a)
