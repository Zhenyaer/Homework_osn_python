from random import randint

basic_list = [randint(0, 25) for i in range(50)]
# basic_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
final_list = [num for num in basic_list if basic_list.count(num) == 1]

print(final_list)
