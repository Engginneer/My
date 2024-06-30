
def zipper(first: iter, second: iter) -> tuple:
    ...


first_data = 'asd'
secondary_data = (10, 20, 30, 40)

res = zip(first_data, secondary_data)
for itm in res:
    print(tuple(itm))

print('\n\n')

res1 = zipper(first_data, secondary_data)
for itm in res1:
    print(tuple(itm))
