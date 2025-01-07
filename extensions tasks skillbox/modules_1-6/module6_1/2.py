info = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки):').split(' ')

info_dict = {}
evaluations = []

info_dict['Имя'] = info[0]
info_dict['Фамилия'] = info[1]
info_dict['Город'] = info[2]
info_dict['Место учебы'] = info[3]

for i in info[4:]:
    evaluations.append(i)
info_dict['Оценки'] = evaluations

print(info_dict)
