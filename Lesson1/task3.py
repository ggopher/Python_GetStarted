while True:
    digit = input('Введите целое, положительное число\n')
    if digit.isdigit():
        digit1 = digit + digit
        digit2 = digit1 + digit
        final_digit = int(digit2) + int(digit1) + int(digit)
        print(f'{digit} + {digit1} + {digit2} = {final_digit}')
    else:
        print("Вы ввели не число\n")
        break