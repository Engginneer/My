

if __name__ == '__main__':

    list_length = int(input('Введите длину списка: '))

    new_list = [1 if i % 2 == 0 else i % 5 for i in range(list_length)]
    print(new_list)