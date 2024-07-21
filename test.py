from pprint import pprint


def market(quantity_inp: int, site_inp, name_inp):
    for i, j in site_inp.items():
        if isinstance(j, str):
            str_in = j.split(' ')
            for index, word in enumerate(str_in):
                if word.lower() == 'телефон':
                    str_in.insert(index, name_inp)
                    str_in.remove('телефон')
            site_inp[i] = ' '.join(str_in)
        else:
            market(quantity_inp, j, name_inp)
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
name = input('Введите название продукта для нового сайта: ')

pprint(market(quantity, site, name))
