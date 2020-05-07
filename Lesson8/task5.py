"""
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

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

class Equipment:
    def __init__(self, name: str, eq_type: str, qnty: int, color: str, ):
        if name=='':
            self.set_property(eq_type)
        else:
            self.name = name
            self.type = eq_type
            self.qnty = qnty
            self.color = color

    def set_property(self, eq_type):
        """
        Метод запрашивает данные об оборудовании у пользователя
        :param type: str
        :return: None
        """
        self.name = input(f'введите наименование для {eq_type}\n')
        self.qnty = input('введите количество\n')
        self.color = input('введите цвет\n')
        self.eq_type = eq_type


class Scanner(Equipment):
    def __init__(self, name='', eq_type='сканер', qnty='', color='', scanspeed=''):
        super().__init__(name, eq_type, qnty, color)
        if scanspeed == '':
            scanspeed = input('Введите скорость распознавания:\n')
        self.scanspeed = scanspeed


class Printer(Equipment):
    def __init__(self, name='', eq_type='принтер', qnty='', color='', printspeed=''):
        super().__init__(name, eq_type, qnty, color)
        if printspeed == '':
            printspeed = input('Введите скорость печати:\n')
        self.printspeed = printspeed


class Copier(Equipment):
    def __init__(self, name='', eq_type='копир', qnty='', color='', copyspeed=''):
        super().__init__(name, eq_type, qnty, color)
        if copyspeed == '':
            copyspeed = input('Введите скорость копирования:\n')
        self.copyspeed = copyspeed




if __name__ == '__main__':
    warehouse = Warehouse('Основной склад')
    while True:
        room = input('Введите комнату (стоп для выхода):\n')
        if room.lower() == 'стоп':
            exit()
        while True:
            eq_type = input('Введите тип устройства:\n').lower()
            if eq_type == 'принтер':
                warehouse.add_equipment(room, Printer())
            elif eq_type == 'сканер':
                warehouse.add_equipment(room, Scanner())
            elif  eq_type == 'копир':
                warehouse.add_equipment(room, Copier())
            else:
                print('Данный тип устройств отсутствует в БД')


        warehouse.show_equipment()