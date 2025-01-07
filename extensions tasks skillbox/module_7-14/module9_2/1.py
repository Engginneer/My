import os

path_to = input('Путь: ')

if not os.path.exists(path_to):
    print('Указанного пути не существует')
else:
    if os.path.isdir(path_to):
        print(f'{path_to} - является директорией')
        print(f'Размер директория: {os.path.getsize(path_to)} байт')
    elif os.path.isfile(path_to):
        print(f'{path_to} - является файлом')
        print(f'Размер файла: {os.path.getsize(path_to)} байт')
    elif os.path.islink(path_to):
        print(f'{path_to} - является ссылкой')
        print(f'Размер файла: {os.path.getsize(path_to)} байт')


