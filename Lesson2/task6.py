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
#matrix = zip(*goods)
print(goods)


goods = [
        (1, {'Название:': 'Компьютер', 'Цена:': '250', 'Количество:': '5', 'Ед:': 'шт'}),
        (2, {'Название:': 'Стол', 'Цена:': '250', 'Количество:': '6', 'Ед:': 'шт'})
        ]
goods_sorted = []
for i in goods:

     goods_sorted.append(i[1])

print(goods_sorted)
sorted = zip(goods_sorted)
print(list(sorted))
