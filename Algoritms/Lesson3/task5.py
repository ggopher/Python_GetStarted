"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
"""
from random import randint
array = [randint(-20, 10) for _ in range(20)]
itm = max = 0
max_pos = -1

for itm in range(len(array)): #код конечно корявый, но так специально, чтобы не задействовать функции и методы высокого уровня типа .index
    if array[itm] < 0 and max_pos == -1 or 0 > array[itm] > max:
        max = array[itm]
        max_pos = itm
    elif 0 > array[itm] > max:/
        max = array[itm]
        max_pos = itm

print(f'Новый массив: {array}\n max_pos = {max_pos}, max = {max}')

