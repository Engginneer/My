def add_name_in_book():
    menu = input('Выберите пункт меню: \n1. Показать имеющиеся номера \n2. Внести номер \n3. Закончить изменения \n')
    if menu == '1':
        print(book_name)
        add_name_in_book()
    elif menu == '2':
        name = input('Введите имя и фамилию через пробел: ').split(' ')
        if name[0] in book_name and name[1] in book_name:
            print(f'Человек с именем {name[0]} и фамилией {name[1]} уже есть в словаре!')
            add_name_in_book()
        else:
            num = input('Введите номер телефона: ')
            book_name[name[0], name[1]] = num
            add_name_in_book()
    elif menu == '3':
        quit()
    else:
        print('Такого пункта нет в меню, попробуйте еще раз!')
        add_name_in_book()


book_name = dict()
add_name_in_book()
