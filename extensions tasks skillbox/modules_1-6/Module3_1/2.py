quantity = int(input('Введите количество сотрудников: '))
salary_of_worker = []

for worker in range(quantity):
    salary = int(input(f'Введите зарплату {worker + 1} сотрудника: '))
    if salary > 0:
        salary_of_worker.append(salary)

print(f'Сотрудников осталось {len(salary_of_worker)}')
print(f'Их зарплаты: {salary_of_worker}')

print(f'Максимальная зарплата на предприятии: {max(salary_of_worker)}')
print(f'Минимальная зарплата на предприятии: {min(salary_of_worker)}')