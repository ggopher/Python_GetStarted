"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

list = [1, 2, 2, 2, 3, 4, 2, 1, 8, 7, 6, 9, 4, 2, 4, 63, 634, 7, 12, 6, 12]
new_list = []
# new_list = [itm for itm in list if new_list.index(itm)]

def generate(list: list):
    """
    Функция, добавляющая значения, которые больше предыдушего, в новый список.
    :param list: list
    :return: generator
    """
    prev_item = 0
    for item in list:
       if item>prev_item:
            new_list.append(item)
       prev_item = item
    yield item

final = generate(list) #Создали генератор
for i in final:        #Быстренько прогоняем генератор, т.к. конкретно в этой задаче пошаговое управление по сути не нужно.
    print(i)
    #final.__next__()
print(f'Финальный результат: {new_list}')