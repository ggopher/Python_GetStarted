"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod
import time
class MyInterface(ABC):
    @property
    @abstractmethod
    def consumption(self) -> int:
        pass

    @consumption.setter
    @abstractmethod
    def consumption(self) -> int:
        pass


class Garment(MyInterface):
    def __init__(self, name, type, size):
        self.__name = name
        self.type = type
        self.__size = size  #размер, вместо V, или H.
        self.consumption = 0

    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, consumption):
        """
        Определяем расход ткани в зависимости от типа класса.
        :param consumption:
        :return: int
        """
        if self.type=='Пальто':
            self.__consumption = self.__size/6.5 + 0.5
        elif self.type=='Костюм':
            self.__consumption = 2 * self.__size + 0.3
        else:
            self.__consumption =  0
            print('Неправильно задан тип, или размер одежды')


garm = Garment('Одежка1', 'Пальто', 14)
garm2 = Garment('Одежка2', 'Костюм', 14)

print(garm.consumption)
print(garm2.consumption)