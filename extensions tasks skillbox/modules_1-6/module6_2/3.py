
text = input('Введите текст: ').lower()
count_hist = dict()
for sym in text:
    if sym not in count_hist:
        count_hist[sym] = 1
    else:
        count_hist[sym] += 1

max_frequency = max(count_hist.values())

for letters, value in sorted(count_hist.items()):
    print(f'{letters} : {value}')


print(f'Максимальная частота: {max_frequency}')
