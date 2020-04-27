list = [1, 2, 2, 5, 5, 5, 6, 7, 8]
print(f'Список: {list}')
while True:
    digit = input("введите число:\n")
    digit = int(digit)
    qnty = list.count(digit)-1 #считаем количество для сдвига
    if (qnty+1>=1):
        position = list.index(digit) + qnty
        list.insert(position,digit)
    else:
        list.append(digit)
    print(list)