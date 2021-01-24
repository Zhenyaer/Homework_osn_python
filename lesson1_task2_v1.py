time = int(input('Enter time in sec: '))

# По условия максимальное количество часов двузначное значение, принимаем 99 часов
time_max = 100 * 60 * 60 - 1

hour = time // 3600
minute = (time - hour * 3600) // 60
sec = time % 60

if time < time_max:
    if hour < 10:
        hour = str(f'0{hour}')
    if minute < 10:
        minute = str(f'0{minute}')
    if sec < 10:
        sec = str(f'0{sec}')
    print(f'{hour}:{minute}:{sec}')
else:
    print(f"Вы ввели слишком большое значением, введите значение до {time_max}")
