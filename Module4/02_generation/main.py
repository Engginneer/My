

if __name__ == '__main__':

    list_lenght = int(input('Введите длину списка: '))

    new_list = [1 if i % 2 == 0 else i % 5 for i in range(list_lenght)]
    print(new_list)