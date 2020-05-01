def sqrt(x: int, y: int)-> int:
    """
    Возводим x в степень y первый способ
    :param x: int
    :param y: int
    :return: int
    """
    return x**y
print(sqrt(2, -3))



def sqrt2(x: int, y: int)-> int:
    """
    Возводим x в степень y второй способ
    :param x: int
    :param y: int
    :return: int
    """
    y *= -1
    while (y > 1):
        x += x
        y -= 1
    x = 1 / x
    return x

print(sqrt2(2, -3))