from functools import reduce
"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
"""

#РЕШЕНИЕ В ОДНУ СТРОКУ
fin = reduce(lambda x, y: x*y, [itm for itm in range(100, 1001) if not itm & 1])
print(f'Произведение всех элементов списка: {fin}')



#АЛЬТЕРНАТИВНОЕ РЕШЕНИЕ
new_list = list()
def generate(lst: list):
    """
    :param lst: list
    :return: generator
    """
    prev_item = 1
    for item in lst:
       if not item & 1:
            new_list.append(item)
            prev_item *= item
    yield prev_item

final = generate(range(100, 1001)) #Создали генератор
print(f'Финальный результат: {list(final)}')