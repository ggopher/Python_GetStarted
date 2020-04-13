greeting = "Добрый день!\n"
print(greeting)

house_name = input("Введите улицу, на которой вы живете:\n")

while True:
    house_number = input("Введите номер вашего дома:\n")
    if house_number.isdigit():
        house_number = int(house_number)
        break
    else:
        print("Вы ввели не число, введите номер правильно:\n")

#Переводим integer в string
house_number = str(house_number)


"""
#Проверяем возраст
if age >=18 and age <=35:
    print("Доступ разрешен")
elif age >12:
    print("Доступ разрешен в ограниченном режиме")
else:
    print("Доступ запрещен")
"""

print(greeting + "Улица, на которой вы живете:" + house_name + "\nНомер Вашего дома:" + house_number)
