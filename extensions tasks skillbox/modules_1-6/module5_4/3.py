
if __name__ == '__main__':

    text = input("Введите текст: ")
    low_lett = len([sym for sym in text if sym.islower()])
    up_lett = len([sym for sym in text if sym.isupper()])

    if up_lett > low_lett:
        print(text.upper())
    else:
        print(text.lower())


