"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class Complex():
    def __init__(self, digit):
        self.digit = digit

    def __add__(self, other):
        return  self.digit + other.digit

    def __mul__(self, other):
        return  self.digit * other.digit


complex1 = Complex(1 +2j)
complex2 = Complex(2 +3j)

complex3 = complex1 + complex2
complex4 = complex1 * complex2
print(complex3)
print(complex4)