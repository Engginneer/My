from random import randint


class Toyota:

    def __init__(self, color_car, cost, max_speed, speed):
        self.color_car = color_car
        self.cost = cost
        self.max_speed = max_speed
        self.speed = speed

    def info_from(self):
        print(f'Цвет машины: {self.color_car}\nСтоимость машины: {self.cost}\nМаксимальная скорость: '
              f'{self.max_speed}\nТекущая скорость: {self.speed}')

    def change_speed(self, new_sped):
        self.speed = new_sped


car_one = Toyota('Red', 1000000, 200, 0)
car_two = Toyota('Red', 1000000, 200, 0)
car_three = Toyota('Red', 1000000, 200, 0)

car_one.change_speed(randint(1, 200))
print(car_one.speed)
car_one.info_from()
