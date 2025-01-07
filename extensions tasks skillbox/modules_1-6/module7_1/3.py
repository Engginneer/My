import random

def change(nums):
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    temp_list = list(nums)
    temp_list[index] = value
    return temp_list, value


my_nums = (1, 2, 3, 4, 5)
new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)

new_nums = change(my_nums)
rand_val += new_nums[1]
print(new_nums[0], rand_val)

