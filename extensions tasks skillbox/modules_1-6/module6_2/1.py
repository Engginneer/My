small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}
big_storage.update(small_storage)
quantity = input('Введите нужный товар: ')
print(f' Количество товара "{quantity}": {big_storage.get(quantity)}')
