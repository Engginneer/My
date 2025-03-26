from random import randint, uniform


def synthetic_data(power: float, voltage: float):
    value_pow = randint(0, 1000)
    random_step = round(uniform(-20, 20), 4)
    synthet_list = list()
    synthet_list.append(value_pow)
    for i in range(15):
        if value_pow + random_step > 0:
            value_pow = value_pow + random_step
            synthet_list.append(value_pow)
        else:
            synthet_list.append(0)
    return synthet_list
