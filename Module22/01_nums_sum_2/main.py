
file = open('numbers.txt', 'r')
summ = 0
str_file = file.read()
for i in str_file:
    if i.isdigit():
        summ += int(i)

file_answer = open('answer.txt', 'w')
file_answer.write(str(summ))
file.close()
file_answer.close()
