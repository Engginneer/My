class Cell:
    def __init__(self, position, status=0):
        self.position = position
        self.status = status

    def __str__(self):
        return str(self.status)


#num_cell = input('Введите номер клетки в формате XX(строка)(столбец): ')
cells_list = [[Cell(str(j + 1) + str(i + 1)) for i in range(3)] for j in range(3)]
print(cells_list)
cells_list[1][0].status = 'dsfsdf'

for i in cells_list:
    for j in i:
        print(j.position, end=' ')
    print()
print('Status:')
for i in cells_list:
    for j in i:
        print(str(j), end=' ')
    print()



