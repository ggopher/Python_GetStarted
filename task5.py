while True:
    turnover = input('Введите выручку:\n')
    loss = input('Введите затраты:\n')
    turnover = int(turnover)
    loss = int(loss)
    profit = turnover-loss
    if loss<=turnover:
        total = profit/turnover
        balance = f'Прибыль: {profit}\n Рентабельность компании: {total*100}%\n'
        print(balance)
        employees = input("Введите численность сотрудников:")
        employees = int(employees)
        profit_per_employee = profit/employees
        print(f'Прибыль в пересчете на одного сотрудника: {profit_per_employee}\nЕще есть куда расти, до встречи!')

    else:
        print(f"Фирма-то убыточна ({profit}), попробуйте ввести данные другой компании")