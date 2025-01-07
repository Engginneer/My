# TODO здесь писать код
from math import sqrt


def get_sage_sqrt(num):
    answer = []
    try:
        if num <= 0:
            raise ValueError('Число меньше либо равно нулю')
        else:
            answer.append(sqrt(num))
    except ValueError as exp1:
        answer.append(exp1)
    except Exception as exp2:
        answer.append(exp2)
    return answer


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
