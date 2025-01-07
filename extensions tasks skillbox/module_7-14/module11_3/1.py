from random import randint


class Toyota:
    color_car = 'Red'
    cost = 1000000
    max_speed = 200
    speed = 0

    def info_from(self):
        print(f'Цвет машины: {self.color_car}\nСтоимость машины: {self.cost}\nМаксимальная скорость: '
              f'{self.max_speed}\nТекущая скорость: {self.speed}')

    def change_speed(self, new_sped):
        self.speed = new_sped


car_one = Toyota()
car_two = Toyota()
car_three = Toyota()

car_one.change_speed(randint(1, 200))
print(car_one.speed)
car_one.info_from()
