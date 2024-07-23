nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, (12, 13)], ['14', 15], [16, 17, 18]]]


def defolder(obj: list) -> list:
    new_list = []
    for i in obj:
        if isinstance(i, (int, float)):
            new_list.append(i)
        elif isinstance(i, (list, tuple, set)):
            for elem in defolder(i):
                new_list.append(elem)
    return new_list




if __name__ == '__main__':
    print(defolder(nice_list))
