
text = input('Введите текст: ')
text_set = set(text)

check_set = set('123456789')

print(check_set)
print(text_set)

print(f'Различные цифры строки: {text_set.intersection(check_set)}')
