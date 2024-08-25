name_user = input('Введите имя пользователя: ')

with open('chat.txt', 'a', encoding='utf8') as chat:
    while True:
        menu_item = int(input('\n1. Просмотреть текущий чат\n2. Отправить сообщение\n'
                              '3. Завершить сессию\n'))
        if menu_item == 1:
            chat.close() # TODO Как же отвратительно это выглядит, а главное после первого чтения
                         #  программа перестанет работать
            with open('chat.txt', 'r', encoding='utf8') as chat_temp:
                for i_elem in chat_temp:
                    temp_list = i_elem.split(' ')
                    if temp_list[0] == name_user + ':':
                        temp_list[0] = 'Вы:'
                        print(' '.join(temp_list), end='')
                    else:
                        print(i_elem, end='')
            chat_temp.close()

        elif menu_item == 2:
            massage = input()
            chat.write(name_user + ': ' + massage + '\n')
        elif menu_item == 3:
            break
        else:
            print('Некорректный ввод пункта меню')
