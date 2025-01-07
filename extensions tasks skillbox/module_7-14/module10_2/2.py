alphabet = 'abcdefghijklmnopqrstuvwxyz'
file_result = None
file_ages = None
try:
    file_ages = open('ages.txt', 'r', encoding='utf8')
    file_result = open('result.txt', 'x', encoding='utf8')
except (IndentationError, IsADirectoryError, FileExistsError) as error_is:
    print(f'Поймано исключение: {error_is}')

if file_result and file_ages:
    try:
        for i, i_line in enumerate(file_ages):
            int(i_line)
            file_result.write(f'{i_line.split('\n')[0]} - {alphabet[i]}' + '\n')
    except (ValueError, TypeError) as error_type:
        print(f'Словили ошибку {error_type}')
file_result.close()
file_ages.close()
