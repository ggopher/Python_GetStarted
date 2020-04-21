"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

def generate(lst: list):
    """
    Функция, вычисляющая факториал каждого элемента списка
    :param lst: list
    :return: generator
    """

    for item in lst:
       fact = 1
       for el in range(1, item):
           fact *= el
       yield fact

for el in generate(range(1, 17)): #Создали генератор
    print(f'Финальный результат: {el}')