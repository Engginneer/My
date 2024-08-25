from random import randint

luck_or_end = True
red_sum = 777
with open('out_file.txt', 'a', encoding='utf8') as hist:
    while luck_or_end:
        number = int(input('Введите число: '))
        try:
            num_rand = randint(1, 13)
            if num_rand == 3:
                luck_or_end = False
                raise ValueError('Повезло так повезло! (нет)')
            else:
                hist.write(str(number) + '\n')
                red_sum -= number
                if red_sum <= 0:
                    luck_or_end = False
                    print('Вы успешно выполнили условия выхода из порочного цикла!')
        except ValueError as exp:
            print(exp)
            luck_or_end = False
