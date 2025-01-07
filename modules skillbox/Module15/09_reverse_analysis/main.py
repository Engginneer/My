# TODO здесь писать код

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
print(f' Первоначальный список: {numbers_list}')

for i, itm in enumerate(numbers_list):
    if i < len(numbers_list) // 2:
        numbers_list[i] = numbers_list[-i - 1]
        numbers_list[-i - 1] = itm
print(f' Список после свича: {numbers_list}')

for i, itm in enumerate(numbers_list):
    if itm % 2 != 0:
        numbers_list.pop(i)


print(f' Список после чистки: {numbers_list}')


