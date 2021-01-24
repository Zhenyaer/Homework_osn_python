number = int(input('Введите любое целое положительное число: '))

max_figure = 0

while number != 0:
    figure = number % 10
    number = number // 10
    if max_figure < figure:
        max_figure = figure

print(max_figure)
