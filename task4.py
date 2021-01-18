# task4
'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:
    '''Базовый класс для автомобилей'''
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police: bool = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        return print(f'Машина повернула {direction}')

class TownCar(Car):
    '''Обычный легковой городской автомобиль'''

class SportCar(Car):
    '''Гоночный автомобиль'''

class WorkCar(Car):
    '''Грузовой автомобиль'''

class PoliceCar(Car):
    '''Полицейский автомобиль'''

