"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
class Warehouse():
    def __init__(self, name):
        self.name = name
        rooms = dict()          #Потом будем хранить там данные об оборудовании в формате {'комната 1': [Copier, Printer, Scanner]}

class Equipment:
    def __init__(self, name: str, type: str, qnty: int,  color: str,):
        self.name = name
        self.type = type
        self.qnty = qnty
        self.color = color


class Scanner(Equipment):
    def __init__(self, name: str, type: str, qnty:int, color: str, scanspeed: str):
        self.scanspeed = scanspeed
        super().__init__(name, type, qnty, color)

class Printer(Equipment):
    def __init__(self, name: str, type: str, qnty:int, color: str, printspeed: str):
        self.printspeed = printspeed
        super().__init__(name, type, qnty, color)

class Copier(Equipment):
    def __init__(self, name: str, type: str, qnty:int, color: str, copyspeed: str):
        self.copyspeed = copyspeed
        super().__init__(name, type, qnty, color)



if __name__ == '__main__':
    scanner = Scanner('Сканер 1', 'Сканер беспроводной', 1, 'Белый', "лист в минуту")
    print(scanner.__dict__)

    printer = Printer('Принтер', 'Принтер во второй комнате', 2, 'Серый', "10 листов в минуту")
    print(printer.__dict__)

    copier = Copier('Копир', 'Копир проводной', 3, 'Желтый', "15 листов в минуту")
    print(copier.__dict__)