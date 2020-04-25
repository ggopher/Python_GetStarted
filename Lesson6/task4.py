"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

class Car:

    def __init__(self, speed: int, name: str, color: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        """
        Выводим сообщение
        :return: None
        """
        print(f'{self.name} едет со скоростью {self.speed}')

    def go(self):
        """
        Выводим сообщение
        :return: None
        """
        print('Машина едет')
    def stop(self):
        """
        Выводим сообщение
        :return: None
        """
        print('Машина остановилась')
    def turn(self, direction):
        """
        Выводим сообщение
        :return: None
        """
        print(f'Машина повернула {direction}')


class Towncar(Car):
    def __init__(self, name: str, color: str):
        super().__init__(60, name, color, False)

    def show_speed(self):
        if self.speed > 60:
            speed = f'{self.speed} (Превышение!!!)'
        else:
            speed = self.speed
        print(f'{self.name} едет со скоростью {speed}')

class Workcar(Car):
    def __init__(self, name: str, color: str):
        super().__init__(40, name, color, False)

    def show_speed(self):
        if self.speed > 40:
            speed = f'{self.speed} (Превышение!!!)'
        else:
            speed = self.speed
        print(f'{self.name} едет со скоростью {speed}')

class Policecar(Car):
    def __init__(self, name: str, color: str):
        super().__init__(100, name, color, True)

class Sportcar(Car):
    def __init__(self, name: str, color: str):
        super().__init__(180, name, color, False)

towncar = Towncar('Городская машинка', 'Белая')
towncar.show_speed()
towncar.speed = 70
towncar.turn('направо')
towncar.show_speed()
print(towncar.__dict__)

print('\n#################\n')

policecar = Policecar('Полицейская машина', 'Полосатая')
policecar.show_speed()
policecar.turn('налево')
print(policecar.__dict__)

print('\n#################\n')

sportcar = Sportcar('Спортивная машина', 'Красная')
sportcar.show_speed()
sportcar.turn('налево')
print(sportcar.__dict__)

print('\n#################\n')

workcar = Workcar('Рабочая машина', 'Черная')
workcar.show_speed()
workcar.speed = 80
workcar.turn('налево')
workcar.show_speed()
print(workcar.__dict__)
