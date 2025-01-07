file = open('numbers.txt', 'r')
file_new = open('answer.txt', 'w')
summ = 0
for i_line in file:
    summ += int(i_line)
file_new.write(str(summ))
