import random
import time
class Wolf:
    def __init__(self, eyes):
        self.eyes = eyes

    def moon(self):
        print('Воу воу')
        return True


class Homo:
    age = 0
    sex = random.choice(('m','f'))
    weight = 3400
    name = ''
    __population = 0 #protected
    def __init__(self, name: str):
        self.name = name
        Homo.__population += 1
    def ask(self):
        now = int(time.time())
        if now & 1:
            self.moon()
        else:
            print('WHO AM I')
        print(f'My name is {self.name}')
    def new_age(self):
        self.age += 1
    def get_population(self):
        return self.__population



class HomoSap(Homo):
    def __init__(self, color, *args, **kwargs):
        self.color = color
        super().__init__(*args, **kwargs)


class Werevolf(HomoSap, Wolf):
        def __init__(self, color, eyes, *args, **kwargs):
            super().__init__(self, color, *args, **kwargs)
            Wolf.__init__(self, eyes)       #Второй наследуемый надо инициализировать явно

        def ask(self):
            now = int(time.time())
            if now & 1:
                self.moon()
            else:
                print('WHO AM I')
            print(f'My name is {self.name}')

aaa = Werevolf(eyes='green', color='blue')

we = Wolf('sdf')

vasya = Homo('Василий')
petya = Homo('Петр')
vasya.ask()
Homo('sadf').ask()
petr = HomoSap('red', name='Новый Петр')