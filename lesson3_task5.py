def my_func():
    summa = 0
    flag = True
    while flag:
        user_nums = input('Введите числа через пробел для расчета суммы или введите "$" для выхода: ').split()
        for num in user_nums:
            if num != '$':
                summa += int(num)
            else:
                flag = False
        print(f'Сумма введенных чисел составляет {summa}')


my_func()
