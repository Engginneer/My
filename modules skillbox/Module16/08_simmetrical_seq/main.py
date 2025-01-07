quantity = int(input("Введите количество чисел: "))
list_nums = []

for i in range(quantity):
    num = int(input('Введите первое число: '))
    list_nums.append(num)

temp_list = list_nums.copy()

print(f'Последовательность: {list_nums}')
quantity_add = 0

for i in range(len(list_nums)):
    if temp_list[i::1] == temp_list[len(temp_list) - 1::-1] and i == 0:
        print('Число симметрично')
        break
    if temp_list[::1] == temp_list[len(temp_list) - 1::-1]:
        print(f'Для симметрии необходимо добавить {quantity_add} число(сел)')
        for num in range(quantity_add - 1, -1, -1):
            list_nums.append(list_nums[num])
        print(f'Число после приведения его к симметричному виду: {list_nums}')
        break
    else:
        temp_list.pop(0)
        quantity_add += 1



