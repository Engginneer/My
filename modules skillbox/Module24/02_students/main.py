from random import randint
from statistics import mean

if __name__ == '__main__':
    class student:
        def __init__(self, first_last_name, num_group, estimations):
            self.first_last_name = first_last_name
            self.num_group = num_group
            self.estimations = estimations


    list_students = list()
    for i in range(10):
        list_estim = [randint(1, 5) for _ in range(5)]
        info_student = student(f'student{i + 1}', randint(500, 516), list_estim)
        list_students.append(info_student)

    x = sorted(list_students, key=lambda x: mean(x.estimations))

    for i in x:
        print(i.first_last_name, i.num_group, mean(i.estimations))
