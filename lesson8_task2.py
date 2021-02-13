class Div:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def div(self):
        try:
            res = self.x / self.y
            return res
        except ZeroDivisionError:
            return 'На 0 делить нельзя!'


ex = Div(5, 4)
print(ex.div())

ex = Div(5, 0)
print(ex.div())
