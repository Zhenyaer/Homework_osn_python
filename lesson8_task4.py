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

    def __str__(self):
        return f'\nНаименование: {self.name}\nМодель: {self.model}\n' \
               f'Стоимость: {self.cost}$\nКоличество: {self.quantity}\n'


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


warehouse_info = WarehouseOfficeEquipment('ул. Пушкина, д.17, к.4', 715, 3)
print(warehouse_info)

printer = Printer('Принтер', 'HP420', 580, 93, 'А4, А3')
print(printer)

scanner = Scanner('Сканер', 'Epson Perfection V19', 800, 47, '600х600')
print(scanner)

copier = Copier('Ксерокс', 'Xerox 3310', 250, 174, 750)
print(copier)
