user_list = input('Введите значения списка через запятую: ').split(',')
print(user_list)

k = 0
for i in range(int(len(user_list) / 2)):
    user_list[k], user_list[k + 1] = user_list[k + 1], user_list[k]
    k += 2
print(user_list)
