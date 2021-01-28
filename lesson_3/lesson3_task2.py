def user_info(name, surname, age, town, mail, phone_number):
    return f'{name.title()} {surname.title()} {age} {town.title()} {mail} {phone_number}'


print(user_info(name=input('Введите ваше имя: '), surname=input('Введите вашу фамилию: '),
                town=input('Введите ваш город: '), mail=input('Введите ваш адрес почты: '),
                age=int(input('Введите ваш возраст: ')), phone_number=int(input('Введите ваш номер телефона: '))))
