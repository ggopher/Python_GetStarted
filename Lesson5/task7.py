"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

with open('task7.txt', 'r', encoding='UTF-8') as file:
    avg_profit = list()             #Средняя прибыль
    text = file.readlines()
    comp_profit = dict()
    for line in text:
        name, _, income, losses = line.split(' ')
        profit = int(income) - int(losses)
        comp_profit.update({name: profit})
        if profit>0:                            #Если прибыль, то включаем в список средней прибыли
            avg_profit.append(profit)
    final = [comp_profit, {'Средняя прибыль': sum(avg_profit)/len(avg_profit)}]
with open('task7.json', 'w', encoding='UTF-8') as file:
    json.dump(final, file)
    print(f'Наш JSON объект: {json.dumps(final)}')
