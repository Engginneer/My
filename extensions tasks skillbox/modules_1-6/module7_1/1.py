from random import randint

first_tuple = tuple([randint(0, 5) for char in range(10)])
second_tuple = tuple([randint(-5, 0) for i in range(10)])

print(first_tuple)
print(second_tuple)

third_tuple = first_tuple + second_tuple
print()
print(third_tuple)
print(f'Количество нулей в третьем кортеже: {third_tuple.count(0)}')
