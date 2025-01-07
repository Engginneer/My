def assign_the_name(x: int):
    list_card = []
    for i in range(1, x + 1):
        card_model = int(input(f"Введите модель {i} карты: "))
        list_card.append(card_model)
    return list_card


def revised_list(list_card: list, len_list: int):
    new_list = []
    top_card = list_card[0]
    for i in range(0, len_list):
        if list_card[i] > top_card:
            top_card = list_card[i]
    for i in range(0, len_list):
        if list_card[i] != top_card:
            new_list.append(list_card[i])
    return new_list


quantity = int(input("Введите количество видеокарт: "))
list_video_card = assign_the_name(quantity)
new_list_video_card = revised_list(list_video_card, quantity)

print(f'Старый список видеокарт: {list_video_card}')
print(f'Новый список видеокарт: {new_list_video_card}')

#  Красивый код тут вышел
