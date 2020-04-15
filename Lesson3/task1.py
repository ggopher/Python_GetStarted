def divide(a: int, b: int)-> int:
    """
    Функция деления
    :param a: int
    :param b: int
    :return: int or false
    """
    try:
        return a / b
    except ZeroDivisionError:
        return False
while True:
    print(divide(int(input("первое число:\n")), int(input("Второе число:\n"))))
