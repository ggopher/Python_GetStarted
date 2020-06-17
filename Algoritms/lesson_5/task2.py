"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""
from collections import deque
structure = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
# print(structure)

first = deque('A2')
second = deque('C4F')


if len(first) > len(second):
    first, second = second, first
second.reverse()
third = deque()

digits_left = -1
digit = 0
for i in second:
  third.append(structure[(structure.index(i) + structure.index(first[digits_left]) + digit) % 16])
  if (structure.index(i) + structure.index(first[digits_left])) >= 15:
    digit = 1
  else:
    digit = 0
  digits_left -= 1
  if digits_left == -len(first)-1:
    break

difference = len(second) - len(first)
if difference:
    for i in second[-difference]:
        third.append(structure[(structure.index(second[-difference]) + digit) % 16])
        if structure.index(second[-difference]) + 1 >= 15:
            digit = 1
        else:
            digit = 0
if digit == 1:
  third.append('1')
third.reverse()
print(third)


#Проверка
a = 'A2'
b = 'C4F'
c = hex(int(a, 16) + int(b, 16))
print(f'Проверка: {c}')