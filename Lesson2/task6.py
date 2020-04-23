goods = []
create_tuple = "y"
print("Введите стоп, чтобы прервать внесение товаров и получить аналитику")
i = 1
while create_tuple=="y":
    a = (i,
         {
        "Название:": input("Наименование товара:\n"),
        "Цена:": input("Цена товара:\n"),
        "Количество:": input("Количество товара:\n"),
        "Ед:": input("Единицы измерения:\n"),
         })
    goods.append(a)
    print(goods)
    i += i
    create_tuple = input("Продолжить внесение данных (y/n)")
    if create_tuple=='y':
        continue
    else:
        break
print(goods)

structure = ["Название:", "Цена:", "Количество:", "Ед:"]

"""
#Для отладки
goods = [
        (1, {'Название:': 'Компьютер', 'Цена:': '250', 'Количество:': '5', 'Ед:': 'шт'}),
        (2, {'Название:': 'Стол', 'Цена:': '260', 'Количество:': '6', 'Ед:': 'шт'})
        ]
"""
products_analytics = {} #{key: (a, b, c), }
result = []
for key in structure:
    #products_analytics[key] = result
    result = []
    for good in goods:
        result.append(good[1][key])
    products_analytics[key] = result
print(f'\n\n\nОтсортированный список{products_analytics}')
