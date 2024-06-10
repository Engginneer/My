
ip_address = input('Введите ip-адрес: ')

# TODO лучше так
# ip = list(input('Введите IP: ').split('.'))
# for part in ip:
# if...
# if...
# successes



for part in range(len(ip_address.split('.'))):
    if len(ip_address.split('.')) != 4:
        print('IP-адрес - это четыре числа, разделенные точками')
        quit()
    elif not ip_address.split('.')[part].isdigit():
        print(f'Число {ip_address.split('.')[part]} содержит в себе буквы')
        quit()
    elif int(ip_address.split('.')[part]) % 1 != 0:  # TODO разделитель дробной части - ".", соответственно у тебя дробная часть сразу отделится в следующую группу, а если поставить "," то и вовсе вылетит ошибка пр преобразовании в int
        print(f'Число {ip_address.split('.')[part]} не является целым')
        quit()
    elif not 0 <= int(ip_address.split('.')[part]) <= 255:
        print(f'Число {ip_address.split('.')[part]} выходит за диапазон от 0 до 255')
        quit()
    elif part == 3:
        print('IP-адрес корректен!')

# TODO у тебя эта задачка норм запускается? у меня ругается на строки внутри вставок в ф-строке ('.')
# TODO ваще необычное решение через квиты))
# TODO решение крайне мозговыносящее, ты хде его взял, как будто не ты писал, а опенаи))
# TODO поправь что бы запускалось, ну или отпиши что у тебя тут нет траблов....