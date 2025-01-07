def main():
    word = list(input('Введите слово для проверки: '))
    word_print = ''
    switch = []

    for i, letter in enumerate(word):
        word_print += word[i]

    for i, letter in enumerate(word):
        switch.append(word[len(word) - 1 - i])

    if word == switch:
        print(f'Слово {word_print} является палиндромом')
    elif word != switch:
        print(f'Слово {word_print} не является палиндромом')
    main()

main()

"""
тут ты вообще запутался как вижу, сначала стринг в лист превратил, потом побуквенно обратно в стринг...
попробуй переписать, не очень красиво вышло, рекомендую использовать для обратного 
порядка word[-i] вместо len-1-i

"""

