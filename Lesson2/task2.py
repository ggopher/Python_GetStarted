"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

i = 0
list = []
while True:
    i += i
    answer = input("Введите элемент в список. Если вы больше не хотите вводить элементы, то напишите нет:\n")
    if (answer=="нет" or answer=="Нет"):
        break
    else:
        list.append(answer)


print("Список для работы:\n")
print(list)
print("Меняем местами элементы:\n")


i = 0
#list = ["1", "2", "3"]
switch = True
for value in list:
    i += 1
    if (switch==False):
        switch = True                   #Переключатель Чет/Нечет
    else:
        switch = False
        if (id(value)==id(list[-1])):       #Проверяем, а не последний ли у нас элемент
            break
        list.insert(i-1, list.pop(i))
print(list)