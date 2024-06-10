

ip_address = input('Введите ip-адрес: ').split('.')

if len(ip_address) != 4:
    print('IP-адрес - это четыре числа, разделенные точками')
else:
    for part in ip_address:
        if not part.isdigit():
            print(f'Число {part} содержит в себе буквы или символы')
            break
        if not 0 <= int(part) <= 255:
            print(f'Число {part} выходит за диапазон от 0 до 255')
            break

    else:
        print('IP-адрес корректен!')

