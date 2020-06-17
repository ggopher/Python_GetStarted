"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

Structure = namedtuple('Structure', 'name i ii iii iv sum average')
companies = list()

total_avg = 0
for itm in range(int(input("Введите количество компаний:\n"))):
    name = input('Введите название компании:\n')
    i = int(input('Введите прибыль за первый квартал:\n'))
    ii = int(input('Введите прибыль за второй квартал:\n'))
    iii = int(input('Введите прибыль за третий квартал:\n'))
    iv = int(input('Введите прибыль за четвертый квартал:\n'))
    sum = i + ii + iii + iv
    average = sum / 4
    total_avg += sum
    company = Structure(name, i, ii, iii, iv, sum, average)
    companies.append(company)
total_avg /= len(companies)

print(f'Общая средняя прибыль компаний: {total_avg}')

for itm in companies:
    if itm.average < total_avg:
        print(f'Средняя прибыль меньше общей ({total_avg}): Компания {itm.name}, {itm.average}')
    else:
        print(f'Средняя прибыль больше общей ({total_avg}): Компания {itm.name}, {itm.average}')



# cat1 = Structure('Овцебык', '100', '150', '80', '90', 12050, 123)
# cat2 = Structure('Овцебык2', '123100', '154120', '1480', 9120, 5512, 12783)
# cat3 = Structure('Овцебык3', '123980', '4120', '140', '91', 21233, 126783)
# cat4 = Structure('Овцебык4', '12340', '1120', '180', '920', 123, 121233)
# companies.append(cat1)
# companies.append(cat2)
# companies.append(cat3)
# companies.append(cat4)