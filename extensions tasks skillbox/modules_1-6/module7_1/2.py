import math

def area_cylinder(parameters):
    side = 2 * math.pi * int(parameters[0]) * int(parameters[1])
    full_area = side + 2 * math.pi * int(parameters[1]) ** 2
    return side, full_area





height_radius = input('Введите высоту и радиус через пробел: ').split(' ')

side, full_area = area_cylinder(height_radius)

print(side, full_area)
