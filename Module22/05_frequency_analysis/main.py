from collections import defaultdict

file = open('text.txt', 'r')
str_file = file.read()
file.close()
frequency_dict = defaultdict(int)
for sym in str_file:
    if sym.isalpha():
        frequency_dict[sym.lower()] += 1

summ_alpha = sum(frequency_dict.values())
for i in frequency_dict:
    frequency_dict[i] = round(frequency_dict[i] / summ_alpha, 3)

sorted_analysis = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)

print(sorted_analysis)
file_2 = open('analysis.txt', 'w')
for i in sorted_analysis:
    print(i)
    file_2.write(str(i[0]) + ' ' + str(i[1]) + '\n')
file_2.close()
