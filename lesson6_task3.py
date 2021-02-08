class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


pos = Position('Petr', 'Ivanov', 'Senior Python', 180000, 45000)
print(pos.get_full_name(), pos.get_total_income())

pos = Position('Aleksandr', 'Sidorov', 'Middle Python', 135000, 30000)
print(pos.get_full_name(), pos.get_total_income())
