class Clothes:
    def __init__(self, v=0.0, h=0.0):
        self.v = v
        self.h = h

    def res_expenditure(self):
        res_exp = self.v / 6.5 + 0.5 + self.h * 2 + 0.3
        return f'Для пошива одного пальто и одного костюма необходимо {res_exp:.1f} м2 ткани'


class Coat(Clothes):
    def expenditure(self):
        exp = self.v / 6.5 + 0.5
        return f'Для пошива одного пальто необходимо {exp:.1f} м2 ткани'


class Suit(Clothes):
    @property
    def expenditure(self):
        exp = self.v * 2 + 0.3
        return f'Для пошива одного костюма необходимо {exp:.1f} м2 ткани'


coat = Coat(54)
print(coat.expenditure())

suit = Suit(1.87)
print(suit.expenditure)

clothes = Clothes(54, 1.87)
print(clothes.res_expenditure())
