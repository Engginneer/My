


if __name__ == '__main__':
    quantity = int(input("Введите количество товаров: "))
    start_cost = [float(input(f"Введите стоимость {i}го товара:  ")) for i in range(1, quantity + 1)]

    cost_first_year = int(input("Введите повышение на первый год: "))
    cost_second_year = int(input("Введите повышение на второй год: "))

    first_year = [i + (i * cost_first_year / 100) for i in start_cost]
    second_year = [i + (i * cost_second_year / 100) for i in first_year]

    print(f'Сумма цен за каждый год: {sum(start_cost)}, {sum(first_year)}, {round(sum(second_year), 2)}')
