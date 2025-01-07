from random import randint

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

nums_1_2 = set(nums_1)
nums_2_2 = set(nums_2)

print(f'Первое множество: {nums_1_2}')
print(f'Второе множество: {nums_2_2}')

print(f'Минимальное число из 1-го множества: {min(nums_1_2)}')
print(f'Минимальное число из 2-го множества: {min(nums_2_2)}')

nums_1_2.discard(min(nums_1_2))
nums_2_2.discard(min(nums_2_2))

nums_1_3 = set(nums_1_2)
nums_2_3 = set(nums_2_2)

nums_1_3.add(randint(100, 200))
nums_2_3.add(randint(100, 200))

print(f'Случайное число для 1-го множества: {nums_1_3.difference(nums_1_2)}')
print(f'Случайное число для 1-го множества: {nums_2_3.difference(nums_2_2)}')

print(f'Объединение множеств: {nums_1_3.union(nums_2_3)}')
print(f'Пересечение множеств: {nums_1_3.intersection(nums_2_3)}')
print(f'Элементы, входящие в 2-е множество, но не входящие в 1-е: {nums_2_3.difference(nums_1_3)}')



