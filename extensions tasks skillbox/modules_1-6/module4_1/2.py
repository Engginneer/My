


if __name__ == '__main__':
    word = input("Введите строку: ")
    symbol = input('Введите дополнительный символ: ')

    first_list = [i * 2 for i in word]
    second_list = [sym + symbol for sym in first_list]

    print(f'Список удвоения: {first_list}')
    print(f'Список с дополнительным символом: {second_list}')
