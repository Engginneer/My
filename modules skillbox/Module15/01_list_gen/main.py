def the_odd_list(x: int):
    odd_list = []
    for i in range(1, x + 1):
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list


number = int(input("Введите число: "))
print(the_odd_list(number))
