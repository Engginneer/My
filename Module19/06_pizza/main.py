from collections import defaultdict
from pprint import pprint

order_quantity = int(input('Введите количество заказов: '))

dict_all_order = dict()
dict_all_order_time = dict()

for i in range(order_quantity):
    time_order = input(f'Введите {i + 1}-ый заказ в формате "Фамилия Название-пиццы количество": ').split(' ')
    dict_all_order_time[i] = time_order

for key, items in dict_all_order_time.items():
    if items[0] not in dict_all_order.keys():
        dict_all_order[items[0]] = {items[1]: int(items[2])}
    else:
        if items[1] not in dict_all_order[items[0]].keys():
            dict_all_order[items[0]][items[1]] = int(items[2])
        else:
            dict_all_order[items[0]][items[1]] += int(items[2])

pprint(dict_all_order)  # Можно сделать красивый вывод, как просят, но мне и "ппринт" нравится
