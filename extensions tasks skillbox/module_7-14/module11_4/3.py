class Potato:
    maturity_posit = {0: 'Пусто', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, num, maturity=0):
        self.num = num
        self.maturity = maturity

    def maturity_information(self):
        print(f'Картошка {self.num} сейчас {Potato.maturity_posit[self.maturity]}')

    def height(self):
        if self.maturity < 3:
            self.maturity += 1
        self.maturity_information()

    def maturity_end(self):
        if self.maturity == 3:
            return True
        return False


class PotatoesGarden:

    def __init__(self, count):
        self.potatoes = [Potato(i) for i in range(1, count + 1)]

    def all_height(self):
        print('Картошка прорастает')
        for potato in self.potatoes:
            potato.height()

    def all_maturity_end(self):
        if not all([i_potato.maturity_end() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            return False
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True


Garden_one = PotatoesGarden(5)
Garden_one.all_maturity_end()
for i in range(3):
    Garden_one.all_height()
Garden_one.all_maturity_end()
