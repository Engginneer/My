from random import randint


class Toyota:
    color_car = 'Red'
    cost = 1000000
    max_speed = 200
    speed = 0


car_one = Toyota()
car_two = Toyota()
car_three = Toyota()
print(car_one.speed, car_two.speed, car_three.speed)
car_one.speed = randint(1, 200)
car_two.speed = randint(1, 200)
car_three.speed = randint(1, 200)
print(car_one.speed, car_two.speed, car_three.speed)
