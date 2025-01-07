list_name = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
new_list = []

for i, name in enumerate(list_name):
    if i % 2 == 0:
        new_list.append(name)

print(new_list)
