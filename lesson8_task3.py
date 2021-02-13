class Exc:
    def __init__(self, user):
        self.user = list(user)

    def validation(self):
        try:
            self.user = [int(i) for i in self.user]
            return 'В списке только числа'
        except ValueError:
            return 'В списке не только числа'


user_input = list(input('Введите числа в список через пробел: ').split())
ex = Exc(user_input)
print(ex.validation())
