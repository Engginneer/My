shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name_detail = input("Введите наименование детали: ")
quantity = int(input('Введите количество выбранной детали: '))
cost = 0

for i, detail in enumerate(shop):
        if shop[i][0] == name_detail:
                cost = shop[i][1] * quantity
                break
print(f'Общая стоимость: {cost}')

