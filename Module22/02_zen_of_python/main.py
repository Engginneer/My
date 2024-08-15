file = open('zen.txt', 'r')
temp_str = file.read()
temp_list = temp_str.split('\n')
file.close()
file = open('zen_copy.txt', 'a')

temp_list = temp_list[::-1]
ans_str = '\n\n\n'
for i_elem in temp_list:
    ans_str += i_elem
    ans_str += '\n'
file.write(ans_str)
file.close()

