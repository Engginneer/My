def triangle(list_inp: str):
    list_normal = list_inp.split(' ')
    num = list_normal[0]
    count = 0
    result = ''
    for i in list_normal:
        if i == num:
            count += 1
    if count == 1:
        result = 'Обычный'
    elif count == 2:
        result = 'Равнобедренный'
    elif count == 3:
        result = 'Равносторонний'
    return result



len_triangle = input("Введите стороны: ")
print(triangle(len_triangle))
