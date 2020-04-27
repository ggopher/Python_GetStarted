def user(name='default', surname='default', birthday='default', city='default', email='default', phone='default'):
    """
    :param name: str
    :param surname: str
    :param birthday: str
    :param city: str
    :param email: str
    :param phone: str
    :return:  str
    """
    return f'Имя:{name}, Фамилия:{surname}, Дата рождения:{birthday}, Город:{city}, email:{email}, Телефон:{phone}'

data = []
data.append(input("Введите имя\n"))
data.append(input("Введите фамилию\n"))
data.append(input("Введите дату рождения\n"))
data.append(input("Введите город проживания\n"))
data.append(input("Введите email\n"))
data.append(input("Введите телефон\n"))

final = user(name=data[0], surname=data[1], birthday=data[2], city=data[3], email=data[4], phone=data[5])
print(final)

