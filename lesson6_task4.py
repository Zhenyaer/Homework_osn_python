class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.color.title()} {self.name.title()} поехала'

    def stop(self):
        return f'{self.color.title()} {self.name.title()} остановилась'

    def turn(self, direction):
        return f'{self.color.title()} {self.name.title()} повернула {direction}'

    def show_speed(self):
        return f'Машина едет со скоростью {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость превышена! Машина едет со скоростью {self.speed} км/ч!' \
                   f'Для вашей безопасности снизьте скорость до 60 км/ч!'
        else:
            return f'Машина едет со скоростью {self.speed} км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость превышена! Машина едет со скоростью {self.speed} км/ч!'\
                   f'Для вашей безопасности снизьте скорость до 60 км/ч!'
        else:
            return f'Машина едет со скоростью {self.speed} км/ч'


class PoliceCar(Car):
    pass


car_town = TownCar(80, 'красная', 'хонда')
print(f'\n{car_town.go()} \n{car_town.stop()} \n{car_town.turn("в сторону Смоленска")} \n{car_town.show_speed()}')

car_sport = SportCar(100, 'зеленая', 'хонда')
print(f'\n{car_sport.go()} \n{car_sport.stop()} \n{car_sport.turn("направо")} \n{car_sport.show_speed()}')

car_work = WorkCar(50, 'белая', 'газель')
print(f'\n{car_work.go()} \n{car_work.stop()} \n{car_work.turn("на юг")} \n{car_work.show_speed()}')

car_police = PoliceCar(50, 'бело-синяя', 'гранта', True)
print(f'\n{car_police.go()} \n{car_police.stop()} \n{car_police.turn("на юг")} \n{car_police.show_speed()}')
