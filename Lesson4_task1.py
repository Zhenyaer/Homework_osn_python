def salary():
    # Расчитывает заработную плату сотрудника
    try:
        rate = int(input('Введите ставку сотрудника: '))
        time_worked = int(input('Введите отработанное время: '))
        prize = int(input('Введите размер премии: '))
        sal = rate * time_worked + prize
        return f'Размер заработной платы сотрудника составил {sal}'
    except ValueError:
        return 'Допустим только ввод числовых значения!'


print(salary())
