
# Сама задача, которую нужно сделать красиво
print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if i_key % 2 == 0])

# Решение задачи
print([char for index, char in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if index % 2 == 0])

