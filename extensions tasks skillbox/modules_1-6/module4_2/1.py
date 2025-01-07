

if __name__ == '__main__':

    first_num = int(input('Введите левую границу: '))
    second_num = int(input('Введите правую границу: '))

    number_list = [i for i in range(first_num, second_num + 1) if i % 2 == 0]
    print(number_list)