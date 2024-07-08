def is_prime(x: int) -> bool:
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
        if count > 2:
            break
    if count == 2:
        return True
    else:
        return False


def main(object_input):
    list_output = []
    for index, char in enumerate(object_input):
        if is_prime(index):
            list_output.append(char)
    return list_output


object_input = 'О Дивный Новый мир!'
list_output = main(object_input)
print(list_output)


#  выполни по этой архитектуре, не просто так оставил, тебе надо написать только одну функцию prime, ввод и вывод функции указан, если очень хочешь, можешь использовать ещё и is_prime
# и ещё подумай как ускорить твою функцию is_prime, прям базовую утечку ресурса цпу оставил в этой задаче


def prime(maximum: int) -> iter:
    ...


inpt = input('Введите фразу для обработки: ')
print([inpt[i] for i in prime(len(inpt) - 1)])
