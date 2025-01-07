
if __name__ == '__main__':
    list_words = input('Введите слова через запятую: ').split(', ')
    text = input('Введите текст: ')

    for i in range(len(list_words)):
        x = text.count(list_words[i])
        print(f'Слово {list_words[i]} встречается в тексте {x} раз')





