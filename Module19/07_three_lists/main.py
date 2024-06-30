array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# # 1 задача
answer_intersection = []
answer_dif = []

for i in array_1:
    if i in array_2 and i in array_3:
        answer_intersection.append(i)

print(sorted(answer_intersection))

for i in array_1:
    if i not in array_2 and i not in array_3:
        answer_dif.append(i)
print(sorted(answer_dif))



# 2 задача

# array_1_2 = set(array_1)
# array_2_2 = set(array_2)
# array_3_2 = set(array_3)
#
# answer_intersection = array_1_2 & array_2_2 & array_3_2
# answer_dif = array_1_2.difference(array_2_2).difference(array_3_2)
#
# print(sorted(answer_intersection))
# print(sorted(answer_dif))
