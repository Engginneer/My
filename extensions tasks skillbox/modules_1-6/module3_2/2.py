first_message = input('Введите первое предложение: ')
second_message = input('Введите второе предложение: ')
count_first = first_message.count('!') + first_message.count('?')
count_second = second_message.count('!') + second_message.count('?')

if count_first > count_second:
    print(first_message + second_message)
elif count_first < count_second:
    print(second_message + first_message)
else:
    print('уппс...')