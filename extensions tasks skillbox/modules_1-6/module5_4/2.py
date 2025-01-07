
if __name__ == '__main__':
    way = input('Введите путь к файлу: ')
    disk = input('На каком диске должен быть файл? ')
    end_name = input('Какое расширение у файла? ')

    if way.startswith(disk) and way.endswith(end_name):
        print('Путь к файлу корректен')
    else:
        print('Путь неверный!')