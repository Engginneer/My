import os


def find_path_to_file(dir_name, file_name):
    for elem in os.listdir(dir_name):
        path = os.path.join(dir_name, elem)
        if elem == file_name:
            print(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_path_to_file(path, file_name)
            if result:
                break
    else:
        result = None
    return result


name_file = input('Введите имя файла: ')

find_path_to_file(os.path.join('..', '..'), name_file)
