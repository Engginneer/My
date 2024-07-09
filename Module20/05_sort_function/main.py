def sorted_int(num_list: iter) -> iter:
    for i in num_list:
        if i % 1 != 0:
            return num_list

    temp_list = list(num_list)

    flag = True
    while flag:
        flag = False
        for index, value in enumerate(temp_list):
            if index != len(temp_list) - 1 and value > temp_list[index + 1]:
                flag = True
                temp_list[index], temp_list[index + 1] = temp_list[index + 1], temp_list[index]

    return tuple(temp_list)


print(sorted_int((6, 3, -1, 8, 4, 10, -5)))
