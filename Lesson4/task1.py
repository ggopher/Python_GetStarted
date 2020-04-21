"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
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
    try:
        _, hours, price, bonus = argv
        print(f'ЗАРПЛАТА: {salary(int(hours), int(price), int(bonus))}')

    except ValueError:
        print("Скрипт запущен без дополнительных параметров")




=IF(
$A4="";
"";
    IF(
        COUNTIF('Заявки'!$A:$A;E$1)=0;
        "";
        SUMIFS('Заявки'!$G:$G;'Заявки'!$A:$A;E$1;'Заявки'!$D:$D;$A4)+$B4)

)
