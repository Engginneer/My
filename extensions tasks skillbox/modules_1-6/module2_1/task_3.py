quantity = int(input("Введите количество сотрудников: "))
list_worker = []
for _ in range(quantity):
    id_workers = int(input("Введите ID сотрудника: "))
    list_worker.append(id_workers)
search_id = int(input("С каким ID ищем сотрудника? "))

check_work = False
for i in list_worker:
    if i == search_id:
        print('Сотрудник на месте и, скорее всего, работает!')
        check_work = True
        break
if check_work == False:
    print('Сотрудника нет на рабочем месте...')