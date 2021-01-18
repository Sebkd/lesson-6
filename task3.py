# task3
'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def get_income(self):
        return self._income()

class Position(Worker):

    def get_full_name(self):
        return str(self.surname + ' ' + self.name)

    def get_total_income(self):
        return Worker.get_income(self)

docker = Position('Andre', 'Grey', 'docker', {'wage': 2000, 'bonus': 500})
print(docker.get_full_name())
print(docker.get_total_income())