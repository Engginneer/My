import os


def information(path: str):
    count_dir = 0
    count_file = 0
    count_memory = 0
    if os.path.isfile(path):
        count_file += 1
        count_memory += os.path.getsize(path)
    elif os.path.isdir(path):
        for i_elem in os.listdir(path):
            temp_count_dir, temp_count_file, temp_count_memory = information(os.path.join(path, i_elem))
            count_dir += temp_count_dir
            count_file += temp_count_file
            count_memory += temp_count_memory
        count_dir += 1
    return count_dir, count_file, count_memory


path_in = input('Введите абсолютный путь: ')

quantity_dir, quantity_file, memory_total = information(path_in)
print(f'Размер каталога (в Кб): {round(memory_total / 1024, 2)}')
print(f'Количество подкаталогов: {quantity_dir}')
print(f'Количество файлов: {quantity_file}')
