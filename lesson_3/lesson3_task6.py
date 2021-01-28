def int_func(text):
    # Возвращает введенное слово с большой буквы
    return text.title()


user_input = input('Введите слово маленькими буквами: ')
print(int_func(user_input))
