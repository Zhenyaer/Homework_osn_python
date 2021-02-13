class Data:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def str_to_int(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        date_int = [day, month, year]
        return date_int[0], date_int[1], date_int[2]

    @staticmethod
    def validation(date_str):
        day, month, year = map(int, date_str.split('-'))
        if 0 < day < 32 and 0 < month < 13 and 0 < year < 2100:
            return f'Введены корректные данные'
        else:
            return f'Введены неверные данные'


date_1_i = Data.str_to_int('13-02-2021')
print(date_1_i)
date_1_p = Data.validation('13-02-2021')
print(date_1_p)

date_2_i = Data.str_to_int('13-13-2021')
print(date_2_i)
date_2_p = Data.validation('13-13-2021')
print(date_2_p)
