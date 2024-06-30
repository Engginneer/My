from collections import defaultdict

str_inp = input("Введите строку: ")

dict_str = defaultdict(int)

for char in str_inp:
    dict_str[char] += 1

poly = 2

for values in dict_str.values():
    if values % 2 == 1:
        poly -= 1
        if poly == 0:
            print('Палиндром не получается')
            break

else:
    print('Можно сделать палиндром')
print(dict_str)


