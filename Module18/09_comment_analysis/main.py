
def up_low_count(x: str):  # TODO ъуъуъу
    a = 0
    b = 0
    for sym in range(len(x)):  # TODO тут вообще не нужны индексы, просто "for char in x"
        if x[sym].islower():
            a += 1
        elif x[sym].isupper():
            b += 1
    return a, b

if __name__ == '__main__':
    text = input('Введите текст: ')
    low_sym, up_sym = up_low_count(text)
    print(f'Количество заглавных букв: {up_sym}')
    print(f'Количество строчных букв: {low_sym}')
