guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


def main():
    print(f'Сейчас гостей {len(guests)}: {guests}')
    name_guest = ''
    question = input('Гость пришел или ушел? ')
    if question == 'пришел' or question == 'пришёл':
        if len(guests) > 5:
            print("На даче нет мест для гостей", end='\n')
            main()
        else:
            name_guest = input('Имя гостя? ')
            guests.append(name_guest)
            main()
    elif question == 'ушел' or question == 'ушёл':
        name_guest = input('Имя гостя? ')
        guests.remove(name_guest)
        main()
    else:
        print("Такой команды нет, попробуйте снова", end='\n')


main()
