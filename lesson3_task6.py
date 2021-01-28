def int_func():
    # Возвращает введенные слова с заглавных букв
    text = ''
    check_ascii = []
    flag = True
    words = input('Введите слова маленькими латинскими буквами через пробел: ').split()
    # Проверяет что были введены маленькие латинские буквы по кодировке ASCII
    for word in words:
        check_ascii += word
        for letter in check_ascii:
            if 97 <= ord(letter) <= 122:
                continue
            else:
                flag = False
    # Меняет первую букву каждого слова на заглавную
    if flag:
        for word in words:
            text += word.title()
            text += ' '
        return text
    else:
        return 'Нужно вводить только маленькие латинские буквы!'


print(int_func())
