# task5
'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Пора поставить на {self.title} подпись ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Проведем линии на {self.title} карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'Порисуем на {self.title} маркером')

contract = Pen('договор')
diagramm = Pencil('диаграмма')
drawing = Handle('холст')

contract.draw()
diagramm.draw()
drawing.draw()
