from collections import defaultdict
from pprint import pprint

order_quantity = int(input('Введите количество заказов: '))

dict_all_order = dict()
dict_all_order_temp = dict()

for i in range(order_quantity):
    temp_order = input(f'Введите {i + 1}-ый заказ в формате "Фамилия Название-пиццы количество": ').split(' ')
    dict_all_order_temp[i] = temp_order

print(dict_all_order_temp)

for values in dict_all_order_temp.values():
    if values[0] not in dict_all_order.keys():
        dict_all_order[values[0]] = {values[1]: int(values[2])}
    else:
        if values[1] not in dict_all_order[values[0]].keys():
            dict_all_order[values[0]][values[1]] = int(values[2])
        else:
            dict_all_order[values[0]][values[1]] += int(values[2])

pprint(dict_all_order)  # Можно сделать красивый вывод, как просят, но мне и "ппринт" нравится



