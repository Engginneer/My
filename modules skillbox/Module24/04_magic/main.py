# TODO здесь писать код
# Вот таблица преобразований:
#
# Вода + Воздух = Шторм
# Вода + Огонь = Пар
# Вода + Земля = Грязь
# Воздух + Огонь = Молния
# Воздух + Земля = Пыль
# Огонь + Земля = Лава
class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam
        elif isinstance(other, Earth):
            return Lava
        elif isinstance(other, Air):
            return Lightning
        else:
            return None


class Water:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam
        elif isinstance(other, Earth):
            return Dirt
        elif isinstance(other, Fire):
            return Storm
        elif isinstance(other, Frost):
            return Ice


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt
        elif isinstance(other, Air):
            return Dust
        elif isinstance(other, Fire):
            return Lava


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm
        elif isinstance(other, Earth):
            return Dust
        elif isinstance(other, Fire):
            return Lightning
        elif isinstance(other, Frost):
            return Blizzard


class Frost:
    def __add__(self, other):
        if isinstance(other, Water):
            return Ice
        elif isinstance(other, Air):
            return Blizzard


#
#
class Steam:
    def __str__(self):
        return 'Пар'


class Lava:
    def __str__(self):
        return 'Лава'


class Storm:
    def __str__(self):
        return 'Шторм'


class Dust:
    def __str__(self):
        return 'Пыль'


class Dirt:
    def __str__(self):
        return 'грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Ice:
    def __str__(self):
        return 'Лёд'


class Blizzard:
    def __str__(self):
        return 'Вьюга'


fire = Fire()
water = Water()
earth = Earth()
air = Air()
frost = Frost()
x = water + frost
print(x)  #Почему он мне выдаёт класс - как объект, а не как строковое представление через __str__?
print(x()) # А вот так выдает правильно, почему?? Причем если несуществующую комбинацию поставить,
# в этом принте он выдаст ошибку