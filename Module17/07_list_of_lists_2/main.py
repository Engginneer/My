

if __name__ == '__main__':
    nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]



    new_list = [sym for list1 in nice_list for list2 in list1 for sym in list2]
    print(new_list)
