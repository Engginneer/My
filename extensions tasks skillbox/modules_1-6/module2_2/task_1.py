nums_list = []
num_in_list = int(input('Кол-во чисел в списке: '))

for _ in range(num_in_list):
    num = int(input('Очередное число: '))
    nums_list.append(num)
maximum = nums_list[0]
minimum = nums_list[0]

for i in nums_list:
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i

print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)
