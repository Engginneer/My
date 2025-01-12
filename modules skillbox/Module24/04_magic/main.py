# TODO здесь писать код
class Fire:
    def __add__(self, Water):
        return Steam


class Water:
    def __add__(self, Fire):
        return Steam

# class Earth:
#
#
# class Air:
#
#
class Steam:
    print(f'Сложили воду и огонь, получили пар')


print(Fire() + Water())