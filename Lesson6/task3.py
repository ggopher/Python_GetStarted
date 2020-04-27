"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например,
    {"wage": wage,
    "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    #Здесь пустые переменные нужны на случай, если кто-то забудет запустить конструктор __init__ в дочерних классах. Мы ведь пишем универсальные классы так, чтобы и другие потом пользовались.
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name: str, surname: str, position: str, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_full_name(self):
        """
        Метод возвращает имя сотрудника
        :return: str
        """
        return self.name

    def get_total_income(self):
        """
        Метод возвращает итоговую зарплату с бонусами
        :return: float
        """
        return float(sum(self._income.values()))


inc = {'wage': 20000, 'bonus': 3000}

pos = Position('Имя', 'Фамилия', 'Кладовщик', inc)
print(f'Имя сотрудника: {pos.get_full_name()}')
print(f'Итого зп: {pos.get_total_income()}')


pos._income = {'wage': 10000, 'bonus': 5000}
print(f'Итого программно измененная зп: {pos.get_total_income()}')