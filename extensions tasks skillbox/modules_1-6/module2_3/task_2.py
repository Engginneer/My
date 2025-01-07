text = input('Введите текст: ')
sym_in_text = int(input('Введите номер символа: '))
sym_of_interest = list(text[sym_in_text - 1])
count_clones = 0

if list(text[sym_in_text - 2]) == sym_of_interest:
    count_clones += 1
if list(text[sym_in_text]) == sym_of_interest:
    count_clones += 1

print(f'Символ слева: {list(text[sym_in_text - 2])}')
print(f'Символ справа: {list(text[sym_in_text])}')
print(f'По соседству таких же символов - {count_clones}')