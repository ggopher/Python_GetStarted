"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random
#Задание a
array = [i for i in range(-100, 100)]
random.shuffle(array)
print(array)


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
        print(array)
    return array

print(bubble_sort(array))

#Задание b

array = [i for i in range(-100, 100)]
random.shuffle(array)



print(f'Вариант b, улучшенный\n {array}')


def bubble_sort_optimized(array):
    num = len(array)
    while (True):
        n = 0
        for i in range(num - 1):
            ii = num - i - 1
            if array[ii] > array[ii - 1]:
                array[ii], array[ii - 1] = array[ii - 1], array[ii]
                n += 1
        if n == 0:
            break
    print(array)
    return array

print(bubble_sort_optimized(array))

