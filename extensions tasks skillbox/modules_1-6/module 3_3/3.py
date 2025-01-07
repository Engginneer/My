goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

new_fruit = input('Введите новый фрукт: ')
cost_new_fruit = int(input('Введите цену нового фрукта: '))

temp_list = []
temp_list.append(new_fruit)
temp_list.append(cost_new_fruit)

goods.append(temp_list)
print(f'Новый список фруктов: {goods}')
print()

for i in range(len(goods)):
    goods[i][1] *= 1.08
    goods[i][1] = round(goods[i][1], 2)

print(f'Новый список после удорожания: {goods}')
