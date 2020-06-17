from string import ascii_lowercase as str1
import random
"""
 Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
"""

a = int(input('Введите a:\n'))
b = int(input('Введите b:\n'))
start = str1.index(input('Введите букву начала:\n'))
end = str1.index(input('Введите букву конца:\n'))

print(f'Число в границах: {random.randrange(a, b)}')
print(f'Число float в границах: {random.uniform(a, b)}')
print(random.choices(str1[start:end]))
