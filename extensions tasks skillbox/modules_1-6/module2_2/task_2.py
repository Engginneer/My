quantity = int(input("Введите количество элементов в списке: "))
divider = int(input("Введите делитель: "))
list_num = []
summ_i = 0

for i in range(quantity):
    number = int(input(f'Введите {i + 1} число в списке: '))
    list_num.append(number)

print(list_num)
for num in range(quantity):
    if list_num[num] % divider == 0:
        summ_i += num
        print(f'Индекс числа {list_num[num]} = {num}')

print(f'Сумма индексов: {summ_i}')
