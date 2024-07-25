def finder(key: str, sites: dict, depth=None):
    if depth == 0:
        return None
    if key in sites:
        return sites[key]
    else:
        if depth:  # эта проверка поидее не имеет смысла, ты на второй строчке ещё проверил все
            depth -= 1
            if depth == 0:  # вот здесь не пойму, а это как будто лишнее, он понизил уровень, и не проверяя что там,
                # выкинул, оно точно работает?, если работает - базар вокзал

                return None
            else:
                for low_data in sites:
                    if isinstance(sites[low_data], dict):
                        result = finder(key, sites[low_data])
                        if result:
                            break
                else:
                    result = None
            return result
        else:
            for low_data in sites:  # крч да, это должно влиться в основную функцию, и 9ая строка соответственно тоже
                # отъезжает

                if isinstance(sites[low_data], dict):
                    result = finder(key, sites[low_data])
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


# TODO погляди мое решение, разберись как оно работает, и потом на память/логику перепиши пж, удивительно как четко ты
#  прочувствовал рекурсию в шестой, и как тут не можешь забороть, как будто списал откуда то там, ну или тут))
