file = 'task3.txt'
my_f = open(file, "r")
content = my_f.readlines()
sal = 0

for i in range(len(content)):
    for x in content[i].split():
        try:
            x = int(x)
            sal += x
            if x < 20000:
                print(f'{content[i].split()[0]} имеет оклад менее 20 тыс.')
        except ValueError:
            pass

print(f'\nСредняя зарплата сотрудников составляет: {sal / len(content)}')
