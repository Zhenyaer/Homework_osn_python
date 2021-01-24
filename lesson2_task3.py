month = int(input('Введите номер месяца от 1 до 12: '))

''' Вариант решения с использованием списка
'''

seasons_l = ['весна', 'лето', 'осень', 'зима']

if 1 <= month <= 12:
    if 3 <= month <= 5:
        print(seasons_l[0].title())
    elif 6 <= month <= 8:
        print(seasons_l[1].title())
    elif 9 <= month <= 11:
        print(seasons_l[2].title())
    else:
        print(seasons_l[3].title())
else:
    print('Такого месяца не существует!')


''' Вариант решения с использованием словаря
'''

seasons_sl = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима',
}

if 1 <= month <= 12:
    print(seasons_sl[month].title())
else:
    print('Такого месяца не существует!')
