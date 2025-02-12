sequence = int(input('Введите количество чисел? '))
numCount = 0
for num in range(sequence):
    print('Введите', num + 1, '-е число: ', end='')
    number = int(input())
    for n in range(2, number):
        if number % n == 0:
            numCount += 1
            break
print('Количество простых чисел в последовательности: ', numCount)
