def printer(num: int) -> str:
    if num == 1:
        str_temp = str(src - num + 1) + '\n'
        return str_temp
    else:
        return str(src - num + 1) + '\n' + printer(num - 1)


src = int(input('Введите число: '))
print(printer(src))

# TODO функция не должна обращаться к глобальной области видимости (src), переделывать 10 из 10, и в целом str_temp
#  не нужен, его нафиг отсюда