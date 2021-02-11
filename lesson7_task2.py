from abc import ABC, abstractmethod


class Clothes(ABC):
    total = 0

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def abstract(self):
        return 'Абстрактный метод'


class Coat(Clothes):
    def expenditure(self):
        exp = float('{:.1f}'.format(self.param / 6.5 + 0.5))
        Clothes.total += exp
        return f'Для пошива одного пальто необходимо {exp} м2 ткани'

    def abstract(self):
        return 'Абстрактный метод пальто'


class Suit(Clothes):
    @property
    def expenditure(self):
        exp = float('{:.1f}'.format(self.param * 2 + 0.3))
        Clothes.total += exp
        return f'Для пошива одного костюма необходимо {exp} м2 ткани'

    def abstract(self):
        return 'Абстрактный метод костюма'


coat = Coat(54)
print(coat.expenditure())

suit = Suit(1.87)
print(suit.expenditure)

print(f'Для пошива одного костюма и одного пальто необходимо {Clothes.total} м2 ткани')
