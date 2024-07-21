def printer(num: int) -> str:
    if num == 1:
        return str(num) + '\n'
    else:
        return printer(num - 1) + str(num) + '\n'


src = int(input('Введите число: '))
print(printer(src))

# TODO функция не должна обращаться к глобальной области видимости (src), переделывать 10 из 10, и в целом str_temp
#  не нужен, его нафиг отсюда