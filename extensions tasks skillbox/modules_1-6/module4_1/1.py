


if __name__ == '__main__':
    a = int(input("Введите левую границу: "))
    b = int(input("Введите правую границу: "))

    first_list = [i ** 3 for i in range(b - a, b + 1)]
    second_list = [i ** 2 for i in range(b - a, b + 1)]
    print(f'Список кубов чисел в диапазоне от {a} до {b} : {first_list}')
    print(f'Список квадратов чисел в диапазоне от {a} до {b} : {second_list}')