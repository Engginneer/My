dogs_num = int(input("Введите количество собак: "))
list_of_points = []

for i in range(dogs_num):
    score_dog = int(input(f'Введите количество очков у {i + 1}-ой собаки: '))
    list_of_points.append(score_dog)
print(list_of_points)

maximum = list_of_points[0]
minimum = list_of_points[0]
for i in list_of_points:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

new_list = []
for i in list_of_points:
    if i == maximum:
        new_list.append(minimum)
    elif i == minimum:
        new_list.append(maximum)
    else:
        new_list.append(i)
print(new_list)
