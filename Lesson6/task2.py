"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""

class Road:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def squaremeter(self, mass: int, cm: int):
        """
        Данный метод рассчитывает необходимую массу сырья на заданную толщину и заданную плотность материала.
        :param mass: int
        :param cm:  int
        :return: float
        """
        return float(self._length * self._width * (mass / 1000) * cm)            #Ответ в тоннах

rd = Road(20, 5000)
print(rd.squaremeter(25, 5))