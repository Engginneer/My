def find_in_str(key_inp: str, site_inp: dict, switch_inp: bool, depth_inp=None):
    result = None
    if key_inp in site_inp:
        return site_inp[key_inp]

    else:
        if switch_inp:
            if depth_inp < 1:
                return None
            depth_inp -= 1

        for key in site_inp:
            if isinstance(site_inp[key], dict):
                result = find_in_str(key_inp, site_inp[key], switch_inp, depth_inp)
                if result:
                    return result
    return None


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

key = input('Введите искомый ключ: ')
switch = True if input('Хотите ввести максимальную глубину? Y/N: ').upper() == 'Y' else False

if switch:
    depth = int(input('Введите максимальную глубину: '))
else:
    depth = 0

print(find_in_str(key, site, switch, depth))
