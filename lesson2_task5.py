current_rating = list(range(9, 0, -2))
print(f'Текущий рейтинг: {current_rating}')

rate = int(input('Добавьте новое значение: '))

new_rate = current_rating
new_rate.append(rate)

for i in range(len(new_rate) - 1):
    while new_rate[len(new_rate) - i - 1] > new_rate[len(new_rate) - i - 2]:
        new_rate[len(new_rate) - i - 1], new_rate[len(new_rate) - i - 2] = \
            new_rate[len(new_rate) - i - 2], new_rate[len(new_rate) - i - 1]

print(f'Обновленный рейтинг: {new_rate}')
