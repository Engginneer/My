def fake_zip(x, y):
    list_one = tuple(x)
    list_two = tuple(y)

    new_list = []
    for i in range(min(len(list_one), len(list_two))):
        new_list.append((list_one[i], list_two[i]))

    return tuple(new_list)

str_example = {'abcd': 23, 'sdfdsf': 23.5}
tuple_example = (10, 20, 30, 40)

print(fake_zip(str_example, tuple_example))




#
# str_example = 'abcd'
# tuple_example = (10, 20, 30, 40)
#
# new_tuple = zip(str_example, tuple_example)
#
# print(new_tuple)
