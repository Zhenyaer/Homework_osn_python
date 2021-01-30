from random import randint

basic_list = [randint(0, 1000) for i in range(10)]
# basic_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
final_list = [num for i, num in enumerate(basic_list) if i > 0 and basic_list[i] > basic_list[i - 1]]

print(final_list)
