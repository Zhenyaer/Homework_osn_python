def division():
    # Возвращает результат деления двух чисел
    arg1 = int(input('Введите делитель: '))
    while True:
        arg2 = int(input('Введите делитель: '))
        if arg2 != 0:
            res = arg1 / arg2
            return f"Резьтат деления двух чисел равен: {res}"
        else:
            print('Делить на 0 нельзя, введите другое число: ')


print(division())
