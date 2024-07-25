def finder(key: str, sites: dict, depth=None):
    if depth == 0:
        return None
    if key in sites:
        return sites[key]
    else:
        if depth:
            depth -= 1
            if depth == 0:
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
            for low_data in sites:
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


# TODO крч смотри, в рекурсии, не надо делать проверку на депс, просто на каждом шаге итерации вычитать единицу, как
#  ток значение становится равно нулю, выход, если указана глубина числом а не наном, второй момент от которого попрошу
#  избавиться, от твоих любимых .values(), они тут не нужны, логика рекурсии примерно следующая, заходит в функцию,
#  чекает, есть ли тут ключ сразу, если нет, чекает указанна ли глубина, и больше ли нуля она, потом начинает
#  обращаться ко всем элементам подряд по ключу, проверять, словарь ли и если словарь, закидывает в рекурсию, у тебя
#  как бы все правильно, все будет работать, базар вокзал, но можно сделать код более читаемым, и чуть менее ветвящимся

# Я постарался подправить по рекомендованному алгоритму, убрал все валюес