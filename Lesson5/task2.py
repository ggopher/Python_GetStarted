"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк,количества слов в каждой строке.
"""

with open('task1.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    lines = text.split('\n')
    print(f'Количество строк: {len(lines)}')

    for itm in lines:
        print(f'В строке №{lines.index(itm)+1}, количество символов: {len(itm)}. Строка: {itm}')