goods = []
good = []
i = 1

while True:
    add = input('Для добавления нового товара введите "Да", \nДля выхода из цикла введите любое другое значение: ')
    add_prod = {}
    if add == 'Да':
        add_prod['название'] = input('Введите название товара: ')
        add_prod['цена'] = int(input('Введите цену товара: '))
        add_prod['количество'] = int(input('Введите количество товара: '))
        add_prod['ед.'] = input('Введите единицы измерения товара: ')
        good.append(i)
        good.append(add_prod)
        goods.append(tuple(good))
        i += 1
        good.clear()
    else:
        break

print(goods)

an_goods = {}
for product in goods:
    for key, value in product[-1].items():
        if key in an_goods:
            if value not in an_goods.get(key):
                an_goods.get(key).append(value)
        else:
            an_goods.update({key: [value]})

print(an_goods)
