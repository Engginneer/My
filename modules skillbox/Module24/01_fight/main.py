from random import randint


class Warrior:
    def __init__(self, name, health=100, damage=20):
        self.name = name
        self.health = health
        self.damage = damage


if __name__ == '__main__':
    war1 = Warrior('war1')
    war2 = Warrior('war2')
    while war1.health != 0 and war2.health != 0:
        move = randint(1, 2)
        if move == 1:
            war2.health -= war1.damage
            print(f'Воин с ником {war1.name} ударил воина {war2.name}, нанёс {war1.damage} урона, '
                  f' у 2го воина осталось {war2.health} хп')
        else:
            war1.health -= war2.damage
            print(f'Воин с ником {war2.name} ударил воина {war1.name}, нанёс {war2.damage} урона, '
                  f'у 1го воина осталось {war1.health} хп')
    else:
        if war1.health == 0:
            print(f'Воин {war2.name} одержал победу, у него осталось {war2.health}хп')
        else:
            print(f'Воин {war1.name} одержал победу, у него осталось {war1.health}хп')
