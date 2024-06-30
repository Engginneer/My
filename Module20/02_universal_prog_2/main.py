
def prime(maximum: int) -> iter:
    ...


inpt = input('Введите фразу для обработки: ')
print([inpt[i] for i in prime(len(inpt) - 1)])
