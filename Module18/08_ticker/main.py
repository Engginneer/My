str_one = input('Введите первую строку: ')
str_two = input('Введите вторую строку: ')

if len(str_two) != len(str_one):
    print('Строки с разным количеством символов не могут быть одинаковыми.')
    quit()

for i in range(len(str_one)):
    str_time = str_one[1:len(str_one)] + str_one[0]
    if str_time == str_two:
        print(f'Первая строка получается из второй со сдвигом {i + 1}')
        quit()
    else:
        str_one = str_time
print('Первую строку нельзя получить из второй с помощью циклического сдвига.')



# absd - bsda - sdab - dabs - absd


#  TODO: Рассмотри ещё такой вариант, просто для паттернов, что ещё можно так сделать, и работать это будет попроще
# temp_str = str_one * 2
# for i in range(len(str_two)):
#     if temp_str[i: i + len(str_two)] == str_two:
#         print(f'Первая строка получается из второй со сдвигом {i}')
#         break
# else:
#     print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
#
