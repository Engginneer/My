text = input('Введите текст программы: ')

for index, char in enumerate(text):
    if char == '~':
        print(index, end=' ')
