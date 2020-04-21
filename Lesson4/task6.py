from itertools import cycle, count
from time import sleep
"""
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

#ЗАДАНИЕ А:
start_digit = 0
for el in count(start_digit):
    print(el)
    sleep(0.1)


#ЗАДАНИЕ Б:
times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for itm in cycle(times):
    print(itm)
    sleep(0.1)
