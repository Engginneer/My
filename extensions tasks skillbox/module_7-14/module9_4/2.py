import os
from random import randint


def find_file(cur_path):
    # print("Запуск поиска в папке", os.path.join(os.path.abspath(cur_path)))
    list_path_in = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isfile(path):
            temp_file = open(path, 'r', encoding='utf8')
            for i_line in temp_file:
                list_path_in.append(i_line)
            list_path_in.append('*' * 40)
        elif os.path.isdir(path):
            list_path_in += (find_file(path))

    return list_path_in


list_path = find_file('..')

for i in list_path:
    if i == '*' * 40:
        print()
    print(i, end='')
    if i == '*' * 40:
        print()
