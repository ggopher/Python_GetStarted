from sys import argv

def salary(hours: int, price: int, bonus: int)-> int:
    """
    Функция расчета заработной платы в зависимости от премии, часов и ставки.
    :param hours: int
    :param price: int
    :param bonus: int
    :return: int
    """
    return (hours * price) + bonus

if __name__ == '__main__':
         _, hours, price, bonus = argv
         print(f'ЗАРПЛАТА: {salary(int(hours), int(price), int(bonus))}')