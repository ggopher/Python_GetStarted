"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

base_list = [1, 2, 2, 2, 3, 4, 2, 1, 8, 7, 6, 9, 4, 2, 4, 63, 634, 7, 12, 6, 12]
new_list = list()
# new_list = [itm for itm in list if new_list.index(itm)]

def generate(lst: list):
    """
    Функция, добавляющая значения, которые больше предыдушего, в новый список.
    :param lst: list
    :return: generator
    """
    prev_item = 999999999
    for item in lst:
       if item>prev_item:
            new_list.append(item)
       prev_item = item
    yield item

final = generate(base_list) #Создали генератор
list(final)

print(f'Финальный результат: {new_list}')



#второй способ (после разбора дз)
result = [itm for marker, itm in enumerate(base_list) if marker and itm > base_list[marker - 1]]
print(result)