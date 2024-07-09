def interests_and_len(x: dict):
    list_interests = set()
    len_name = 0
    for i in students:
        list_interests.update(set(students[i]['interests']))
        len_name += len(students[i]['surname'])

    return list(list_interests), len_name


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

for student in students:
    print(f'ID студента: {student}, его возраст: {students[student]['age']}')

# 2 задание:


interest, len_names = interests_and_len(students)
print(f'Интересы студентов: {interest},\nОбщая длина всех фамилий: {len_names}')
