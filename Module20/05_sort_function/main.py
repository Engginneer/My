def sorted_int(num_list: iter) -> iter:
    for i in num_list:
        if i % 1 != 0:
            return num_list

    temp_list = list(num_list)

    flag = True
    while flag:
        flag = False
        for index, value in enumerate(temp_list):
            if index != len(temp_list) - 1 and value > temp_list[index + 1]:
                flag = True
                temp_list[index], temp_list[index + 1] = temp_list[index + 1], temp_list[index]

    return tuple(temp_list)


print(sorted_int((6, 3, -1, 8, 4, 10, -5)))

# Короче у меня тут несколько вопросов:
# 1. Я сначала сделал проверку на флоат вот так:
# if float in object:
#   return object
# Но такое не сработало, почему и как-то можно по другому сделать или мой вариант пойдет??
# 2. Я тут сделал метод пузырька, его тут достаточно(я в курсе, что есть быстрее, но там через рекурсии и тд)?
# или можнт вообще надо было сортер ебануть без приколов? не совсем задание понял


#  по вопросам:
#  первый - проверку на флоат делаешь либо так - да, либо проверяешь принадлежность объекта типу
#  через isinstance(num, float) ответ будет true ли false соответственно, я проверку делал так:

# if True not in [isinstance(x, float) for x in src_lst]:
#         src_lst.sort()

# проверка прикольная)))

# через лист компрехишнс, как ты любишь, хотя было разумнее проверить на инт и избавиться от not, и ещё ошибки
#  не было бы, если бы кто то закинул туда буквы
#  второй - пузырек норм, так же можешь использовать метода списка sort: temp_list.sort()

