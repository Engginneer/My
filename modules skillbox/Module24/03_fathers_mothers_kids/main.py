# TODO здесь писать код
from random import randint


def list_kid(list_kid):
    print_list_child = list()
    for kid in list_kid:
        print_list_child.append(str(kid.name))
    return print_list_child


class Parent:
    def __init__(self, name, age, list_child):
        self.name = name
        self.age = age
        self.list_child = list_child

    def info(self):
        print_list_child = list_kid(self.list_child)
        print(f'Меня зовут {self.name}, мне {self.age} лет! {print_list_child} - мои дети!')

    def calm_to_child(self):
        list_kids = list_kid(self.list_child)
        choise_child = input(f'Какого ребенка вы хотите успокоить: {list_kids}? ')
        for i, kid in enumerate(list_kids):
            if kid == choise_child:
                if self.list_child[i].state_of_calm == 0:
                    print(f'Малыш {kid} итак спокоен')
                else:
                    self.list_child[i].state_of_calm = 0
                    print(f'Родитель успокоил малыша с именем {kid}')

    def to_feed_to_child(self):
        list_kids = list_kid(self.list_child)
        choise_child = input(f'Какого ребенка вы хотите покормить: {list_kids}? ')
        for i, kid in enumerate(list_kids):
            if kid == choise_child:
                if self.list_child[i].state_of_hungry == 0:
                    print(f'Малыш {kid} не голоден!')
                else:
                    self.list_child[i].state_of_hungry = 0
                    print(f'Малыш с именем {kid} покушал и доволен!')


class Kid:
    def __init__(self, name, age, state_of_calm, state_of_hungry):
        self.name = name
        self.age = age
        self.state_of_calm = state_of_calm
        self.state_of_hungry = state_of_hungry

    def info_kid(self):
        print(f'Меня зовут {self.name}, мне {self.age} год(а)!')
        if self.state_of_calm == 1:
            print(f'Я плачу, меня нужно успокоить!')
        else:
            print(f'Я спокоен')
        if self.state_of_hungry == 1:
            print(f'Я хочу кушать!')
        else:
            print(f'Я сыт!')


Semen = Kid('Семен', 2, randint(0, 1), randint(0, 1))
Alisa = Kid('Алиса', 1, randint(0, 1), randint(0, 1))
Sveta = Kid('Света', 3, randint(0, 1), randint(0, 1))

print(Semen.age)

while True:
    try:
        age_parent = int(input('Введите возраст родителя: '))
        Parent_Vasya = Parent('Вася', age_parent, [Semen, Sveta, Alisa])
        for kid in Parent_Vasya.list_child:
            if Parent_Vasya.age - kid.age <= 16:
                raise ValueError('Ошибка возраста')
        break
    except:
        print('Разница в возрасте родителя и ребенка должна быть минимум 16 лет')
Parent_Vasya.info()
Semen.info_kid()
Alisa.info_kid()
Sveta.info_kid()
Parent_Vasya.calm_to_child()
Semen.info_kid()
Alisa.info_kid()
Sveta.info_kid()
Parent_Vasya.to_feed_to_child()
Semen.info_kid()
Alisa.info_kid()
Sveta.info_kid()
