def printer(num: int) -> str:
    if num == 1:
        return str(num) + '\n'
    else:
        return printer(num - 1) + str(num) + '\n'


src = int(input('Введите любое число: '))
print(printer(src))
