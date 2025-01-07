
if __name__ == '__main__':
    menu_inp = input('Введите меню через символ ";": ').split(';')
    print("Сегодня у нас в меню: {}".format(', '.join(menu_inp)))