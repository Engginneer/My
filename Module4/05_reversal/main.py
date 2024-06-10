

if __name__ == '__main__':
    word = input('Введите строку, в которой символ "h" встречается не менее 2х раз: ')
    count = 0
    left = 0
    right = 0


    for i, sym in enumerate(word):
        if sym == 'h' and count == 0:
            left = i
            count += 1
        elif sym == 'h':
            right = i

    print(f'Развернутая последовательность между первым "h" и последним: {word[right - 1:left:-1]}')

    print(left, right)
