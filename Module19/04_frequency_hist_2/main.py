from pprint import pprint
from collections import defaultdict

text = input('Введите текст: ').lower()
count_hist = dict()
for sym in text:
    if sym not in count_hist:
        count_hist[sym] = 1
    else:
        count_hist[sym] += 1

set_values = set(count_hist.values())
inv_count_hist = {}
time_list = []

for i in set_values:
    time_list = []
    for key, values in count_hist.items():
        if i == values:
            time_list.append(key)
    inv_count_hist[i] = time_list

print()

for key, value in inv_count_hist.items():
    print(f'{key} : {value}')


pprint(inv_count_hist)




# src = input('Введите текст: ').lower()
#
# for char in src:
#     syn_dict[char] += 1
#
#
# keys = syn_dict.keys()
# items = syn_dict.values()
# reverce_dict = list(zip(items, keys))
# pprint(reverce_dict)




