"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random
array = [2 * i for i in range(0, 11)]
random.shuffle(array)
print(array)

import random

def rnd_take(num, array):
    pivot = random.choice(array)

    less = [item for item in array if item < pivot]
    if len(less) > num:
        return rnd_take(num, less)
    num -= len(less)
    numeq = array.count(pivot)
    if numeq > num:
        return pivot
    num -= numeq
    above = [item for item in array if item > pivot]
    return rnd_take(num, above)

def median(array):
    if len(array) % 2:
        return rnd_take(len(array) // 2, array)

    else:
        lt  = rnd_take((len(array) - 1) // 2, array)
        rt = rnd_take((len(array) + 1) // 2, array)

        return (lt + rt) / 2


median = median(array)
print(f'Медиана массива: {median}')