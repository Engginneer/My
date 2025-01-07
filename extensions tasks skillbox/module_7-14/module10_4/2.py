from collections import defaultdict


def palindrome(word: str) -> bool:
    possible = False
    dict_str = defaultdict(int)

    for char in word:
        dict_str[char] += 1

    poly = 2

    for values in dict_str.values():
        if values % 2 == 1:
            poly -= 1
            if poly == 0:
                return possible

    else:
        possible = True
        return possible


words = open('words.txt', 'r', encoding='utf8')
list_words = words.read().split('\n')
words.close()
summ_words_pal = 0
for word in list_words:
    if not word.isalpha():
        raise ValueError(f'Слово {word} содержит в себе цифры!')
    else:
        if palindrome(word):
            summ_words_pal += 1

print(f'Слов, из которых можно сделать палиндром: {summ_words_pal}')
