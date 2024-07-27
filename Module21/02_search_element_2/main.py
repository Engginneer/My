def find_in_str(key_inp: str, site_inp: dict, depth_inp=None):
    result = None
    if key_inp in site_inp:
        return site_inp[key_inp]
    elif depth_inp or depth_inp == 0:
        if depth_inp == 0:
            return result
        else:
            depth_inp -= 1
            for key in site_inp:
                if isinstance(site_inp[key], dict):
                    result = find_in_str(key_inp, site_inp[key], depth_inp)
                    if result:
                        return result
                return result
    else:
        for key in site_inp:
            if isinstance(site_inp[key], dict):
                result = find_in_str(key_inp, site_inp[key], depth_inp)
                if result:
                    return result
        return result


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

key = input('Введите ключ: ')
depth_Y_N = input('Хотите указать глубину поиска? y - да, n - нет ').lower()
if depth_Y_N == 'y':
    depth = int(input('Введите глубину: '))
    print(find_in_str(key, site, depth))
else:
    print(find_in_str(key, site))


# TODO погляди мое решение, разберись как оно работает, и потом на память/логику перепиши пж, удивительно как четко ты
#  прочувствовал рекурсию в шестой, и как тут не можешь забороть, как будто списал откуда то там, ну или тут))
