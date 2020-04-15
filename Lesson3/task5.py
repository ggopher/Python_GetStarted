sum = 0
def auto_sum(*args, fin=0):
    """
    Суммирует все параметры, если последний спецсимвол, то его игнорируем
    :param args: int
    :param fin: bool
    :return: int
    """
    result = 0
    if fin:
        for digit in args[0:-1]:
            result += int(digit)
    else:
        for digit in args:
            result += int(digit)
    return result

while True:
    digits = input("Введите строку чисел:\n")
    digits = digits.split(" ")
    if digits[-1]=="&":
        sum = sum + auto_sum(*digits, fin=1)
        print(sum)
        break
    else:
        sum = sum + auto_sum(*digits)
        print(sum)