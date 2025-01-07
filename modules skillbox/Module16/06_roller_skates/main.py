def operation_foot_and_skates(x: list, y: list) -> int:
    global count
    count = 0
    if len(x) > len(y):
        for i, skates in enumerate(x):
            for ind, foot in enumerate(y):
                if skates == foot:
                    count += 1
                    x.pop(i)
                    y.pop(ind)
                    break
        return count
    else:
        for ind, foot in enumerate(y):
            for i, skates in enumerate(x):
                if skates == foot:
                    count += 1
                    x.pop(i)
                    y.pop(ind)
                    break
    return count


list_skates = []
list_foot = []


size_list_skates = int(input("Введите количество коньков: "))
for i in range(size_list_skates):
    x = int(input(f'Размер {i + 1} пары: '))
    list_skates.append(x)

size_list_foot = int(input("Введите количество людей: "))
for i in range(size_list_foot):
    x = int(input(f'Размер ноги {i + 1} человека: '))
    list_foot.append(x)

operation_foot_and_skates(list_foot, list_skates)

print(f'Наибольшее кол-во людей, которые могут взять ролики: {count}')
