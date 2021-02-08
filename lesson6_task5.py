class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки. {self.title.title()} - главный инструмент.'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки. {self.title.title()} - главный инструмент.'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки. {self.title.title()} - главный инструмент.'


stat = Stationery('')
print(stat.draw())

pen = Pen('pen-ручка')
print(pen.draw())

pencil = Pencil('карандаш')
print(pencil.draw())

handle = Handle('handle-ручка')
print(handle.draw())
