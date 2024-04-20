import random

if __name__ == '__main__':
    first_group = [round(random.uniform(5, 10), 2) for i in range(20)]
    second_group = [round(random.uniform(5, 10), 2) for i in range(20)]

    list_win = [first_group[i] if first_group[i] >= second_group[i]
                else second_group[i] for i in range(len(first_group))]

    print(first_group)
    print(second_group)
    print(list_win)
