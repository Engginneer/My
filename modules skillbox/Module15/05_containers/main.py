def assign_the_name(x: int):
    list_container = []
    for i in range(x):
        weight_cont = int(input(f'Введите вес {i + 1}-го контейнера: '))
        list_container.append(weight_cont)
    return list_container


def place_for_new_cont(list_cont: list, weight_new_cont: int):
    place = 0
    for i, sum in enumerate(list_cont):
        if list_cont[i] < weight_new_cont:
            place = i + 1
            break
    return place


quantity = int(input('Введите количество контейнеров: '))
list_containers = assign_the_name(quantity)
print()
new_cont = int(input('Введите вес нового контейнера: '))
print()
print(f'Номер, который получит новый контейнер: {place_for_new_cont(list_containers, new_cont)}')
