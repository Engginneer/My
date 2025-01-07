file_1 = None
file_2 = None
try:
    file_1 = open('zen1.txt', 'r')
    temp_str = file_1.read()
    temp_list = temp_str.split('\n')

except FileNotFoundError as exp1:
    print(f'Файл {exp1} не найден!')
finally:
    if file_1:
        file_1.close()
        print(f'{file_1.closed}')
try:
    file_2 = open('zen_copy.txt', 'a')
    temp_list = temp_list[::-1]
    ans_str = '\n\n\n'
    for i_elem in temp_list:
        ans_str += i_elem
        ans_str += '\n'
    file_2.write(ans_str)
except (FileNotFoundError, ValueError):
    print('Файла нет, или он поврежден')
finally:
    if file_2:
        file_2.close()
        print(f'{file_2.closed}')
