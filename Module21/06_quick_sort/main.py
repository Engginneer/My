def one_to_three(list_input: list):
    left_list = []
    midl_list = []
    right_list = []
    basic_elem = list_input[len(list_input) - 1]
    for i in list_input:
        if i < basic_elem:
            left_list.append(i)
        elif i == basic_elem:
            midl_list.append(i)
        elif i > basic_elem:
            right_list.append(i)
    return left_list, midl_list, right_list


def fast_sort(list_inp: list):
    result_list = []
    left_list, midl_list, right_list = one_to_three(list_inp)
    if left_list:
        result_list += fast_sort(left_list)
    if midl_list:
        for index in midl_list:
            result_list.append(index)
    if right_list:
        result_list += fast_sort(right_list)
    return result_list


example_list = [5, 8, 9, 4, 2, 9, 1, 8]
print(fast_sort(example_list))

