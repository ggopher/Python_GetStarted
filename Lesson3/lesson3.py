"""
my_list = [1, 2, 3, 4, 5]
try:
    a = my_list[10]/0
except ZeroDivisionError:
        print('Овцебык')
except IndexError:
        print('Овцебык индекс')
#except Exception:
#        print('Овцебык Все ошибки')
finally:
        print('Овцебык в любом случае')
"""

def my_sum(tmp: list):
    return tmp[0] + my_sum(tmp[1:]) if tmp else 0
print(my_sum([2,3,4]))
print('\n\n\n\n')


def my_sum(*args):
    return args[0] + my_sum(*args[1:]) if args else 0
print(my_sum(2,3,4,5))
print('\n\n\n\n')



tup = (my_sum)



def my_temp(x, y, z, *args, **kwargs):
    print(x, y, z)
    print(args)
    for key, value in kwargs.items():
        print(f'{key} --- {value}')
    return 0
print(my_temp(1, 2, 3, 4, 5, 6, hello=22, arg=33))
print('\n\n\n\n')


def my_test(a:int, b:int)-> int:
    """
    Эта функция для математиков
    :param a: int
    :param b: int
    :return: int
    """
    result = (a + b) ** a
    return result
a = my_test(2,3)
print(a)

def square(a):
    return  a ** 2
def my_map(func, tmp):
    result = []
    for itm in tmp:
        result.append(func(itm))
    return result

def my_map2(func, tmp):
    for itm in tmp:
        print("one")
        yield func(itm)
        print("two")

my_list = [1, 2, 3, 4, 5]
new_list = []
new_list = my_map2(square, my_list)
for itm in new_list:
    print(itm)
print("\n\n\n\n")
a = list(map(lambda x: x **2, my_list))
print(a)


b = (lambda  x, y, z: x ** 2 + y ** 2 + z ** 2) (333, 322, 77)
print(b)