from abc import ABC, abstractmethod
import time
class MyInterface(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def turn_on(self, x: int, y: int) -> float:
        pass

    @abstractmethod
    def turn_off(self, x: int) -> None:
        pass
    def say(self):
        print(self.name)



class MyCls(MyInterface):
    def __init__(self, name):
        self.one = '22222'
        self.__name = name
        self.__name2 = ''
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data):
        print(data)
        self.name2 = data

    def turn_on(self, x: int, y: int) -> float:
        pass

    def turn_off(self, x: int) -> None:
        pass

    def __str__(self):
        return self.name
    def __add__(self, other):       #переопределение оператора сложения
        return MyCls(self.name.split(' ')[0] + other.name.split(' ')[-1])

    def __eq__(self, other):
        return self.name == other.name
    def __call__(self, x, y):
        tmp = x ** y
        return f'{self.name} -- {tmp}'



def my_deco(func):
    def wrap(*args, **kwargs):
        print(func.__name__)
        tmp = func(*args, **kwargs)
        print('END')
        return f'<p>{tmp}</p>'
    return wrap

@my_deco
def test1(text):
    return f'<span> {text} </span>'

# @my_deco
def test2():
    print('test2')



if __name__ == '__main__':

    tmp = MyCls('Some name')
    tmp_1 = MyCls('Some @1')
    tmp2 = MyCls('Some @2')
    tmp3 = tmp + tmp2
    print(tmp3)
    # tmp.name = 'name 2'
    # tmp.say()
    # some = 'sdfsdf'
    # print(str(tmp))
    # print(tmp.name2)

    print(tmp == tmp_1)
    some = tmp(5,2)
    print()


# print(test1('somete'))