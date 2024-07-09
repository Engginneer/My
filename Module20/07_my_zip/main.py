def zipper(first: iter, second: iter) -> tuple:
    list_one = tuple(first)
    list_two = tuple(second)

    new_list = []
    for i in range(min(len(list_one), len(list_two))):
        new_list.append((list_one[i], list_two[i]))

    return tuple(new_list)


first_data = 'asd'
secondary_data = (10, 20, 30, 40)

res = zip(first_data, secondary_data)
for itm in res:
    print(tuple(itm))

print('\n\n')

res1 = zipper(first_data, secondary_data)
for itm in res1:
    print(tuple(itm))
