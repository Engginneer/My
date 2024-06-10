
def check_pass():

    password = input('Введите пароль: ')

    if len(password) < 8:
        print('Пароль ненадежный! Придумайте новый!')
        check_pass()

    top_sym = True
    for sym in password:
        if sym.isupper():
            top_sym = False
            break
    if top_sym:
        print('Пароль ненадежный! Придумайте новый!')
        check_pass()

    int_quantity = 0

    for sym in password:
        if sym.isdigit():
            int_quantity += 1
            if int_quantity > 2:
                break
    else:
        print('Пароль ненадежный! Придумайте новый!')
        check_pass()

    print('Пароль надежный!')




check_pass()


