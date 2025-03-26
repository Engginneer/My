from math import pi, cos
def generation_table():
    base_table_cosa = [[round(cos(y * pi / 180) * cos(x * pi / 180), 3)
    if round(cos(y * pi / 180) * cos(x * pi / 180), 3) > 0 else 0 for y in range(0, 181)] for x in range(0, 181)]
    return base_table_cosa