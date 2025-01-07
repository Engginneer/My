from random import randint

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

list_one = [alphabet[randint(0, 32)] for char in range(10)]
list_two = [alphabet[randint(0, 32)] for char in range(10)]

dict_one = dict(enumerate(list_one))
dict_two = dict(enumerate(list_two))

print(list_one)
print(list_two)
print(dict_one)
print(dict_two)




