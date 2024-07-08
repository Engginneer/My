
from random import randint

list_rand = [randint(0, 10) for i in range(10)]

# 1 вариант решения _____________________________________________________________________
# new_list = []
#
# for index, value in enumerate(list_rand):
#     if index % 2 == 0:
#         temp = (value, list_rand[index + 1])
#         new_list.append(temp)
#________________________________________________________________________________________

# 2 вариант решения______________________________________________________________________

new_list = [(list_rand[i], list_rand[i + 1]) for i in range(0, len(list_rand), 2)]

# _______________________________________________________________________________________

print(list_rand)
print(new_list)

