number_of_players = int(input("Введите количество участников: "))
numbers_of_team = int(input("Введите количество команд: "))
teams = []
count = 1
flag = True

for i in range(numbers_of_team - 1):
    if number_of_players % numbers_of_team == 0:
        temp = list(range(count, (count + number_of_players // numbers_of_team) + 1))
        count += numbers_of_team
        teams.append(temp)
    else:
        flag = False
if flag:
    print(teams)
else:
    print(f'{number_of_players} участников нельзя поделить на {numbers_of_team} команд(ы)')