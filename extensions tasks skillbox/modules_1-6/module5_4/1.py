def cesar_cod(x: str, y: int) -> str:
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    cod = []
    for sym in x:
        if sym in alphabet:
            if alphabet.index(sym) + y < len(alphabet):
                inp_sym = alphabet.index(sym)
                out_sym = alphabet[inp_sym + y]
                cod.append(out_sym)
            else:
                inp_sym = alphabet.index(sym)
                out_sym = alphabet[inp_sym + y - len(alphabet)]
                cod.append(out_sym)
        else:
            cod.append(sym)


    cod_str = ''
    for i in cod:
        cod_str += i
    return cod_str


if __name__ == '__main__':

    text = input("Введите текст: ")
    text = text.lower()
    shift = int(input("Введите сдвиг: "))

    new_text = cesar_cod(text, shift)
    print(f'Закодированное сообщение:  {new_text}')
