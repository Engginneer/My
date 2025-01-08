from pprint import pprint
from math import pi, cos

base_table_cosa = [[round(cos(y * pi / 180) * cos(x * pi / 180), 3) for y in range(0, 91)] for x in range(0, 91)]



for i in list_for_boss:
    print(i)
