violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

quantity_songs = int(input('Сколько песен хотите выбрать? '))
count_songs = 1
count_time = 0
while quantity_songs != 0:
    name = input(f'Введите название {count_songs}-ой песни: ')
    if name not in violator_songs:
        print('Такого трека нет в списке, введите другой')
    else:
        quantity_songs -= 1
        count_songs += 1
        count_time += violator_songs[name]

print(f'Общее время звучания {count_songs}-х песен: {round(count_time, 2)}')

#  СНачала делал через ФОР, потом передумал, с вайлом при отсутствии трека в списке проще возвращаться
# for i in range(quantity_songs):
#     name = input(f'Введите название {i}-ой песни: ')
#     if name not in violator_songs:
#         print('Такого трека нет в списке, введите другой')
