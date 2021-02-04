my_f = open("task5.txt", "w")
numbers = input('Введите числа через пробел: ').split()
for number in numbers:
    my_f.writelines(number + ' ')
my_f.close()

my_f = open("task5.txt", "r")
content = my_f.readlines()
summ = 0
for i in range(len(content)):
    for x in content[i].split():
        try:
            x = int(x)
            summ += x
        except ValueError:
            pass

print(f'Сумма введенных чисел равна: {summ}')
