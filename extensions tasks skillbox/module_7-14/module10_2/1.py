BRUCE_WILLIS = 42
input_data = input('Введите строку: ')

try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError as error:
    print(f'Значение {type(error)} не является цифрой')
except IndexError:
    print('В указанной строчке нет пятого символа')
except Exception:
    print('Что-то пошло не так')

