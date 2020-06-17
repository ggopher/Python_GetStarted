"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.
"""
array = list(range(2, 100))
result = 0
print(array)

for itm in range(2, 10):
    for i in range(len(array)):

        if array[i] % itm == 0:
            result += 1
    print(f'количество чисел, кратных {itm}: {result}')
    result = 0