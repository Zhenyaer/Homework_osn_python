def sum_max(arg1, arg2, arg3):
    # Выводит сумму двух наибольших чисел
    li = [arg1, arg2, arg3]
    li.remove(min(li))
    return f'Сумма двух наибольших чисел равна {sum(li)}'


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print(sum_max(a, b, c))
