from pprint import pprint
from collections import defaultdict

text = input('Введите текст: ').lower()
count_hist = dict()
for char in text:
    if char not in count_hist:
        count_hist[char] = 1
    else:
        count_hist[char] += 1

pprint(count_hist)

set_values = set(count_hist.values())
inv_count_hist = {}
temp_list = []

print(set_values)
for i in set_values:
    temp_list = []
    for key in count_hist.keys():
        if i == count_hist[key]:
            temp_list.append(key)
    inv_count_hist[i] = temp_list

print()

for key, value in inv_count_hist.items():
    print(f'{key} : {value}')







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




