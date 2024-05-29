
if __name__ == '__main__':
    text = input('Введите название файла: ')
    start_sym_not = '@№$%^&*()'
    sym_start = False

    for sym in start_sym_not:
        if text.startswith(sym):
            sym_start = True
            break

    if sym_start:
        print('Название начинается на один из специальных символов.')
    elif text.endswith('.txt') or text.endswith('.dox'):
        print("it's okay")
    else:
        print('неверное расширение файла. Ожидалось .txt или .docx.')





