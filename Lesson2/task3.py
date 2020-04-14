season = ["Зима", "весна", "лето", "осень"]
while True:
    seas = input("Введите число (работа по списку): \n")
    seas = int(seas)
    seas = (seas%12)/3
    print(season[int(seas)])

    season_dict = {1:"Зима",
    2:"Зима",
    3:"Весна",
    4:"Весна",
    5:"Весна",
    6:"Лето",
    7:"Лето",
    8:"Лето",
    9:"Осень",
    10:"Осень",
    11:"Осень",
    12:"Зима",
    }
    seas = input("Введите число (работа по словарю): \n")
    seas = int(seas)
    print(f'Словарь: {season_dict.get(seas)}')