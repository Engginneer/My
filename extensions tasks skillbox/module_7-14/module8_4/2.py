def num_in_list(num, lst=None):
    lst = lst or []
    if not lst:
        lst = []
    lst.append(num)
    print(lst)




num_in_list(5)
num_in_list(10)
num_in_list(15)
