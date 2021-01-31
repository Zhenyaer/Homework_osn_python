def salary(rate, time_worked, prize):
    # Расчитывает заработную плату сотрудника
    try:
        sal = rate * time_worked + prize
        return f'Размер заработной платы сотрудника составил {sal} бубликов'
    except ValueError:
        return 'Допустим только ввод числовых значений!'


print(salary(500, 160, 15000))
