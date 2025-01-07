violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
time_songs = 0
quantity = int(input("Сколько песен выбрать? "))
for i in range(quantity):
    name = input(f"Введите название {i + 1} песни: ")
    for ind, song in enumerate(violator_songs):
        if violator_songs[ind][0] == name:
            time_songs += violator_songs[ind][1]
            break

print(f'Общее время звучания песен: {time_songs}')
