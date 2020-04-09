while True:
    digit = input('Введите целое, положительное число\n')
    digit = int(digit)
    max_digit = 0
    while digit>0:
        right_digit = digit%10                              #Получаем правую цифру
        if right_digit>max_digit:                           #Сравниваем с наибольшей цифрой на данный момент
            max_digit = right_digit
        digit = digit//10                                   #Переходим к следующему порядку, отбрасывая остаток
    print(f'Самая большая цифра в числе:' + str(max_digit))