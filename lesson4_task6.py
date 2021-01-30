from itertools import count, cycle


def iter_gen(a):
    # итератор, генерирующий целые числа, начиная с указанного
    for el in count(a):
        if el > a + 20:
            break
        else:
            print(el)


def iter_rep(b):
    # итератор, повторяющий элементы некоторого списка, определенного заранее
    c = 0
    for i in b:
        for el in cycle(i):
            if c > 20:
                break
            print(el)
            c += 1


try:
    iter_gen(int(input('Введите целое число: ')))
except ValueError:
    print('Допустим только ввод числовых значений!')


iter_rep([input('Введите элементы списка через пробел: ').split()])
