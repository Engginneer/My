def fake_fact(num: int) -> int:
    if num == 1:
        return 1
    answer = fake_fact(num - 1)
    return num * fake_fact(num - 1)


num = int(input('Введите число, для которого нужно найти факториал: '))
print(fake_fact(num))
