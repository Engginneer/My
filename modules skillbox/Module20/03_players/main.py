players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

new = []
for name, numbers in players.items():
    new.append(name + numbers)



# 1 вариант - ответ не такой, как просят
new1 = list(zip([i for i in players], [j for j in players.values()]))

# 2 вариант - ответ опять не такой
new2 = list(zip(players, players.values()))

# 3 вариант - угарно вышло, возможно тут есть что-то дельное)
new3 = list(zip([(name2 + numbers2) for name2, numbers2 in players.items()]))




print(new)
print(new1)
print(new2)
print(new3)
