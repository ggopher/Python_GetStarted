"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
"""


"""
UPD: Изначально неправильно понял условие задачи и сформировал список без повторений (в коде, все работает, порядок сохраняется и т.д.):
Вот правильноее решение:
result = [itm for itm in base_list if base_list.count(itm) == 1]
print(result)
"""




base_list = [1, 2, 4, 2, 3, 4, 2, 1, 8, 7, 6, 9, 4, 2, 4, 63, 634, 7, 12, 6]
new_list = list()

def generate(lst: list):
    """
    Функция, создающая новый список из уникальных значений в том же порядке
    :param lst: list
    :return: generator
    """
    for item in lst:
        try:
            if new_list.index(item):
                yield item
        except ValueError:
            new_list.append(item)
            yield item

final = generate(base_list) #Создали генератор
list(final)
print(f'Финальный результат: {new_list}')



