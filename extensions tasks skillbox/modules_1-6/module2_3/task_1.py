str_list = input('Введите строку: ')
new_str_list = []
count_switch = 0

for i in str_list:
    if i == ':':
        count_switch += 1
        new_str_list.append(';')
    else:
        new_str_list.append(i)

print(f'Строка до изменения: {str_list}')
print(f'Строка после изменения:', end = ' ')
for i in new_str_list:
    print(i, end = '')
print(f'\nВсего изменений: {count_switch}')