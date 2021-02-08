class Road:
    def __init__(self, length, width):
        # длина и ширина дорожного полотна (м)
        self._length = length
        self._width = width

    def mass(self):
        # удельная масса (кг/(м2*см)) и толщина (см)
        m = 25
        width = 10
        m_full = self._length * self._width * m * width / 1000
        print(f'Для строительства дороги потребуется {int(m_full)} тонн асфальта.')


road_mass = Road(10000, 25)
road_mass.mass()
