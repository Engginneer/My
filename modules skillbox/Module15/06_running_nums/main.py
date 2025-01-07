def shifting(x: list, y: int):
    new_list = []
    for i, sym in enumerate(x):
        new_list.append(x[i - y])
    return new_list


list_sym = input('Введите символы через пробел: ').split(' ')
shift = int(input('Введите значение сдвига: '))

print(f'Изначальный список: {list_sym}')
print(f'Список после сдвига: {shifting(list_sym, shift)}')
