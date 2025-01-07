def search(x: dict):
    num_series = input('Введите номер и серию паспорта через пробел: ').split(' ')
    for data_inside in x:
        if int(num_series[0]) in data_inside and int(num_series[1]) in data_inside:
            print(f'Фамилия: {x[data_inside][0]} \nИмя: {x[data_inside][1]}')




data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}


search(data)