# # Сначала без читов:
quantity = int(input("Введите количество символов в списке: "))
list_num = []

for i in range(quantity):
    list_num.append(int(input(f"Введите символ № {i + 1}: ")))
key = 1

while key != 0:
    key = 0
    for i, sym in enumerate(list_num):
        if i < len(list_num) - 1:
            if list_num[i] > list_num[i + 1]:
                list_num[i] = list_num[i + 1]
                list_num[i + 1] = sym
                key = 1

print(list_num)


# list_num = list(map(int, input(f'Введите значения через пробел: ').split(' ')))
# key = 1
# while key != 0:
#     key = 0
#     for i, sym in enumerate(list_num):
#         if i < len(list_num) - 1:
#             if list_num[i] > list_num[i + 1]:
#                 list_num[i] = list_num[i + 1]
#                 list_num[i + 1] = sym
#                 key = 1
#
# print(list_num)
