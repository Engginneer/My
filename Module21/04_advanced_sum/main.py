
def custom_sum(obj: list):
    sum_out = 0
    for index in obj:
        if isinstance(index, (int, float)):
            sum_out += index
        elif isinstance(index, (list, tuple, set)):
            sum_out += custom_sum(index)
    return sum_out


num_lst = [[1, 2, [3]], [1, 5, (15, 0), 'hi'], 3, '18']
print(custom_sum(num_lst))

# TODO я тут маленько исходный словарь поправил, и оно чета не работает)
