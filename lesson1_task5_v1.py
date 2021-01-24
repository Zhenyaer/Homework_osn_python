gains = int(input("Введите размер выручки, $: "))
costs = int(input("Введите размер издержек, $: "))

if gains > costs:
    print('Ваша фирма прибыльная')
    profit = int(((gains - costs) / gains) * 100)
    print(f'Рентабельность вашей фирмы составила {profit}%')
    pop = int(input("Введите количество сотдрудников в вашей фирме: "))
    eff = int((gains - costs) / pop)
    print(f'Каждый ваш сотрудник в среднем генерирует {eff}$ прибыли')
elif gains < costs:
    print('Ваша фирма убыточная')
else:
    print('Фирма работает в 0')
