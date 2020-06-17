"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


from random import randint
array = [randint(0, 20) for _ in range(10)]
sum = itm = 0
min = max = array[0]

for itm in range(len(array)): #код конечно корявый, но так специально,
                              # чтобы не задействовать функции и методы высокого уровня типа .index
    if array[itm] > max:
        max = array[itm]
    elif array[itm] < min:
        min = array[itm]
    sum += array[itm]
sum -= max + min
print(f'Новый массив: {array}\n min = {min}, max = {max} sum = {sum}')

