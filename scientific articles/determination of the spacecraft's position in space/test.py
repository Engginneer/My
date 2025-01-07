import pandas

base_cos = pandas.read_excel('base_cos.xlsx')
angle = 0.587
min_diff = 1
result_X = 0
result_Y = 0
for x in range(0, 91, 5):
    for y in range(1, 19):
        if abs(angle - base_cos[x][y]) < min_diff:
            min_diff = abs(angle - base_cos[x][y])
            result_X = x
            result_Y = y * 5

print(result_X, result_Y)

