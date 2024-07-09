def is_prime(num: int) -> bool:
    count = 0
    for i in range(1, round(num)):
        if num % i == 0:
            count += 1
        if count > 1:
            return False
    if count == 1:
        return True
    else:
        return False


def prime(maximum: int) -> iter:
    list_output = []
    for i in range(maximum):
        if is_prime(i):
            list_output.append(i)
    return list_output


if __name__ == '__main__':
    inpt = input('Введите фразу для обработки: ')
    print([inpt[i] for i in prime(len(inpt))])

    print(prime(len(inpt) - 1))
