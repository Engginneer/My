def func_read(name):
    with open('chat.txt', 'r', encoding='utf8') as chat_temp:
        for i_elem in chat_temp:
            temp_list = i_elem.split(' ')
            if temp_list[0] == name + ':':
                temp_list[0] = 'Вы:'
                print(' '.join(temp_list), end='')
            else:
                print(i_elem, end='')


def func_write(name_2):
    with open('chat.txt', 'a', encoding='utf8') as chat_temp:
        massage = input()
        chat_temp.write(name_2 + ': ' + massage + '\n')


name_user = input('Введите имя пользователя: ')

with open('chat.txt', 'a', encoding='utf8') as chat:
    while True:
        menu_item = int(input('\n1. Просмотреть текущий чат\n2. Отправить сообщение\n'
                              '3. Завершить сессию\n'))
        if menu_item == 1:
            func_read(name_user)
        elif menu_item == 2:
            func_write(name_user)
        elif menu_item == 3:
            break
        else:
            print('Некорректный ввод пункта меню')