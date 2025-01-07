user_str = ''
file = None
try:
    user_str = input('Введите строку: ')
    file = open('str_user', 'w', encoding='utf8')
    file.write(str(user_str))
except ValueError as exp1:
    print(f'Нельзя преобразовать данные в целое: {exp1}')
except FileNotFoundError as exp2:
    print(f'Проблема с открытием файла: {exp2}')
except Exception as exp3:
    print(f'Что-то пошло не так...{exp3}')
else:
    print('Запись прошла без ошибок')
finally:
    if file and not file.closed:
        file.close()
