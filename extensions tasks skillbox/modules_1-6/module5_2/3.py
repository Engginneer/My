list_num = []

for i in range(4):
    x = input(f'Введите {i + 1}-е число:')
    list_num.append(x)

for i in range(4):
    if i != 3:
        print(f'{list_num[i]}', end='.')
    else:
        print(f'{list_num[i]}')
