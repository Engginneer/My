quantity_word = int(input('Введите количество слов в тексте: '))
key_word_list = []
count_words = [0, 0, 0]
word_text = ''

for i in range(quantity_word):
    print(f'Введите {i + 1} ключевое слово: ')
    word = input()
    key_word_list.append(word)

while word_text != 'end':
    word_text = input('Введите слово из текста: ')
    for index in range(quantity_word):
        if key_word_list[index] == word_text:
            count_words[index] += 1

print(f'Подсчёт слов в тексте:')
for num in range(quantity_word):
    print(f'Слов "{key_word_list[num]}" в тексте: {count_words[num]}')
