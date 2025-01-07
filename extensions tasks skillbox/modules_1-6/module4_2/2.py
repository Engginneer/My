


if __name__ == '__main__':
    original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

    new_list_cost = [(0 if original_prices[i] <= 0 else original_prices[i])
                     for i in range(len(original_prices))]
    print(f'Изначальный список: {original_prices}')
    print(f'Список после изменений: {new_list_cost}')
