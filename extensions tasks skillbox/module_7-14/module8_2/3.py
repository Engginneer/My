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


def find(dict_1: dict, key: iter) -> iter:
    result = None
    if key in dict_1:
        return dict_1[key]

    for value_in in dict_1.values():
        if isinstance(value_in, dict):
            result = find(value_in, key)
            if result:
                return result
    return result


key_find = input('Искомый ключ: ')
value = find(site, key_find)
if value:
    print("Значение:", value)
else:
    print("Такого ключа в структуре сайта нет.")

