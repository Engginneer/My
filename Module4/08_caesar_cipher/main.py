def cesar_cod(x: str, y: int) -> str:
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    cod = [(alphabet[(alphabet.index(sym) + y)] if x[x.index(sym)] in alphabet else x[x.index(sym)])
           if x.index(sym) + y >= len(alphabet)
           else (alphabet[(alphabet.index(sym) + y - len(alphabet))]
           if x[x.index(sym)] in alphabet
           else x[x.index(sym)])
           for sym in x]

    cod_str = ''
    for i in cod:
        cod_str += i
    return cod_str


if __name__ == '__main__':

    text = input("Введите текст: ")
    shift = int(input("Введите сдвиг: "))

    new_text = cesar_cod(text, shift)
    print(f'Закодированное сообщение:  {new_text}')

