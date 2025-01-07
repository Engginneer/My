text = input('Введите текст: ')
sign = {".", ",", ";", ":", "!", "?"}
count = sign.intersection(text)

print(f'Количество знаков пунктуации: {len(count)}')
