from zipfile import ZipFile
from collections import defaultdict
from pprint import pprint

with ZipFile('voyna-i-mir.zip', 'r') as inside:
    inside.extractall()

book = open('voyna-i-mir.txt', 'r', encoding='UTF=8')

text_for_book = book.read()
analysis_symbol = defaultdict(int)
for sym in text_for_book:
    if sym.isalpha():
        analysis_symbol[sym.lower()] += 1
book.close()
result = sorted(analysis_symbol.items(), key=lambda item: item[1], reverse=True)
pprint(result)

result = dict(result)
summ_symbol = 0
for i in result:
    summ_symbol += result[i]

print(f'Всего букв в произведении: {summ_symbol}')
