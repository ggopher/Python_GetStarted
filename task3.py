while True:
    digit = input('Введите целое, положительное число\n')
    if digit.isdigit():
        digit1 = digit + digit
        digit2 = digit1 + digit
        final_digit = int(digit2) + int(digit1) + int(digit)
        print(final_digit)
    else:
        print("Вы ввели не число\n")
        break