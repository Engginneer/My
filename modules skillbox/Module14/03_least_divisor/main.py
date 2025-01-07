def nod(src):
    divider = 2
    while divider <= src:
        if src % divider == 0:
            return divider
        divider += 1


if __name__ == '__main__':
    inpt = int(input('Введите число большее единицы: '))
    print(f'Наименьший делитель, отличный от единицы: {nod(inpt)}')
