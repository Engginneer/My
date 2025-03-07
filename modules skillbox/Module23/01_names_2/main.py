summ_total = 0
errors_list = []
with open('people.txt', 'r', encoding='utf8') as people:
    for i_line in people:
        try:
            if len(i_line) < 4:
                raise ValueError(f'Ошибка длины в строке {i_line}')
            else:
                summ_total += len(i_line) - 1
        except ValueError as exp:
            print(exp)
            errors_list.append(f'Возникла ошибка в строке {i_line}')

str_to_log = '\n'.join(errors_list)

with open('errors.log', 'w', encoding='utf8') as errors_log:
    if str_to_log:
        errors_log.write(str_to_log)
        print(f'список ошибок: \n{str_to_log}') # TODO тут работает как то некорректно вывод

print(f'Общее количество символов: {summ_total}')
