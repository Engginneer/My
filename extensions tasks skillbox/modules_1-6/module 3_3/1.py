matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i, num in enumerate(matrix):
    for i_two, num_two in enumerate(matrix[i]):
        print(f'{matrix[i][i_two]}', end = '\t')
    print()


