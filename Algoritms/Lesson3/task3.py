"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randint
array = [randint(0, 20) for _ in range(5)]
itm = min_pos = max_pos = 0
min = max = array[0]

for itm in range(len(array)): #код конечно корявый, но так специально,
                              # чтобы не задействовать функции и методы высокого уровня типа .index
    if array[itm] > max:
        max = array[itm]
        max_pos = itm
    elif array[itm] < min:
        min = array[itm]
        min_pos = itm

print(f'Старый массив: {array}\n')
array[min_pos] = max
array [max_pos] = min
print(f'Новый массив: {array}\n min = {min}, max = {max}')