quantity_packs = int(input("Введите количество пакетов: "))
all_packs = []
count_error_packs = 0

for pack in range(quantity_packs):
    print(f'Пакет номер {pack + 1}:')
    stack_pack = []
    for i in range(4):
        info = int(input(f"{i + 1} бит: "))
        stack_pack.append(info)
    print(stack_pack)
    if stack_pack.count(-1) > 1:
        count_error_packs += 1
        print('много ошибок в пакете')
    else:
        all_packs.extend(stack_pack)

print(f'Полученное сообщение: {all_packs}')
print(f'Количество ошибок в сообщении: {all_packs.count(-1)}')
print(f'Количество потерянных пакетов: {count_error_packs}')