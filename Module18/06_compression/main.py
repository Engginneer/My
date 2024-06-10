def coding_rar(x: str) -> str:  # TODO ох уж эти иксы
    text_after = ''
    count = 1
    for i in range(1, len(x)):  # TODO тут лучше использовать enumerate(x)

        if x[i - 1] == x[i]:
            count += 1
        elif x[i - 1] != x[i]:
            text_after += x[i - 1]
            text_after += str(count)
            count = 1
        if i == len(x) - 1:
            text_after += x[i]
            text_after += str(count)
    return text_after


if __name__ == '__main__':
    text = input('Введите код без пробелов: ')
    print(coding_rar(text))
