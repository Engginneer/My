def mobile_book():
    print(f'Текущие контакты на телефоне: {contact_dict}')
    name = input('Введите имя: ')
    if name in contact_dict:
        print('Ошибка, такое имя уже существует.')
        mobile_book()
    number = input('Введите номер телефона: ')
    contact_dict[name] = number
    mobile_book()


contact_dict = {}
mobile_book()
