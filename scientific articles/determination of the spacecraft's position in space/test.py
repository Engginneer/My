from generation_table import generation_table


def find_degree(value_cosa, start_x, start_y):  # Функция находит максимально схожее теоретическое значение с получившимся
    # и выдаёт предполагаемые значения углов по осям X и Y
    target_diff = 0.003
    if value_cosa == 0:
        result_x = 'батарея солнечная в тени'
        result_y = 'батарея солнечная в тени'
        return result_x, result_y


    else:
        min_diff = 1
        count = 0
        while min_diff > target_diff:
            count += 1
            base_cos = generation_table()
            result_x = 0
            result_y = 0
            for x in range(start_x - count, start_x + count + 1):
                for y in range(start_y - count, start_y + count + 1):
                    if abs(value_cosa - base_cos[x][y]) < min_diff:
                        min_diff = abs(value_cosa - base_cos[x][y])
                        result_y = y
                        result_x = x
        return result_x, result_y

x_cord, y_cord = find_degree(0.565, 10, 50)
print(x_cord, y_cord)