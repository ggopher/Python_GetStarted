"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
struct = dict()
with open('task6.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        line = line.split(" ")
        for itm in line[1:]:
            i = itm.partition('(')[0]
            if i=="—":
                continue
            else:
                if struct.get(line[0])==None:
                    struct.update({line[0] : int(i)})  # Через update лучше, т.к. если вдруг добавится новая дисциплина, она все равно будет посчитана
                else:
                    struct.update({line[0] : struct[line[0]] + int(i)})
    print(struct)
