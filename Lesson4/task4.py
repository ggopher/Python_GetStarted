"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
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





#Расшифровка алгоритма:
# for i in range(20, 241):
#     if i%21==0 or i%20==0:
#         print(f'Число: {i} кратно 21, или 20')