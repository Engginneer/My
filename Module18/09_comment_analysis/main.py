
def up_low_count(x: str):
    a = 0
    b = 0
    for sym in x:
        if sym.islower():
            a += 1
        elif sym.isupper():
            b += 1
    return a, b


if __name__ == '__main__':
    text = input('Введите текст: ')
    low_sym, up_sym = up_low_count(text)
    print(f'Количество заглавных букв: {up_sym}')
    print(f'Количество строчных букв: {low_sym}')

# ывавы