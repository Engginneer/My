def add_num() -> None:
    name = input('Введите имя и фамилию через пробел: ').split(' ')
    if (name[0], name[1]) in book_name:
        print(f'Человек с именем {name[0]} и фамилией {name[1]} уже есть в словаре!\n')
        name_in_book()
    else:
        num = input('Введите номер телефона: ')
        book_name[name[0], name[1]] = num
        name_in_book()


def find_num() -> None:
    name_for_find = input('Введите фамилию для поиска: ')
    for name_temp in book_name.keys():
        if name_for_find in name_temp:
            print(f'Вот нужный контакт: {name_temp} - {book_name[name_temp]}\n')
    name_in_book()


def name_in_book():
    menu = input('\nВыберите пункт меню: \n1. Показать имеющиеся номера \n2. Внести номер \n3. Найти контакт'
                 ' \n4. Закончить изменения \n')
    if menu == '1':
        print(book_name)
        name_in_book()
    elif menu == '2':
        add_num()
    elif menu == '3':
        find_num()
    elif menu == '4':
        quit()
    else:
        print('Такого пункта нет в меню, попробуйте еще раз!\n')
        name_in_book()


book_name = dict()
if __name__ == '__main__':
    name_in_book()

# TODO тут опять же написал структуру, зачем все попереименовывал не понимаю...
#  в след раз так не делай, я ж не просто так рисую, стараюсь тебе культуру названий переменных и функций привить,
#  время трачу, а ты потом просто удаляешь все, ну в целом норм теперь стало, по сравнению с первым вариантом,
#  но вот это так и осталось неинформативным "name_in_book"
