from pprint import pprint
from copy import deepcopy


def market(site_inp, name_inp):
    for key in site_inp:
        if isinstance(site_inp[key], str):
            str_in = site_inp[key].split(' ')
            for index, word in enumerate(str_in):
                if word.lower() == 'телефон':
                    str_in[index] = name_inp

            site_inp[key] = ' '.join(str_in)
        else:
            market(site_inp[key], name_inp)
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
