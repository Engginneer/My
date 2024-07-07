def interests_and_len(x: dict):
    list_interests = []
    for values in x.values():
        for sense in values['interests']:
            list_interests.append(sense)

    len_name = 0
    for values in x.values():
        for sense in values['surname']:
            len_name += len(sense)

    return list_interests, len_name


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

# 1 задание:

for ID, data in students.items():
    print(f'ID студента: {ID}, его возраст: {data['age']}')

# 2 задание:


interest, len_names = interests_and_len(students)
print(f'Интересы студентов: {interest},\nОбщая длина всех фамилий: {len_names}')
