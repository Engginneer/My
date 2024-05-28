def longer(x: str) -> str:
    word_time = ''
    max_word = ''
    for sym in x:
        if sym != ' ':
            word_time = word_time + sym
        else:
            if len(word_time) > len(max_word):
                max_word = word_time
            word_time = ''
    if len(word_time) > len(max_word):
        return word_time
    else:
        return max_word


if __name__ == '__main__':
    text = input("Введите текст: ")
    long_word = longer(text)
    print(f'Самое длинное слово: "{long_word}"\nЕго длина: {len(long_word)}')