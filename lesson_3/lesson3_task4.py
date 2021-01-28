def my_func_1(x, y):
    # Возводит в степень через **
    res = x ** y
    return f'Результат возведения в степень равен {res}'


a = int(input('Введите положительное число: '))
b = int(input('Введите отрицательное число: '))

print(my_func_1(a, b))


def my_func_2(x, y):
    # Возводит в степень c помощью цикла
    res = x
    for i in range(abs(y) + 1):
        res = res / y
    return f'Результат возведения в степень равен {res}'


a = int(input('Введите положительное число: '))
b = int(input('Введите отрицательное число: '))

print(my_func_2(a, b))