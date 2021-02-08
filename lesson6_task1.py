from time import sleep


class TrafficLight:
    __color = ('красный', 'желтый', 'зеленый')

    def running(self):
        for i in range(len(TrafficLight.__color)):
            print(f'Загорелся {TrafficLight.__color[i]} свет')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(4)


traffic_manage = TrafficLight()
traffic_manage.running()
