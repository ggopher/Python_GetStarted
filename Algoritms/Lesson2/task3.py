"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
# number = int(input('Введите число\n'))
# reverse = ''
# while number > 0:
#     reverse += str(number % 10)
#     number //= 10
# print(f'Перевернутое число: {reverse}')
#


user = input('0 to exit or some number to run code.\n')
list_of_numbers = [1]
for _ in range(1,int(user)):
    a = list_of_numbers[-1]/(-2)
    list_of_numbers.append(a)

sum_of_number = 0
for _ in list_of_numbers:
    sum_of_number += _
    print(sum_of_number)