
ip_address = input('Введите ip-адрес: ')


for part in range(len(ip_address.split('.'))):
    if len(ip_address.split('.')) != 4:
        print('IP-адрес - это четыре числа, разделенные точками')
        quit()
    elif not 0 <= int(ip_address.split('.')[part]) <= 255:
        print(f'Число {ip_address.split('.')[part]} выходит за диапазон от 0 до 255')
        quit()
    elif True:
        for sym in range(len(ip_address.split('.')[part].split(''))):
            if str(ip_address.split('.')[part].split('')).isalpha():
                print(f'Число {ip_address.split('.')[part]} содержит в себе буквы')
                quit()
    elif int(ip_address.split('.')[part]) % 1 != 0:
        print(f'Число {ip_address.split('.')[part]} не является целым')
        quit()
    elif part == 3:
        print('IP-адрес корректен!')