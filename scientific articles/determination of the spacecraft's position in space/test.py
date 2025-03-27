from generation_table import generation_table


def find_degree(value_cosa, start_x, start_y, DT_X, DT_Y):  # Функция находит максимально схожее теоретическое значение
    # с получившимся и выдаёт предполагаемые значения углов по осям X и Y, она так же использует температуру панелей
    target_diff = 0.05
    if value_cosa == 0:
        result_x = 'батарея солнечная в тени'
        result_y = 'батарея солнечная в тени'
        return result_x, result_y


    else:
        min_diff = 1
        count = 0
        if DT_X > DT_Y:
            while min_diff > target_diff:
                count += 1
                base_cos = generation_table()
                result_x = 0
                result_y = 0
                for x in range(start_x - count, start_x + count + 1):
                    for y in range(start_y, start_y + 1):
                        if abs(value_cosa - base_cos[x][y]) < min_diff:
                            min_diff = abs(value_cosa - base_cos[x][y])
                            result_y = y
                            result_x = x
            return result_x, result_y
        elif DT_X < DT_Y:
            while min_diff > target_diff:
                count += 1
                base_cos = generation_table()
                result_x = 0
                result_y = 0
                for x in range(start_x, start_x + 1):
                    for y in range(start_y - count, start_y + count + 1):
                        if abs(value_cosa - base_cos[x][y]) < min_diff:
                            min_diff = abs(value_cosa - base_cos[x][y])
                            result_y = y
                            result_x = x
            return result_x, result_y

x_cord, y_cord = find_degree(0.34, 10, 50, 0, 1)
print(x_cord, y_cord)