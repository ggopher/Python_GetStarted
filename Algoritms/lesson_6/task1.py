from sys import getsizeof
"""
Итоги:

# type= <class 'list'>, size= 840, object= [2, 3, 4, .., 97, 98, 99]
# type= <class 'tuple'>, size= 824, object= (2, 3, 4, .., 97, 98, 99)
# type= <class 'dict'>, size= 4696, object= {2: 2, 3: 3, 4: 4, .., 97: 97, 98: 98, 99: 99}



Таким образом использование кортежа для этой задачи является наиболее оптимальным вариантом:
1. Меньше памяти занимает
2. Не изменяется в течение программы.
"""

def size_recursion(object, lev=0, recursion=0):
    print('\t' * lev, f'type= {object.__class__}, size= {getsizeof(object)}, object= {object}')
    if recursion == 1:
        if hasattr(object, '__iter__'):
            if hasattr(object, 'items'):
                    for itm in object.items():
                        size_recursion(itm, lev + 1)
            elif not isinstance(object, str):
                    for itm in object:
                        size_recursion(itm, lev + 1)



#######################################LIST#############################################################
# type= <class 'list'>, size= 840, object= [2, 3, 4, .., 97, 98, 99]

array = list(range(2, 100))
result = 0
# print(array)

for itm in range(2, 10):
    for i in range(len(array)):

        if array[i] % itm == 0:
            result += 1
    print(f'количество чисел, кратных {itm}: {result}')
    result = 0
size_recursion(array)
# size_recursion(array, recursion=1)


#######################################TUPLE#############################################################
print('*' * 50)
# type= <class 'tuple'>, size= 824, object= (2, 3, 4, .., 97, 98, 99)

array = tuple(range(2, 100))
result = 0
# print(array)

for itm in range(2, 10):
    for i in range(len(array)):

        if array[i] % itm == 0:
            result += 1
    print(f'количество чисел, кратных {itm}: {result}')
    result = 0
size_recursion(array)
# size_recursion(array, recursion=1)



#######################################DICT#############################################################
print('*' * 50)
# type= <class 'dict'>, size= 4696, object= {2: 2, 3: 3, 4: 4, .., 97: 97, 98: 98, 99: 99}

array = {x: x for x in range(2, 100)}
result = 0
# print(array)

for itm in range(2, 10):
    for i in range(len(array)):
        if array[i+2] % itm == 0:
            result += 1
    print(f'количество чисел, кратных {itm}: {result}')
    result = 0
size_recursion(array)
# size_recursion(array, recursion=1)