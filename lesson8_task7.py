class ComplexNums:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f'Сумма чисел равна = {self.x + other.x} + {self.y + other.y}*i'

    def __mul__(self, other):
        return f'Произведение чисел равно = {self.x * other.x - self.y * other.y} + ' \
               f'{self.x * other.y + self.y * other.x}*i'


n_1 = ComplexNums(5, 6)
n_2 = ComplexNums(7, 8)
print(n_1 + n_2)
print(n_1 * n_2)
