def division():
    # Выводит результат деления двух чисел
    arg1 = int(input('Введите делимое: '))
    while True:
        arg2 = int(input('Введите делитель: '))
        if arg2 != 0:
            res = arg1 / arg2
            return f'Результат деления равен: {res}'


print(division())
