from random import randint


if __name__ == '__main__':
    first_group = [randint(50, 80) for i in range(10)]
    second_group = [randint(30, 60) for i in range(10)]

    print(first_group)
    print(second_group)
    list_survivors = ['Выжил' if first_group[i] + second_group[i] < 100
                      else 'Погиб' for i in range(10)]
    print(list_survivors)
