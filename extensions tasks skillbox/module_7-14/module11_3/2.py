class Family:
    family_name = 'Simple_surname'
    money = 10
    have_a_haus = False

    def info_family(self):
        print(f'{self.family_name}\n{self.money}\n{self.have_a_haus}')

    def earn_money(self, earn):
        if earn:
            self.money += earn

    def bay_a_haus(self, cost, discount=0):
        remains = self.money - cost + cost * discount / 100
        if remains >= 0:
            self.money = remains
            self.have_a_haus = True
            print(f'Дом успешно приобретен, остаток средств {self.money}')
        else:
            print('Денег на дом не хватает')


family_one = Family()
family_one.info_family()
family_one.earn_money(10)
family_one.info_family()
family_one.bay_a_haus(21, 10)
family_one.info_family()
