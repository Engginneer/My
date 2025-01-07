import os

def find_file(cur_path, file_name):
    # print("Запуск поиска в папке", os.path.join(os.path.abspath(cur_path)))
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        # print("Проверяется путь", path)
        if file_name == i_elem:
            print(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result

find_file('..', '1.py')