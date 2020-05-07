"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

from abc import ABC
import datetime

class Data(ABC):
    def __init__(self, data: str):
        self.data = data

    @staticmethod
    def validate(date: str) -> bool:
        """
        Валидирует дату в строке на корректность данных
        :param date: str
        :return: bool
        """
        date_format = '%d-%m-%Y'
        try:
            datetime.datetime.strptime(date, date_format)
            return True
        except ValueError:
            print('Введена неверная дата. Формат дд-мм-гггг')
            return False

    @classmethod
    def extract(cls, string: str) -> list:
        """
        Принимает дату строкой и разбирает ее на int в списке
        :param string: str
        :return: list
        """
        if Data.validate(string):
            date = string.split('-')
            date[0] = int(date[0])
            date[1] = int(date[1])
            date[2] = int(date[2])
            return date
        else:
            return None

date = "21-12-1967"

print(Data.extract(date))
# print(Data.validate(date))

