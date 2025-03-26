from generation_table import generation_table


def find_degree(value_cosa, start_x, start_y):  # Функция находит максимально схожее
    # теоретическое значение с получившимся
    # и выдаёт предполагаемые значения углов по осям X и Y
    target_diff = 0.1 # тут типо можно выбирать погрешность определения угла
    base_cos = generation_table()
    if value_cosa == 0:
        result_x = 'батарея солнечная в тени'
        result_y = 'батарея солнечная в тени'
        return result_x, result_y
    else:
        min_diff = 1
        count = 0
        while min_diff < target_diff or count < 2: # тут я бы хотел реализовать выход из цикла либо по шагам в стороны
            # в матрице либо по точности, которой он достигнет, но он не выходит, я уже голову сломал

            count += 1
            result_x = 0
            result_y = 0
            for x in range(start_x - count, start_x + count + 1):
                for y in range(start_y - count, start_y + count + 1):
                    if abs(value_cosa - base_cos[x][y]) <= min_diff:
                        min_diff = abs(value_cosa - base_cos[x][y])
                        result_y = x
                        result_x = y
        return result_x, result_y
