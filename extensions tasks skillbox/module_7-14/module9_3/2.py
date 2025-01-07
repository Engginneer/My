import os
from random import randint


def find_file(cur_path, file_name):
    # print("Запуск поиска в папке", os.path.join(os.path.abspath(cur_path)))
    list_path_in = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        # print("Проверяется путь", path)
        if file_name == i_elem:
            list_path_in.append(os.path.abspath(path))
            # print(os.path.abspath(path))
        elif os.path.isdir(path):
            list_path_in += (find_file(path, file_name))

    return list_path_in


list_path = find_file('..', '1.py')

rand_num_file = randint(1, len(list_path) - 1)
rand_file = open(list_path[rand_num_file], 'r', encoding='utf8')

print(f'Случайным образом выбран файл: {list_path[rand_num_file]}')
for i_line in rand_file:
    print(i_line, end='')

