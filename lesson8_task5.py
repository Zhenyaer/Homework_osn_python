import datetime


class WarehouseOfficeEquipment:
    # Описывает склад оргтехники
    def __init__(self, address, square, floor):
        self.address = address
        self.square = square
        self.floor = floor

    def __str__(self):
        return f'Склад оргтехники находится по адресу {self.address} ' \
               f'и занимает {self.floor} этажа общей площадью {self.square} м2.'


class OfficeEquipment:
    # Базовый класс всей оргтехники храняйщейся на складе
    def __init__(self, name, model, cost, quantity):
        self.name = name
        self.model = model
        self.cost = cost
        self.quantity = quantity
        self.inform = {'Наименование': self.name, 'Модель': self.model,
                       'Стоимость': self.cost, 'Количество': self.quantity}
        self.store_transfer = []
        self.store_reception = []

    def __str__(self):
        return f'\nНаименование: {self.name}\nМодель: {self.model}\n' \
               f'Стоимость: {self.cost}$\nКоличество: {self.quantity}\n'

    def reception(self):
        self.store_reception.append(self.inform)
        return f'{self.inform} было принято на склад {datetime.datetime.now()}'

    def transfer(self, department):
        self.department = department
        self.store_transfer.append(self.inform)
        return f'{self.inform} было передано в {self.department}'


class Printer(OfficeEquipment):
    def __init__(self, name, model, cost, quantity, paper_size):
        super().__init__(name, model, cost, quantity)
        self.paper_size = paper_size

    def __str__(self):
        return f'Наименование: {self.name}\nМодель: {self.model}\n' \
               f'Стоимость: {self.cost}$\nКоличество: {self.quantity}\nРаботает с форматами: {self.paper_size}\n'


class Scanner(OfficeEquipment):
    def __init__(self, name, model, cost, quantity, dpi):
        super().__init__(name, model, cost, quantity)
        self.dpi = dpi

    def __str__(self):
        return f'Наименование: {self.name}\nМодель: {self.model}\n' \
               f'Стоимость: {self.cost}$\nКоличество: {self.quantity}\nРазрешение: {self.dpi} dpi\n'


class Copier(OfficeEquipment):
    def __init__(self, name, model, cost, quantity, max_load):
        super().__init__(name, model, cost, quantity)
        self.max_load = max_load

    def __str__(self):
        return f'Наименование: {self.name}\nМодель: {self.model}\n' \
               f'Стоимость: {self.cost}$\nКоличество: {self.quantity}\nМаксимальная загрузка: {self.max_load} листов\n'


printer_transfer = OfficeEquipment('Принтер', 'HP420', 580, 12)
print(printer_transfer.transfer('отдел снабжения.'))

printer_reception = OfficeEquipment('Принтер', 'HP420', 580, 180)
print(printer_reception.reception())
