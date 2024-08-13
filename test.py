
from collections import defaultdict
from pprint import pprint

freq_dict = defaultdict(int)
eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
char_cntr = 0
with open('text.txt', encoding='utf8', mode='r') as txt:
    for line in txt:
        for char in line:
            if char.lower() in eng_alphabet:
                freq_dict[char.lower()] += 1
                char_cntr += 1

freq_list = list(zip(freq_dict, freq_dict.values()))
freq_list.sort(key=lambda obj: - obj[1])
print(freq_list)
print(char_cntr)

with open('analysis.txt', mode='w', encoding='utf8') as txt:
    for itm in freq_list:
        txt.write(f'{itm[0]}\t{round(itm[1]/char_cntr, 3)}\n')
