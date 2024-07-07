
from random import randint

list_rand = [randint(0, 10) for i in range(10)]

# 1 вариант решения _____________________________________________________________________
# new_list = []
#
# for index, value in enumerate(list_rand):
#     if index == 0 or index % 2 == 0: # TODO проверка на ноль тут не нужна
#         temp = (value, list_rand[index + 1])
#         new_list.append(temp)
#________________________________________________________________________________________

# 2 вариант решения______________________________________________________________________

new_list = [(list_rand[i], list_rand[i + 1]) for i in range(len(list_rand)) if i == 0 or i % 2 == 0]  #TODO здесь можно избавиться от условий указав шаг range(0, len(...), 2)

# _______________________________________________________________________________________

print(list_rand)
print(new_list)

