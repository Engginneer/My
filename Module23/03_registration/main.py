str_good_log = ''
str_bad_log = ''

with open('registrations.txt', 'r', encoding='utf8') as registr_data:
    for i_line in registr_data:
        try:
            temp_list_data = i_line.split(' ')
            if len(temp_list_data) != 3:
                raise IndexError
            if not temp_list_data[0].isalpha():
                raise NameError
            if '@' not in temp_list_data[1] or '.' not in temp_list_data[1]:
                raise SyntaxError
            if not 10 < int(temp_list_data[2]) < 99:
                raise ValueError
            else:
                str_good_log += i_line
        except IndexError:
            str_bad_log += (i_line + ' - Ошибка заполнения полей\n')
        except NameError:
            str_bad_log += (i_line + ' - Ошибка имени\n')
        except SyntaxError:
            str_bad_log += (i_line + ' - Ошибка поля "емейл"\n')
        except ValueError:
            str_bad_log += (i_line + ' - Ошибка возраста\n')
    else:
        print('Программа выполнена, начинаем запись)')
with (open('registrations_good.txt', 'w', encoding='utf8') as good,
      open('registrations_bad.txt', 'w', encoding='utf8') as bad):
    good.write(str_good_log)
    bad.write(str_bad_log)
