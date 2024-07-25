from pprint import pprint
from copy import deepcopy


def market(site_inp, name_inp):
    for i, j in site_inp.items():
        if isinstance(j, str):
            str_in = j.split(' ')
            for index, word in enumerate(str_in):
                if word.lower() == 'телефон':
                    str_in.insert(index, name_inp)
                    str_in.remove('телефон')
            site_inp[i] = ' '.join(str_in)
        else:
            market(j, name_inp)
    return site_inp


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

quantity = int(input('Введите количество сайтов: '))

list_dict = []
while quantity != 0:
    quantity -= 1
    temp_dict = deepcopy(site)
    name = input('Введите название продукта для нового сайта: ')
    list_dict.append(market(temp_dict, name))
    pprint(list_dict)

# TODO ты это прекращай, да ".items()", ща подумал, тут наверн рекурсия предполагается из предыдущего задания
#  тебе скорее всего надо найти теги, и просто их править, хотя пох, главное от .items() избавься, они не нужны для
#  такого решения
