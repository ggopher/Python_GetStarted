def sum_max(a: int, b: int, c: int)-> int:
    """
    Сумма наибольших двух элементов. помещаем все в список, сортируем его и выдаем сумму.
    :param a: int
    :param b: int
    :param c: int
    :return: int
    """
    sum = [a, b, c]
    sum.sort()
    return int(sum[1]) + int(sum[2])


sum = input("Введите три числа")
sum = sum.split()
print(f'Сумма максимальных двух чисел: {sum_max(*sum)}')

