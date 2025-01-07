
if __name__ == '__main__':

    # text_complited = input('Введите текст поздравления с конструкциями {name} и {age}: ')
    # name_list = input('Введите ФИО именинников через запятую: ').split(", ")
    # age_list = input('Введите возраст именинников через запятую: ').split(', ')

    text_complited = 'Привет, {name}, тебе уже целых {age} лет!'
    name_list = ["Виктор", "Наталья", "Степан"]
    age_list = ["30", "29", "0.5"]
    print(name_list)

    for i in range(len(name_list)):
        print(text_complited.format(name=name_list[i], age=age_list[i]))

    new_list = []
    for i in range(len(name_list)):
        new_list.append(' '.join([name_list[i], age_list[i]]))
    new_list = ' ,'.join(new_list)
    print(f'\n{new_list}')

