from pprint import pprint

num = int(input('Введите целое число: '))

num_dict = dict()
for i in range(1, num + 1):
    num_dict[i] = i ** 2

pprint(num_dict)
