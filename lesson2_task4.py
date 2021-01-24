user_list = input('Введите строку состоящую из нескольких слов через пробел: ').split(' ')

for i in range(len(user_list)):
    print(f'{i+1}. {user_list[i][:10]}')
