"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
"""

# print([itm * itm for itm in range(100, 1001) if not itm & 1])
# Здесь непонятно как перемножить в однострочном генераторе.
new_list = []
def generate(list: list):
    """
    :param list: list
    :return: generator
    """
    prev_item = 1
    for item in list:
       if not item & 1:
            new_list.append(item)
            prev_item *= item
    yield prev_item

final = generate(range(100, 1001)) #Создали генератор
print(list(final))

# for i in final:        #Быстренько прогоняем генератор, т.к. конкретно в этой задаче пошаговое управление по сути не нужно.
#     print(i)
#     #final.__next__()
print(f'Финальный результат: {new_list}')