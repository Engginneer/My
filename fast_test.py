from pprint import pprint
from collections import defaultdict
from copy import deepcopy


def clear_str(str_inp: str) -> str:
    new_str = ''
    for char in str_inp:
        if char.isalpha():
            new_str += char.lower()
    new_str = ''.join(sorted(new_str))
    return new_str


def anagramm(list_inp: list):
    list_clear = []
    dict_out = defaultdict(int)
    for i in list_inp:
        x = clear_str(i)
        list_clear.append(x)

    for i in list_clear:
        dict_out[i] += 1

    dict_out2 = deepcopy(dict_out)

    for key, val in dict_out.items():
        if val < 2:
            dict_out2.pop(key)

    return dict_out2


list_inp1 = ["Ав@сТРа&лоПИтек", "пО&лУс&МЕРть", "дРЕ№вес&ни#ЦА", "ФРА@@киец" "@АНКИлоза@вр",
             "ВАТЕР&&поли@@@СТКА", "ПУльСОме@т&р", "ВоС;пРе;ЩеНи;E" "СЕРдЦ@ЕВ&&ина", "АВС,,,триец",
             "ЦАРС;ТВ@ИЕ", "Ис@То&ПН;иК"]

pprint(anagramm(list_inp1))
