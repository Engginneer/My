with open('data.txt', 'r', encoding='utf8') as chat_temp:
    new_list = list(chat_temp)
    x = new_list[0]
    print(x)
    x = x.split(' ')
    print(x[0])
