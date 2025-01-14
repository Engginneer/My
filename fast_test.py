from random import randint


class Human:

    def __init__(self, name):
        self.name = name
        self.__fullness = 50
        self.__home = None

    def set_home(self, house):
        self.__home = house

    def eat(self):
        self.__home.set_fridge(self.__home.get_fridge() - 5)
        self.__fullness += 10

    def work(self):
        self.__fullness -= 5
        self.__home.set_money(self.__home.get_money() + 15)

    def play(self):
        self.__fullness -= 5

    def shopping(self):
        self.__home.set_money(self.__home.get_money() - 5)
        self.__home.set_fridge(self.__home.get_fridge() + 15)

    def action_roll(self):

        action = randint(1,6)
        print(f'{self.name} текущая сытость - {self.__fullness}, '
              f'остаток денег - {self.__home.get_money()}, '
              f'остаток еды - {self.__home.get_fridge()} ', end='')

        if self.__fullness <= 0:
            print(f'{self.name} умер(ла) от голода')

        elif self.__fullness < 10:
            print(f'низкая сытость - кушаем')
            self.eat()

        elif self.__home.get_fridge() < 10:
            print('в холодильнике мало еды - закупаемся')
            self.shopping()

        elif self.__home.get_money() < 50:
            print('дома мало денег - работаем')
            self.work()

        elif action == 1:
            self.work()
            print('все в порядке, решил(а) сходить на работу')

        elif action == 2:
            self.eat()
            print('все в порядке, решил(а) перекусить')

        else:
            self.play()
            print('все в порядке, решил(а) поиграться')


class Home:

    def __init__(self):
        self.__fridge = 50
        self.__money = 0

    def get_fridge(self):
        return self.__fridge

    def set_fridge(self, new_value):
        self.__fridge = new_value

    def get_money(self):
        return self.__money

    def set_money(self, new_value):
        self.__money = new_value


if __name__ == '__main__':

    oleg = Human('Oleg')
    anna = Human('Anna')
    home = Home()
    oleg.set_home(home)
    anna.set_home(home)
    for i in range(365):
        print(f'\nДень {i}')
        oleg.action_roll()
        anna.action_roll()
