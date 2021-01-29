def division(arg1, arg2):
    # Выводит результат деления двух чисел
    res = arg1 / arg2
    return f'Результат деления равен: {res}'


x = int(input('Введите делимое: '))
while True:
    y = int(input('Введите делитель: '))
    if y != 0:
        break
    else:
        print('Делить на 0 нельзя! Введите другое число')
        continue

print(division(x, y))
