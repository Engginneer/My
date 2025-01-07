

all_films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
    'Город грехов', 'Мементо', 'Отступники', 'Деревня'
]
number_films = int(input('Введите количество фильмов: '))
search_counter = 0
like_list_films = []

while number_films != 0:
    film = input("Введите название фильма: ")
    if film in all_films:
        like_list_films.append(film)
        number_films -= 1
        print('Фильм добавлен в коллекцию "любимые"')
    else:
        print(f'Фильма {film} нет в нашей картотеке.')

print(f'Ваш список любимых фильмов: {like_list_films}')



