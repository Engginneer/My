import zipfile
from collections import defaultdict
from pprint import pprint


def extract_file(filename):
    z_file = zipfile.ZipFile(filename)
    name_list = z_file.namelist()
    if name_list:
        for nme in name_list:
            z_file.extract(nme)
        print(f'Извлечены следующие файлы:\n{name_list}')
        return name_list
    else:
        print(f'Архив пуст')
        return None


def counter(txt_file):
    for line in txt_file:
        for char in line:
            if char.isalpha():
                freq_dict[char] += 1


if __name__ == '__main__':
    files_list = extract_file('voyna-i-mir.zip')

    freq_dict = defaultdict(int)

    for name in files_list:
        with open(name, encoding='utf8', mode='r') as txt:
            counter(txt)

    freq_list = list(zip(freq_dict, freq_dict.values()))
    freq_list.sort(key=lambda obj: - obj[1])

    pprint(freq_list)
    summ_symbol = 0
    for i in freq_list:
        summ_symbol += i[1]
    print(summ_symbol)