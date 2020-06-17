"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random
array = [i for i in range(0, 51)]
random.shuffle(array)
print(array)


def mg_group(a, mg_left, part, mg_right):
    if mg_left >= mg_right: return None
    if part < mg_left or mg_right < part: return None
    itm = mg_left
    for j in range(part + 1, mg_right + 1):  # вторая группа
        for i in range(itm, j):  # цикл первой группы
            if a[j] < a[i]:
                r = a[j]
                # Упорядочиваем
                for k in range(j, i, -1):
                    a[k] = a[k - 1]
                a[i] = r
                itm = i  # Продолжаем в первой группе
                break  # Идем к следующему куску

def mg_sort(a):
    if len(a) < 2: return None
    k = 1
    while k < len(a):
        g = 0
        while g < len(a):
            z = g + k + k - 1  # конечный элемент
            r = z if z < len(a) else len(a) - 1  # конечная группа
            mg_group(a, g, g + k - 1, r)  # Само слияние
            g += 2 * k
        k *= 2
mg_sort(array)
print(array)