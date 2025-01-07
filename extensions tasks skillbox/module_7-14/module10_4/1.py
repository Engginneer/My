
file = open('people.txt', 'r', encoding='utf8')
lenght_tot = 0
for i_line in file:
    if len(i_line) - 1 < 3:
        raise ValueError(f'В имени {i_line} менее 3-х букв')
    # except ValueError:
    #     print('Программа полетела...')

    lenght_tot += len(i_line)
    if '\n' in i_line:
        lenght_tot -= 1
print(f'Общая сумма имен: {lenght_tot}')
file.close()
