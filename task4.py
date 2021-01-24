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
import time
import random


class Car:
    '''Базовый класс для автомобилей'''
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police: bool = is_police

    def show_speed(self):
        return print(f' Скорость автомобиля {self.speed}')

    def go(self):
        return print(' Автомобиль двигается прямо')

    def stop(self):
        return print(' Автомобиль остановился')

    def turn(self, direction):
        return print(f' Автомобиль повернул {direction}')


class TownCar(Car):
    '''Обычный легковой городской автомобиль'''
    def show_speed(self):
        if int(self.speed) > 60:
            return print(' Внимание! Скорость автомоибля превышена, должно быть менее 60')
        else:
            return print(f' Скорость автомобиля {self.speed}')


class SportCar(Car):
    '''Гоночный автомобиль'''
    pass


class WorkCar(Car):
    '''Грузовой автомобиль'''
    def show_speed(self):
        if int(self.speed) > 40:
            return print(' Внимание! Скорость автомоибля превышена, должно быть менее 40')
        else:
            return print(f' Скорость автомобиля {self.speed}')


class PoliceCar(Car):
    '''Полицейский автомобиль'''
    pass


def show_attr(auto_obj):
    print(f" Cкорость: {getattr(auto_obj, 'speed')}\n",
          f"Цвет: {getattr(auto_obj, 'color')}\n",
          f"Название модели: {getattr (auto_obj, 'name')}\n",
          f"Это полиция? -  {getattr (auto_obj, 'is_police')}\n")


with open(r'task4.txt', encoding = 'utf-8') as f_obj:
    lines = f_obj.readlines()

auto = []

for count, line in enumerate(lines):
    type_car, speed, color, name, is_police = line.split()
    if type_car == 'town_car':
        auto.append(TownCar(speed, color, name, is_police))
    elif type_car == 'sport_car':
        auto.append(SportCar(speed, color, name, is_police))
    elif type_car == 'work_car':
        auto.append(WorkCar(speed, color, name, is_police))
    elif type_car == 'police_car':
        auto.append(PoliceCar(speed, color, name, is_police))
    else:
        continue


while True:
    for count, line in enumerate(auto):
        random_move = random.randint(1, 3)
        if random_move == 1:
            setattr(auto[count], 'speed', 0)
            auto[count].stop()
        else:
            setattr(auto[count], 'speed', random.randint(5, 90))
        if random_move == 2:
            auto[count].go()
        elif random_move == 3:
            auto[count].turn('налево' if random.randint(1, 2) == 1 else 'направо')
        auto[count].show_speed()
        show_attr(auto[count])
        time.sleep(4)
