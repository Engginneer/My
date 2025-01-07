
def func_question(question='Выйти из программы?',
                  message='Неверный ввод, введите "да" или "нет"',
                  count_try=4):
    while count_try != 0:
        inpt = input(question).lower()
        if inpt == "да":
            return 1
        elif inpt == 'нет':
            return 0
        count_try -= 1
        if count_try == 0:
            print('Количество попыток истекло')
            break
        print(message)
        print(f'попыток осталось {count_try}')



func_question('Вы хотите выйти из программы?')
func_question('Вы хотите удалить файл?', 'Так удалить или нет?')
func_question('Записать файл?', count_try=2)
