#
# def add_name_in_book():
#     menu = input('\nВыберите пункт меню: \n1. Показать имеющиеся номера \n2. Внести номер \n3. Найти контакт'
#                  ' \n4. Закончить изменения \n')
#     if menu == '1':
#         print(book_name)
#         add_name_in_book()
#     elif menu == '2':
#         name = input('Введите имя и фамилию через пробел: ').split(' ')
#         if (name[0], name[1]) in book_name:
#             print(f'Человек с именем {name[0]} и фамилией {name[1]} уже есть в словаре!\n')
#             add_name_in_book()
#         else:
#             num = input('Введите номер телефона: ')
#             book_name[name[0], name[1]] = num
#             add_name_in_book()
#     elif menu == '3':
#         name_for_find = input('Введите фамилию для поиска: ')
#         for name_temp in book_name.keys():
#             if name_for_find in name_temp:
#                 print(f'Вот нужный контакт: {name_temp} - {book_name[name_temp]}\n')
#
#
#         add_name_in_book()
#     elif menu == '4':
#         quit()
#     else:
#         print('Такого пункта нет в меню, попробуйте еще раз!\n')
#         add_name_in_book()
#
#
# book_name = dict()
# add_name_in_book()


# TODO сделай пж по архитектуре как я тебе передал:
def adder() -> None:
    ...


def finder() -> None:
    ...


phone_book = dict()
if __name__ == '__main__':
    ...
