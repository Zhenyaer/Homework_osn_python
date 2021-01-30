def fact(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
        yield res


n = int(input('Введите число для получения факториалов от 1 до этого числа: '))

for el in fact(n):
    print(el)
