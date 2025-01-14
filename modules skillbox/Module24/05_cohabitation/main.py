# TODO здесь писать код
from random import randint


class Human:
    def __init__(self, name, house, satiety=50):
        self.name = name
        self.satiety = satiety
        self.house = house

    def to_eat(self):
        self.satiety += 1
        self.house.eat_in_fridge -= 1

    def go_to_work(self):
        self.satiety -= 1
        self.house.money += 1

    def go_to_market(self):
        self.house.money -= 1
        self.house.eat_in_fridge += 1

    def to_game(self):
        self.satiety -= 1

    def day(self):
        print(f'Сытость {hum.name} = {hum.satiety}')
        x = randint(1, 6)
        if hum.satiety < 20:
            hum.to_eat()
            print(f'{hum.name} поел, сытость = {hum.satiety}')
        elif house.eat_in_fridge < 10:
            hum.go_to_market()
            print(f'{hum.name} сходил в магазин, еды стало - {hum.house.eat_in_fridge}')
        elif house.money < 50:
            hum.go_to_work()
            print(f'{hum.name} подзаработал, теперь денег -  {hum.house.money}')
        elif x == 1:
            hum.go_to_work()
            print(f'{hum.name} подзаработал, теперь денег -  {hum.house.money}')
        elif x == 2:
            hum.to_eat()
            print(f'{hum.name} поел, сытость = {hum.satiety}')
        else:
            hum.to_game()
            print(f'{hum.name} поиграл, сытость = {hum.satiety}')


class House:
    def __init__(self, eat_in_fridge=50, money=0):
        self.eat_in_fridge = eat_in_fridge
        self.money = money
        self.list_lodger = []


if __name__ == '__main__':
    house = House()
    Feel = Human('Фил', house)
    Amanda = Human('Аманда', house)
    house.list_lodger.append(Feel)
    house.list_lodger.append(Amanda)
    for i in range(365):
        print(f'День № {i + 1}')
        print()
        print(f'Денег осталось - {house.money}')
        print(f'Еды в холодильнике осталось - {house.eat_in_fridge}')
        for hum in house.list_lodger:
            if hum.satiety <= 0:
                print(f'{hum} - умер(ла) от голода.')
                break
            hum.day()
        print()
