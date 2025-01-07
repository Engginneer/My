def process_on_like_list(x: list):
    print(f'Ваш текущий топ фильмов: {like_list}')
    film = input('Введите название фильма: ')
    if film not in films:
        print(f'Фильм {film} нет в нашей картотеке')
        process_on_like_list(films)
    print('Команды: добавить, вставить, удалить')
    comand = input('Введите команду: ')
    if comand == 'добавить':
        if film in like_list:
            print("Такой фильм уже есть в Вашем списке")
            print()
        else:
            like_list.append(film)
    elif comand == 'вставить':
        if film in like_list:
            print("Такой фильм уже есть в Вашем списке")
            print()
        else:
            new_place = int(input(f"На какую позицию вставить фильм {film}? "))
            like_list.insert(new_place - 1, film)
    elif comand == 'удалить':
        if film not in like_list:
            print("Такой фильм уже есть в Вашем списке")
            print()
        else:
            like_list.remove(film)
    else:
        print(f'Введите команду корректно')
    process_on_like_list(films)





films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]
like_list = []

process_on_like_list(films)
