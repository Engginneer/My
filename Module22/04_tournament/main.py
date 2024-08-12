def sorted_true(list_people: list) -> list:
    flag = 1
    while flag != 0:
        flag = 0
        for i in range(len(list_people) - 1):
            temp_player_one = list_people[i].split(' ')
            temp_player_two = list_people[i + 1].split(' ')
            if int(temp_player_one[2]) < int(temp_player_two[2]):
                list_people[i], list_people[i + 1] = list_people[i + 1], list_people[i]
                flag = 1
    return list_people


file_1 = open('first_tour.txt', 'r', encoding='utf8')
file_2 = open('second_tour.txt', 'w', encoding='utf8')

final_list = []
ratio = file_1.read().split('\n')[0]
file_1.seek(0)
list_players = file_1.read().split('\n')[1:]

for player in list_players:
    temp_list = player.split(' ')
    if temp_list[2] > ratio:
        final_list.append(temp_list[1][0] + '. ' + temp_list[0] + ' ' + temp_list[2])
    print(final_list)

list_to_second_file = sorted_true(final_list)

file_2.write(str(len(list_to_second_file)) + '\n')
for num in range(len(list_to_second_file)):
    file_2.write(f'{num + 1}) {list_to_second_file[num]}\n')
