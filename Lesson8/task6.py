"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
from abc import ABC, abstractmethod

"""
Использовано знаний:
Абстрактный класс
@property
@property.setter
setattr
Наследование
Класс исключений
@Static
"""
class AnyError(Exception):
    def __init__(self, text):
        self.text = text


class CheckValues():
    """
    Класс для проверки входных данных
    """
    @staticmethod
    def integer(input_string: str, cls=0, param_name=0) -> int:
        """
        Метод запрашивает число и проверяет соответствие строки числу, если успех, то возвращает int, иначе продолжает запрашивать. Если задан класс и имя параметра, то пишет аттрибут сразу в класс.
        :param x:
        :cls : class
        :return: int
        """
        while True:
            inpt_data = input(f'{input_string}\n')
            try:
                if inpt_data.isdigit():
                    if cls and param_name:
                        setattr(cls, param_name, int(inpt_data))  # демонстрация знаний
                        break
                    else:
                        return int(inpt_data)
                else:
                    raise AnyError("Ошибка типа данных! Надо ввести число!")
            except AnyError as mr:
                print(mr)


class EquipmentInterface(ABC):
    @abstractmethod
    def set_property(self, eq_type: str) -> None:
        pass


class Warehouse():
    def __init__(self, name):
        self.name = name
        self.rooms = dict()          #Потом будем хранить там данные об оборудовании в формате {'комната 1': [Copier, Printer, Scanner]}

    def add_equipment(self, room: str, equipment):
        """
        Метод принимает на склад (сразу в комнаты) оборудование
        :param room: str
        :param equipment: class
        :return: None
        """
        if self.rooms.get(room) == None:
            self.rooms[room] = [equipment]
        else:
            self.rooms[room].append(equipment)

    def show_equipment(self):
        """
        Метод выводит все, то лежит на складе и в каких комнатах
        :return: None
        """
        for key, values in self.rooms.items():
            print(f'\nВ комнате "{key}" находятся:')
            i = 1
            for itm in values:
                print(f'{i}.{itm.eq_type} {itm.name} в количестве {itm.qnty} шт., цвет: {itm.color}')
                i += 1



class Equipment(EquipmentInterface):
    def __init__(self, name: str, eq_type: str, qnty: int, color: str, ):
        if name=='':
            self.set_property(eq_type)
        else:
            self.__name = name
            self.type = eq_type
            self.qnty = qnty
            self.color = color

    @property
    def name(self):
        """
        Добавлен для демонстрации возможностей Python
        :param name:
        :return:
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Добавлен для демонстрации возможностей Python
        :param name:
        :return:
        """
        self.__name = name

    def set_property(self, eq_type: str):
        """
        Метод запрашивает данные об оборудовании у пользователя
        :param type: str
        :return: None
        """
        self.name = input(f'введите наименование для {eq_type}\n')
        # self.qnty = CheckValues.integer('введите количество')
        CheckValues.integer('введите количество', self, 'qnty')
        color = input('введите цвет\n')
        setattr(self, 'color', color)                                                       #демонстрация знаний
        self.eq_type = eq_type


class Scanner(Equipment):
    def __init__(self, name='', eq_type='сканер', qnty='', color='', scanspeed=''):
        super().__init__(name, eq_type, qnty, color)
        if scanspeed == '':
            scanspeed = CheckValues.integer('Введите скорость распознавания:')
        self.scanspeed = scanspeed


class Printer(Equipment):
    def __init__(self, name='', eq_type='принтер', qnty='', color='', printspeed=''):
        super().__init__(name, eq_type, qnty, color)
        if printspeed == '':
            printspeed = CheckValues.integer('Введите скорость печати:')
        self.printspeed = printspeed


class Copier(Equipment):
    def __init__(self, name='', eq_type='копир', qnty='', color='', copyspeed=''):
        super().__init__(name, eq_type, qnty, color)
        if copyspeed == '':
            copyspeed = CheckValues.integer('Введите скорость копирования:')
        self.copyspeed = copyspeed




if __name__ == '__main__':
    warehouse = Warehouse('Основной склад Дежьих пожито')

    while True:
        room = input('Введите комнату (стоп для выхода):\n')
        if room.lower() == 'стоп':
            exit()
        eq_type = input('Введите тип устройства:\n').lower()
        if eq_type == 'принтер':
            warehouse.add_equipment(room, Printer())
        elif eq_type == 'сканер':
            warehouse.add_equipment(room, Scanner())
        elif  eq_type == 'копир':
            warehouse.add_equipment(room, Copier())

        warehouse.show_equipment()