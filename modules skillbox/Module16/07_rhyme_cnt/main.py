quantity = int(input("Введите количество человек: "))
kick_num = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {kick_num}-й человек')
print()

players = list(range(1, quantity + 1))
loser = 0
point_start = 0


while len(players) != 1:
    print(f'Текущий круг людей: {players}')

    if loser < len(players) or loser > len(players):
        print(f'Начало счета с игрока с номером: {players[point_start]}')
    elif loser == len(players):
        print(f'Начало счета с игрока с номером: {players[0]}')

    if loser < len(players):
        point_start = loser
    elif loser >= len(players):
        point_start = 0

    loser = (kick_num % len(players)) - 1 + point_start

    print(f'Выбывает участник с номером {players[loser]} ')
    players.pop(loser)
    print()

print(f'Остался один участник, его номер: {players[0]}')


# ДАААААААААААААААААААААААААААААААААААААААААААА СДЕЛАЛ!!!!!!!!!???
