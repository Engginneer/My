def synonyms_created():
    quantity = int(input('Введите количество пар слов: '))
    synonyms_dict_time = dict()
    for i in range(quantity):
        word = input(f'Введите {i}-ю пару слов через "-": ').split('-')
        synonyms_dict_time[word[0]] = word[1]
    return synonyms_dict_time


def synonyms(dict_input):
    word_input = input('Введите слово: ')
    if word_input not in dict_input and word_input not in dict_input.values():
        print(f'Слова {word_input} нет в словаре, попробуйте еще раз.')
        synonyms(synonyms_dict)
    else:
        if word_input in dict_input:
            print(f'Синоним: {dict_input[word_input]}')
        else:
            for key, value in dict_input.items():  # Можно как-то без цикла обойтись, чтобы вытащить ключ по значению?
                if value == word_input:
                    print(f'Синоним: {key}')
                    break


synonyms_dict = synonyms_created()
synonyms(synonyms_dict)
