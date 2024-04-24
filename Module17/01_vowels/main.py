

if __name__ == '__main__':
    vowel_letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я',]

    text = input('Введите Ваш текст: ')
    new_list = []
    for sym in text:
        if sym in vowel_letters:
            new_list.append(sym)

    print(f'Длина списка: {len(new_list)}')
    print(new_list)

