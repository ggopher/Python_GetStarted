"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""

class AnyError(Exception):
    def __init__(self, text):
        self.text = text

listing = list()
while True:
    inpt_data = input("Введите данные:\n")

    if inpt_data.lower() == 'стоп':
        print(listing)
        break
    try:
        if inpt_data.isdigit():
            listing.append(int(inpt_data))
        else:
            raise AnyError("Ошибка типа данных! Надо вводить числа!")
    except AnyError as mr:
        print(mr)

listing.append(int(1))

