from random import randint
from time import sleep


class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.childs = []

    def relax_child(self, child):
        child.relax()

    def feed_child(self, child):
        child.feed()

    def check_babies(self):
        for baby in self.childs:
            if baby.crying():
                if baby.hungry:
                    print(f'{baby.name} голоден')
                    baby.feed()
                    print(f'{self.name} покормил {baby.name}')

                elif not baby.relax_state:
                    print(f'{baby.name} не спокоен')
                    baby.feed()
                    print(f'{self.name} успокоил {baby.name}')

            else:
                print(f'{baby.name} спит')

class Child:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.relax_state = True
        self.hungry = False

    def relax(self):
        self.relax_state = True

    def feed(self):
        self.hungry = False

    def rand_states(self):
        if 0 < randint(0, 100) < 50:
            self.hungry = True

        if 0 < randint(0, 100) < 50:
            self.relax_state = False

    def crying(self):
        if self.relax_state == False or self.hungry == True:
            print(f'Ребенок {self.name} плачет')
            return True

        return False


if __name__ == '__main__':

    viktor = Parent('Vikotr', 29)
    natalya = Parent('Natalya', 28)
    stepa = Child('Stepan', 0)
    viktor.childs.append(stepa)
    natalya.childs.append(stepa)
    while True:
        stepa.rand_states()
        if 0 < randint(0, 100) < 50:
            viktor.check_babies()

        else:
            natalya.check_babies()
        sleep(2)
        print('\n')
