"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
"""
list = [1, 2, 2, 2, 3, 4, 2, 1, 8, 7, 6, 9, 4, 2, 4, 63, 634, 7, 12, 6]
new_list = []
# new_list = [itm for itm in list if new_list.index(itm)]
def generate(list: list):

    for item in list:
        try:
            if new_list.index(item):
                yield item
        except ValueError:
            new_list.append(item)
            yield item

final = generate(list) #Создали генератор
for i in final:        #Быстренько прогоняем генератор, т.к. конкретно в этой задаче пошаговое управление по сути не нужно.
    print(i)
    #final.__next__()
print(f'Финальный результат: {new_list}')





#Расшифровка алгоритма:
# for i in range(20, 241):
#     if i%21==0 or i%20==0:
#         print(f'Число: {i} кратно 21, или 20')