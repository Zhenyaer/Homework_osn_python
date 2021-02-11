class Cell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        return f'Сумма клеток равна: {self.cell_count + other.cell_count}'

    def __sub__(self, other):
        return f'Разность клеток равна: {self.cell_count - other.cell_count}'

    def __mul__(self, other):
        return f'Произведение клеток равно: {self.cell_count * other.cell_count}'

    def __truediv__(self, other):
        return f'Деление клеток равно: {self.cell_count // other.cell_count}'

    def make_order(self, num):
        res = ''
        for i in range(int(self.cell_count / num)):
            res += '#' * num + '\n'
        res += '#' * (self.cell_count % num) + '\n'
        return res


cell_1 = Cell(15)
cell_2 = Cell(2)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(cell_1.make_order(4))
