import random

rand_list = [random.randint(-100, 100) for i in range(random.randint(0, 100))]
print(len(rand_list))
print(rand_list)

a = random.randint(0, len(rand_list) // 2)
b = random.randint(len(rand_list) // 2, len(rand_list))
print(a)
print(b)

rand_list = rand_list[0:a - 1] + rand_list[b:len(rand_list)]

print(rand_list)
