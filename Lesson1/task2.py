
# Метод 1
while True:
    seconds = input('Введите секунды\n')
    if seconds.isdigit():
        seconds = int(seconds)
        minutes = seconds/60
        seconds = seconds%60
        hours = minutes/60
        minutes = minutes%60
        output = "%02d:%02d:%02d" % (hours, minutes, seconds)
        print(output)

# Метод 2
#            min, sec = divmod(seconds, 60)
#           hour, min = divmod(min, 60)
#          output = "%02d:%02d:%02d" % (hour, min, sec)
#         print(output)

    else:
        print("Вы ввели не число\n")
        break