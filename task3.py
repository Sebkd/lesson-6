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


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super(Position, self).__init__(name, surname, position, income)

    def get_full_name(self):
        return str(self.surname + ' ' + self.name)

    def get_total_income(self):
        return (int(self._income.get('wage')) + int(self._income.get('bonus')))


docker = [Position(f'{input("Введите имя: ")}', f'{input("Введите фамилию: ")}',
                             f'{input("Введите должность: ")}',
                             {'wage': f'{input("Введите оклад: ")}', 'bonus': f'{input("Введите премию: ")}'})
                     for count in range(1)]

for count in range(len(docker)):
    print(f"getattr(docker[count], 'name'): {getattr(docker[count], 'name')}\n",
          f"getattr(docker[count], 'surname'): {getattr(docker[count], 'surname')}\n",
          f"getattr(docker[count], 'position'): {getattr(docker[count], 'position')}\n",
          f"hasattr(docker[count], 'income'):{hasattr(docker[count], 'income')}\n")
    print(f'Полное имя работника - {docker[count].get_full_name()}')
    print(f'Его зарплата: {docker[count].get_total_income()}')
