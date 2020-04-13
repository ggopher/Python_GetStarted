while True:
    result = input('Введите результат первого дня спортсмена:\n')
    final_result = input('Введите необходимый конечный результат:\n')
    result = int(result)
    final_result = int(final_result)
    day_number = 1
    while result<final_result:
        print(f'День {day_number}-й:{"%.2f" % result}')
        #result = "%.2f" % (result*1.1)
        result = result * 1.1
        day_number += 1
    print(f'На {day_number}-й день спортсмен достигнет результата не менее:{final_result} км.\n')