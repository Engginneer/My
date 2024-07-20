def printer(num: int) -> str:
    if num == 1:
        str_temp = str(src - num + 1) + '\n'
        return str_temp
    else:
        return str(src - num + 1) + '\n' + printer(num - 1)


src = int(input('Введите число: '))
print(printer(src))
