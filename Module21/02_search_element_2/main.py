def finder(key: str, sites: dict, depth=None):
    if not depth:
        if key in sites:
            return sites[key]
        else:
            for low_data in sites.values():
                if isinstance(low_data, dict):
                    result = finder(key, low_data)
                    if result:
                        break
            else:
                result = None
        return result

    elif depth == 1:
        if key in sites:
            return sites[key]

    else:
        for low_data in sites.values():
            if isinstance(low_data, dict):
                result = finder(key, low_data, depth - 1)
                if result:
                    break
        else:
            result = None
        return result


if __name__ == '__main__':

    site = {
        'html': {
            'head': {
                'title': 'Мой сайт'
            },
            'body': {
                'h2': 'Здесь будет мой заголовок',
                'div': 'Тут, наверное, какой-то блок',
                'p': 'А вот здесь новый абзац'
            }
        }
    }

    key_inp = input('Введите искомый ключ: ')
    depth_Y_N = input('Хотите ввести максимальную глубину? Y/N:').lower()
    if depth_Y_N == 'n':
        print(f'Значение ключа: {finder(key_inp, site)}')
    elif depth_Y_N == 'y':
        depth_inp = int(input('Введите глубину поиска: '))
        print(f'Значение ключа: {finder(key_inp, site, depth_inp)}')
